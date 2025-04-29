"# coding_ppt"
go run replace.go
pyinstaller --onefile --windowed your_script.py


View: Pin Editor


powershell command:

$folderName = Read-Host "Enter folder name"
mkdir $folderName

$fileName = Read-Host "Enter file name"
New-Item -Path "$folderName\$fileName" -ItemType File

