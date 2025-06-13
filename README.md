# Zipy GUI - File Compressor (WIP)

**Zipy GUI** is the graphical version of the original **Zipy** command-line tool. Built using Python and Tkinter, this version lets users browse files and select an output folder through a friendly interface.

---

## Current Features

- Graphical user interface built with **Tkinter**
- **File browser** to select a file to compress
- **Folder browser** to choose the output directory for the zip file

---

## Features Missing (Compared to CLI Version)

| Feature | Status | Notes |
|--------|--------|-------|
| File compression logic | ❌ Missing | Currently, the GUI collects file and output paths but doesn’t zip the file yet |
| Decompression | ❌ Not implemented | GUI version cannot unzip files yet |
| Zip file naming | ❌ Not implemented | User can't specify a custom name for the output `.zip` file |
| User feedback | ❌ Lacking | No message boxes or status confirmation after an action |
| Compress multiple files | ❌ Not yet supported | CLI version allows adding files in a loop; GUI currently supports one file selection |

---

## How to Run

```bash
python zip_gui.py


## TODO / Feature Roadmap
 [] Add zip compression logic after user selects file and output folder

 [] Add unzip functionality with folder extraction

 [] Allow user to name the zip file before compression

 [] Add success/failure messages after actions

 [] Add multi-file selection and batch compression

 