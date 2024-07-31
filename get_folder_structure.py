import os
import tkinter as tk
from tkinter import filedialog

def get_folder_structure(folder_path, indent=""):
    structure = []
    for item in sorted(os.listdir(folder_path)):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            structure.append(f"{indent}|-{item}")
            structure.extend(get_folder_structure(item_path, indent + "    "))
        else:
            structure.append(f"{indent}|-{item}")
    return structure

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")
    print(f"Selected folder: {folder_path}")
    if folder_path:
        folder_name = os.path.basename(folder_path)
        structure = [f"- {folder_name}"]
        structure.extend(get_folder_structure(folder_path, "    "))
        
        result_window = tk.Toplevel(root)
        result_window.title("Folder Structure")
        result_window.geometry("600x400")
        result_text = tk.Text(result_window, wrap=tk.NONE)
        result_text.pack(expand=True, fill=tk.BOTH)
        
        for line in structure:
            result_text.insert(tk.END, line + "\n")
        
        result_text.config(state=tk.DISABLED)
        
        print("Result window created")
        result_window.update()
        root.mainloop()
    else:
        print("No folder selected.")

if __name__ == "__main__":
    print("Script started")
    select_folder()
    print("Script ended")