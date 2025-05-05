import tkinter as tk
from tkinter import scrolledtext, messagebox
import json
import pyperclip

def generate_script():
    try:
        raw_json = input_text.get("1.0", tk.END).strip()
        slide = json.loads(raw_json)

        title = slide.get("title", "").strip()
        content = slide.get("content", "").strip()
        slide_type = slide.get("slide_type", "").strip().lower()

        if not (title and content and slide_type):
            raise ValueError("Har slide me title, content aur slide_type hona chahiye.")

        # Get video duration from entry (default to 5 if invalid)
        try:
            minute = int(duration_entry.get().strip())
            if minute <= 0:
                raise ValueError
        except:
            minute = 5

        output = f"""Main ek {minute} minute ka educational YouTube video bana raha hoon Golang ke upar, jo bilkul beginners ke liye hai — especially India ke programmers ke liye.

Yeh raha ek slide ka JSON format:

   {{
      "title": "{title}",
      "content": "{content}",
      "slide_type": "{slide_type}"
    }}

[Aise hi sabhi slides ke liye repeat karna hoga]

Ab in slides ke base par ek YouTube video ka script likho. Tone bilkul **friendly aur simple** honi chahiye — jaise hum kisi junior ya dost ko casually explain kar rahe ho.

✅ Tone aur Style ke Rules:
- Use **bolne jaisi English**, jaise tum real life me explain karte ho.
- Bhasha simple, clear aur beginner-friendly honi chahiye.
- **Indian relatable examples** do — jaise classroom, coding assignments, ya job interviews.
- Complicated English avoid karo. Na zyada western, na zyada formal.
- **100% Hinglish me likhna hai**
- Ek teacher jaisa tone hona chahiye — jo student ko step by step samjha raha ho.

🎯 Instructions:

Start karo first slide se:
- Pehle title aur content ko samjhao, simple language me.
- Real life ya beginner-level coding examples lo.
- Batayo ki **ye topic kyu important hai**, aur real coding me kaise kaam aayega.

📘 Agar `code` slide hai:
- Code ko line by line explain karo.
- Har part ka kaam batao — simple aur practical way me.
- Beginners ko common galtiyon se bachao.

📊 Agar `table` slide hai:
- Har row aur column ko clear kar ke samjhao.
- Concepts ya values ko compare karo — simple terms me.
- Viewer ko batayo ki is info ko actual dev work me kaise use kare.

⛔ Rules:
- Koi intro ya outro nahi chahiye.
- Ek baar me sirf ek slide explain karo.
- Assume karo ki viewer Golang aur programming me naya hai.
- Agar slide_type `text` ho, to sirf theory explain karo — code include mat karo."""

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output)

    except Exception as e:
        messagebox.showerror("Error", f"Script generate nahi kar paya.\n\n{e}")

def copy_script():
    content = output_text.get("1.0", tk.END).strip()
    if content:
        pyperclip.copy(content)
    else:
        messagebox.showwarning("Warning", "Kuch copy karne layak content nahi mila.")

# Setup GUI
root = tk.Tk()
root.title("Golang Slide Prompt Formatter - Hinglish Version")

tk.Label(root, text="Slide ka JSON daalo yahan:").pack(anchor='w', padx=10, pady=(10, 0))
input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10)
input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

tk.Label(root, text="Video Duration (minutes me):").pack(anchor='w', padx=10, pady=(10, 0))
duration_entry = tk.Entry(root)
duration_entry.insert(0, "5")  # default value
duration_entry.pack(fill=tk.X, padx=10, pady=(0, 5))

tk.Button(root, text="YouTube Prompt Banao", command=generate_script).pack(pady=5)

tk.Button(root, text="Clipboard Me Copy Karo", command=copy_script).pack(pady=5)

tk.Label(root, text="Formatted Prompt Yahan Milega:").pack(anchor='w', padx=10)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20)
output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)



root.mainloop()
