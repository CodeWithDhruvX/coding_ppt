// file: executor/main.go

package main

import (
	"database/sql"
	"log"
	"os/exec"
	"time"

	_ "github.com/lib/pq"
)

const dbConnStr = "user=root password=root dbname=task_scheduler sslmode=disable"

type Task struct {
	ID       int
	Name     string
	Command  string
	Interval int
	LastRun  sql.NullTime
}

func main() {
	for {
		runDueTasks()
		time.Sleep(30 * time.Second) // check every 30 seconds
	}
}

func runDueTasks() {
	db, err := sql.Open("postgres", dbConnStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	rows, err := db.Query("SELECT id, name, command, interval, last_run FROM tasks")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	now := time.Now()

	for rows.Next() {
		var t Task
		err := rows.Scan(&t.ID, &t.Name, &t.Command, &t.Interval, &t.LastRun)
		if err != nil {
			log.Println(err)
			continue
		}

		shouldRun := !t.LastRun.Valid || now.Sub(t.LastRun.Time) > time.Duration(t.Interval)*time.Second

		if shouldRun {
			log.Printf("Running task: %s\n", t.Name)
			go execCommand(t.Command)

			_, err := db.Exec("UPDATE tasks SET last_run = $1 WHERE id = $2", now, t.ID)
			if err != nil {
				log.Println("Failed to update last_run:", err)
			}
		}
	}
}

func execCommand(command string) {
	cmd := exec.Command("powershell", "-Command", command) // works on Linux/macOS. For Windows, use "cmd", "/C"
	err := cmd.Start()
	if err != nil {
		log.Println("Failed to start command:", err)
	}
	cmd.Wait()
}
