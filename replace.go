package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

type Slide struct {
	Title     string      `json:"title"`
	Content   interface{} `json:"content"`
	SlideType string      `json:"slide_type"`
}

func readJSONFile(path string) ([]Slide, error) {
	fileBytes, err := ioutil.ReadFile(path)
	if err != nil {
		return nil, err
	}
	var slides []Slide
	err = json.Unmarshal(fileBytes, &slides)
	if err != nil {
		return nil, err
	}
	return slides, nil
}

func writeJSONFile(path string, data []Slide) error {
	fileBytes, err := json.MarshalIndent(data, "", "  ")
	if err != nil {
		return err
	}
	return ioutil.WriteFile(path, fileBytes, 0644)
}

func main() {
	originalPath := "originalSlides.json"
	updatedPath := "updatedSlides.json"
	outputPath := "finalSlides.json"

	originalSlides, err := readJSONFile(originalPath)
	if err != nil {
		fmt.Printf("Error reading original slides: %v\n", err)
		return
	}

	updatedSlides, err := readJSONFile(updatedPath)
	if err != nil {
		fmt.Printf("Error reading updated slides: %v\n", err)
		return
	}

	// Create a map for quick access
	updatedMap := make(map[string]Slide)
	for _, slide := range updatedSlides {
		updatedMap[slide.Title] = slide
	}

	// Merge logic
	finalSlides := make([]Slide, 0, len(originalSlides))
	for _, slide := range originalSlides {
		if updated, exists := updatedMap[slide.Title]; exists {
			slide.Content = updated.Content
			slide.SlideType = updated.SlideType
		}
		finalSlides = append(finalSlides, slide)
	}

	// Write to file
	err = writeJSONFile(outputPath, finalSlides)
	if err != nil {
		fmt.Printf("Error writing final slides: %v\n", err)
		return
	}

	fmt.Println("Slides merged successfully! Output written to", outputPath)
}
