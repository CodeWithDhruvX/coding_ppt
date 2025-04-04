import json
import tkinter as tk
from tkinter import filedialog

def extract_text_slides(data):
    text_slides = []
    
    for item in data:
        if item.get("slide_type") == "code":
            text_slides.append({"title": item["title"], "content": item["content"]})
    
    return text_slides

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON Files", "*.json")])
    return file_path

def save_file(data):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Save JSON File", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    
    if file_path:
        with open(file_path, "w", encoding="utf-8") as output_file:
            json.dump(data, output_file, ensure_ascii=False, indent=4)
        print(f"Filtered text slides have been saved to {file_path}")
    else:
        print("Save operation canceled.")

# Select input JSON file
input_file = select_file()
if input_file:
    with open(input_file, "r", encoding="utf-8") as file:
        json_data = json.load(file)
    
    # Extract text slides
    text_slides_list = extract_text_slides(json_data)
    
    # Save output JSON file
    save_file(text_slides_list)
else:
    print("File selection canceled.")
