import json
import tkinter as tk
from tkinter import filedialog

def load_json_file(title):
    file_path = filedialog.askopenfilename(title=title, filetypes=[("JSON files", "*.json")])
    if not file_path:
        return None
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def replace_slide_content(old_json, new_json):
    if isinstance(old_json, list):
        old_json = {"slides": old_json}
    if isinstance(new_json, list):
        new_json = {"slides": new_json}
    
    if not isinstance(old_json, dict) or "slides" not in old_json:
        print("Error: Invalid format in old JSON. Expected a dictionary with a 'slides' key.")
        return old_json
    if not isinstance(new_json, dict) or "slides" not in new_json:
        print("Error: Invalid format in new JSON. Expected a dictionary with a 'slides' key.")
        return old_json
    
    slide_text_mapping = {slide["id"]: slide["text"] for slide in new_json["slides"] if "id" in slide and "text" in slide}
    
    updated_slides = []
    for slide in old_json["slides"]:
        if "id" in slide and slide["id"] in slide_text_mapping:
            slide["text"] = slide_text_mapping[slide["id"]]
        updated_slides.append(slide)  # Maintain original order
    
    old_json["slides"] = updated_slides
    return old_json

def main():
    root = tk.Tk()
    root.withdraw()
    
    old_json = load_json_file("Select Old JSON File")
    new_json = load_json_file("Select New JSON File")
    output_file = filedialog.asksaveasfilename(title="Save Output JSON", defaultextension=".json", filetypes=[("JSON files", "*.json")])
    
    if old_json and new_json and output_file:
        updated_json = replace_slide_content(old_json, new_json)
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(updated_json, file, indent=4, ensure_ascii=False)
        print(f"Updated JSON saved as: {output_file}")
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
