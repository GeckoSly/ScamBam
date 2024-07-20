import tkinter as tk
from tkinter import messagebox, filedialog

class ScamBamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamBam GUI")

        # Text area to display comments
        self.text_area = tk.Text(root, wrap=tk.WORD, height=20, width=50)
        self.text_area.pack(padx=10, pady=10)

        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Delete button
        self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_comment)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Report button
        self.report_button = tk.Button(button_frame, text="Report", command=self.report_comment)
        self.report_button.pack(side=tk.LEFT, padx=5)

        # Hide button
        self.hide_button = tk.Button(button_frame, text="Hide", command=self.hide_comment)
        self.hide_button.pack(side=tk.LEFT, padx=5)

        # Load comments button
        self.load_button = tk.Button(root, text="Load Comments", command=self.load_comments)
        self.load_button.pack(pady=10)

    def load_comments(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                comments = file.read()
                self.text_area.insert(tk.END, comments)

    def delete_comment(self):
        selected_text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
            messagebox.showinfo("Info", "Comment deleted.")
        else:
            messagebox.showwarning("Warning", "No comment selected.")

    def report_comment(self):
        selected_text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            messagebox.showinfo("Info", f"Reported comment: {selected_text}")
        else:
            messagebox.showwarning("Warning", "No comment selected.")

    def hide_comment(self):
        selected_text = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            self.text_area.tag_add("hidden", tk.SEL_FIRST, tk.SEL_LAST)
            self.text_area.tag_config("hidden", elide=True)
            messagebox.showinfo("Info", "Comment hidden.")
        else:
            messagebox.showwarning("Warning", "No comment selected.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScamBamApp(root)
    root.mainloop()
