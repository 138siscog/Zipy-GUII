from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Zippy")
root.geometry("400x300")

file_var = StringVar()      # Variable to hold the file path
output_var = StringVar()    # Variable to hold the output folder path

def browse_file():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("all files", "*.*"), ("Text files", "*.txt*"))
    )
    if filename:
        file_var.set(filename)  # Set the entry box to the selected file path

def browse_output_folder():
    foldername = filedialog.askdirectory(
        initialdir="/",
        title="Select Output Folder"
    )
    if foldername:
        output_var.set(foldername)  # Set the entry box to the selected folder path


########File Select#######

frm = ttk.Frame(root, padding=5)
frm.pack(pady=20)

entry = ttk.Entry(frm, textvariable=file_var, width=40)
entry.grid(column=0, row=1, columnspan=3, padx=5)

browse_button = ttk.Button(frm, text="Browse Files", command=browse_file)
browse_button.grid(column=3, row=1, pady=5)

########Output Selection#####

output_entry = ttk.Entry(frm, textvariable=output_var, width=40)
output_entry.grid(column=0, row=2, columnspan=3, padx=5)

output_button = ttk.Button(frm, text="Output Folder", command=browse_output_folder)
output_button.grid(column=3, row=2, pady=5)

root.mainloop()