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





# prompts text


# You are an expert career coach and PowerPoint storyteller.

# Given the behavioral interview question below, create multiple PowerPoint slides (4–5) using the SOAR framework (Situation, Obstacle, Action, Result).

# Each slide should have:

# A "title" relevant to the section (e.g., Situation, Action Taken, Final Outcome)

# A "slide_type" of "behavioral"

# A short "content" string, 2–4 sentences each.

# Behavioral Interview Question:
# "Tell me about a time something felt unfair."

# Output JSON Format:
# json
# [
#   {
#     "title": "Slide Title Here",
#     "slide_type": "behavioral",
#     "content": "Short, concise description here."
#   },
#   ...
# ]
# Please ensure the output is well-structured and formatted for direct import into a PowerPoint presentation generator. Use professional tone.


# Write a detailed, engaging, and professional story following the chosen method. The story should be relevant to an Indian corporate work environment, use realistic examples (e.g., IT services, consulting, MNC culture), and include a clear context, your actions, results, and a meaningful takeaway or reflection. Make the tone conversational yet polished, suitable for LinkedIn posts, YouTube videos, or presentations.

# At the beginning of your answer, mention which storytelling method you chose and why it fits this question."** please make sure that this story is based on the created slide content in the above format

# please make sure that script is gibing based on the slide scence



