# Function to create folder and file, then open the file
function Create-FolderAndFile {
    # Prompt the user for folder name and file name
    $folderName = Read-Host "Enter the folder name"
    $fileName = Read-Host "Enter the file name (with extension, e.g., file.txt)"

    # Check if the folder exists, create it if it doesn't
    if (-not (Test-Path -Path $folderName)) {
        New-Item -ItemType Directory -Path $folderName
        Write-Host "Folder '$folderName' created."
    } else {
        Write-Host "Folder '$folderName' already exists."
    }

    # Define the full file path
    $filePath = Join-Path -Path $folderName -ChildPath $fileName

    # Create the file if it doesn't exist
    if (-not (Test-Path -Path $filePath)) {
        New-Item -ItemType File -Path $filePath
        Write-Host "File '$fileName' created inside '$folderName'."
    } else {
        Write-Host "File '$fileName' already exists in '$folderName'."
    }

    # Open the file
    Start-Process $filePath
    Write-Host "Opening '$filePath'..."
}

# Call the function to run the process
Create-FolderAndFile
