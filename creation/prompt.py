import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

# JSON File Path
PROMPT_FILE_PATH = PROMPT_FILE_PATH = os.path.join(os.path.dirname(__file__), "prompts.json")


def load_prompt_templates(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("JSON file not found.")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def copy_to_clipboard(text, root):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    # messagebox.showinfo("Copied", "Prompt copied to clipboard!")

def run_gui():
    templates = load_prompt_templates(PROMPT_FILE_PATH)

    root = tk.Tk()
    root.title("Prompt Viewer")
    root.geometry("600x400")

    template_var = tk.StringVar()
    template_ids = list(templates.keys())

    def update_prompt_display(event=None):
        selected_id = template_var.get()
        if selected_id in templates:
            prompt = templates[selected_id]["prompt"]
            prompt_display.config(state="normal")
            prompt_display.delete("1.0", "end")
            prompt_display.insert("1.0", prompt)
            # prompt_display.config(state="disabled")

    def copy_prompt():
        text = prompt_display.get("1.0", "end").strip()
        if text:
            copy_to_clipboard(text, root)

    ttk.Label(root, text="Select a Prompt Template:").pack(anchor="w", padx=10, pady=(10, 0))

    template_dropdown = ttk.Combobox(root, textvariable=template_var, values=template_ids, state="readonly")
    template_dropdown.pack(fill="x", padx=10, pady=5)
    template_dropdown.bind("<<ComboboxSelected>>", update_prompt_display)
    template_dropdown.current(0)
    template_var.set(template_ids[0])

    prompt_display = tk.Text(root, height=10, wrap="word")
    prompt_display.pack(fill="both", expand=True, padx=10, pady=10)

    copy_btn = ttk.Button(root, text="Copy to Clipboard", command=copy_prompt)
    copy_btn.pack(pady=5)

    update_prompt_display()

    root.mainloop()

if __name__ == "__main__":
    run_gui()
