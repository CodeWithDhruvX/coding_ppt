import tkinter as tk
from tkinter import ttk, messagebox
import json
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound

# --- Smart Language Detector ---
def detect_language(content):
    try:
        lexer = guess_lexer(content)
        language = lexer.name.lower()

        if "python" in language:
            return "python"
        elif "javascript" in language:
            return "javascript"
        elif "go" in language:
            return "go"
        elif "java" in language:
            return "java"
        elif "c++" in language or "cpp" in language:
            return "cpp"
        elif "c#" in language:
            return "csharp"
        elif "html" in language:
            return "html"
        elif "css" in language:
            return "css"
        elif "php" in language:
            return "php"
        elif "ruby" in language:
            return "ruby"
        else:
            return "plaintext"
    except ClassNotFound:
        return "plaintext"

# --- Core Engine ---
def generate_prompt(obj, selected_mode, add_best_mistakes):
    title = obj.get('title', 'Untitled')
    content = obj.get('content', '')
    slide_type = obj.get('slide_type', 'code')

    language = detect_language(content)

    output = f"### 📘 Title: {title}\n\n"
    output += "---\n\n"

    if selected_mode == "Code Creation Mode":
        output += f"### 🛠 Code Creation\n"
        output += f"Write a code snippet based on the following content:\n\n"
        output += f"**Content Idea:** {content}\n\n"
        output += f"### 💻 Code ({language})\n"
        output += f"```{language}\n"
        output += f"// Your code starts here...\n"
        output += f"```\n\n"
        output += "---\n\n"
        output += "### 🧠 Explanation:\n- Explain what this newly created code does.\n\n"

        if add_best_mistakes:
            output += "### ✅ Best Practices:\n- Mention best practices for this type of code.\n\n"
            output += "### ⚡ Common Mistakes:\n- Highlight mistakes to avoid.\n\n"

        return output

    # Normal code explanation flow
    output += f"### 💻 Code ({language})\n"
    output += f"```{language}\n{content}\n```\n\n"
    output += "---\n\n"

    if selected_mode == "Simple Mode":
        output += "### 🧠 Explanation (Simple):\n- Basic description of the code.\n\n"
    elif selected_mode == "Detailed Mode":
        output += "### 🧠 Explanation (Detailed):\n"
        output += "- Explain line-by-line what the code does.\n"
        output += "- Use analogies if possible.\n\n"
        output += "### ✅ Best Practices:\n- Mention best practices related to this code.\n\n"
        output += "### 🌍 Real-World Applications:\n- Mention where this code would be useful.\n\n"
        output += "### ⚡ Common Mistakes:\n- Highlight mistakes developers make with such code.\n\n"
    elif selected_mode == "Deep Dive Mode":
        output += "### 🧠 Explanation (Deep Dive):\n"
        output += "- Line-by-line explanation.\n"
        output += "- Memory size and performance notes.\n"
        output += "- Internal working of types.\n\n"
        output += "### ✅ Best Practices:\n- Optimize for large-scale usage.\n\n"
        output += "### 🌍 Real-World Applications:\n- Banking, trading systems, large datasets.\n\n"
        output += "### ⚡ Common Mistakes:\n- Overflow, portability mistakes.\n\n"
    elif selected_mode == "Interview Mode":
        output += "### 🧠 Explanation (Interview Focus):\n"
        output += "- How to explain in an interview (STAR format).\n\n"
        output += "### 🎯 Interview Pro Tip:\n- Focus on type safety and optimization.\n\n"
    elif selected_mode == "Mistake Hunt Mode":
        output += "### ⚡ Common Mistakes (Mistake Hunt Mode):\n"
        output += "- Mistakes people usually make and how to fix them.\n\n"
    elif selected_mode == "Pro Developer Mode":
        output += "### 🧠 Explanation (Pro Developer Focus):\n"
        output += "- Production-ready code tips.\n"
        output += "- Scalability, readability, maintainability.\n\n"
    elif selected_mode == "Architecture Mode":
        output += "### 🏛 System Architecture Connection:\n"
        output += "- How this code fits into large-scale systems.\n\n"
    else:
        output += "### 🧠 Explanation:\n- General explanation mode.\n\n"

    return output

# --- GUI App ---
def generate_output():
    try:
        input_text = input_box.get("1.0", tk.END).strip()
        objs = json.loads(input_text)

        if not isinstance(objs, list):
            objs = [objs]  # Wrap single object into list

        selected_mode = mode_var.get()
        add_best_mistakes = add_best_mistakes_var.get()
        final_output = ""

        for obj in objs:
            prompt = generate_prompt(obj, selected_mode, add_best_mistakes)
            final_output += prompt + "\n\n"

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, final_output)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input format!\n\n{str(e)}")

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_box.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Output copied to clipboard!")

# --- Main window ---
root = tk.Tk()
root.title("Prompt Generator App with Language Detection and Code Creation")
root.geometry("1000x900")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Paste JSON Object(s):").pack(anchor="w")
input_box = tk.Text(input_frame, width=120, height=10)
input_box.pack()

# Mode Selector
mode_frame = tk.Frame(root)
mode_frame.pack(pady=5)

tk.Label(mode_frame, text="Select Flavor Mode:").pack(side="left", padx=5)

mode_var = tk.StringVar()
mode_dropdown = ttk.Combobox(mode_frame, textvariable=mode_var, width=35)
mode_dropdown['values'] = (
    "Simple Mode",
    "Detailed Mode",
    "Deep Dive Mode",
    "Interview Mode",
    "Pro Developer Mode",
    "Mistake Hunt Mode",
    "Architecture Mode",
    "Code Creation Mode",   # <-- Added new mode
)
mode_dropdown.current(7)  # Default to Detailed Mode
mode_dropdown.pack(side="left", padx=5)

# Checkbox for "Best Practices + Mistakes" in Code Creation Mode
add_best_mistakes_var = tk.BooleanVar()
add_best_mistakes_checkbox = tk.Checkbutton(root, text="Add Best Practices and Mistakes (Code Creation Mode)", variable=add_best_mistakes_var)
add_best_mistakes_checkbox.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Generate Output", command=generate_output).pack(side="left", padx=10)
tk.Button(button_frame, text="Copy to Clipboard", command=copy_output).pack(side="left", padx=10)

# Output Frame
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

tk.Label(output_frame, text="Generated Prompt Output:").pack(anchor="w")
output_box = tk.Text(output_frame, width=120, height=20)
output_box.pack()

# Plan / Info Section
plan_frame = tk.LabelFrame(root, text="🏗 Plan for Code Structure", padx=10, pady=10)
plan_frame.pack(padx=10, pady=10, fill="both")

plan_info = (
    "Mode                    | Description\n"
    "-------------------------|------------------------------------------------------------\n"
    "Simple Mode             | Short explanations, focus on essentials only.\n"
    "Detailed Mode           | Full explanations, beginner-friendly, real-world analogies.\n"
    "Deep Dive Mode          | Add memory usage, performance impacts, underlying internals.\n"
    "Interview Mode          | Explain code in interview with STAR method.\n"
    "Pro Developer Mode      | Write production-level, scalable, clean, optimized code.\n"
    "Mistake Hunt Mode       | Focus on common mistakes and how to fix them.\n"
    "Architecture Mode       | Connect snippets to large system or microservices architecture.\n"
    "Code Creation Mode      | Create full code from content idea and explain it.\n"
)

plan_text = tk.Text(plan_frame, height=12, width=100, wrap="none", bg="#f8f8f8")
plan_text.insert(tk.END, plan_info)
plan_text.config(state="disabled")
plan_text.pack()

root.mainloop()
