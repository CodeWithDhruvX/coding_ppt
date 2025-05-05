import tkinter as tk
from tkinter import messagebox, scrolledtext
import json
import pyperclip

def convert_json_to_text():
    try:
        json_data = json.loads(input_text.get("1.0", tk.END))
        output_text.delete("1.0", tk.END)
        for slide in json_data:
            title = slide.get("title", "")
            content = slide.get("content", "")
            slide_type = slide.get("slide_type", "")
            formatted = f"--- {title} [{slide_type}] ---\n{content}\n\n"
            output_text.insert(tk.END, formatted)
    except json.JSONDecodeError as e:
        messagebox.showerror("JSON Error", f"Invalid JSON:\n{e}")

def copy_to_clipboard():
    result = output_text.get("1.0", tk.END)
    pyperclip.copy(result)
    messagebox.showinfo("Copied", "Converted text copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("JSON to Text Converter")

tk.Label(root, text="Paste JSON below:").pack()

input_text = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD)
input_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

tk.Button(root, text="Convert", command=convert_json_to_text).pack(pady=5)

tk.Label(root, text="Converted Text:").pack()

output_text = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
