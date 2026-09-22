# PYTHON 3.12 FILE MANAGEMENT COMPREHENSIVE GUIDE

---

|**INDEX**|**LINKS TO DOCS**|
|---------|-----------------|
|1 **[WORKING WITH DIRECTORIES AND PATHS](#1-working-with-directories-and-paths)**|1 **[PATHLIB](https://docs.python.org/3.12/library/pathlib.html)**|
|2 **[WRITING TO FILES](#2-writing-to-files)**|2 **[PURE-PATHS](https://docs.python.org/3.12/library/pathlib.html#pure-paths)**|
|3 **[APPENDING TO FILES](#3-appending-to-files)**|3 **[MK-DIR](https://docs.python.org/3.12/library/pathlib.html#pathlib.Path.mkdir)**|
|4 **[READING FROM FILES](#4-reading-from-files)**|4 **[WRITE TEXT](https://docs.python.org/3.12/library/pathlib.html#pathlib.Path.write_text)**|
|5 **[WRITING & READING BINARY DATA](#5-writing--reading-binary-data)**|5 **[READ TEXT](https://docs.python.org/3.12/library/pathlib.html#pathlib.Path.read_text)**|
|6 **[FILE METADATA AND CLEANUP](#6-file-metadata-and-cleanup)**|6 **[PATH EXISTS](https://docs.python.org/3.12/library/pathlib.html#pathlib.Path.exists)**|
||7 **[UNLINK](https://docs.python.org/3.12/library/pathlib.html#pathlib.Path.unlink)**|
||8 **[READ TEXT](https://docs.python.org/3.12/library/pathlib.html#pathlib.Path.read_text)**|
---
# 1: WORKING WITH DIRECTORIES AND PATHS



```python
# First, we import the modern 'pathlib' module for object-oriented path handling.
from pathlib import Path

# Also import the 'os' module for fallback or environment tasks.
import os
# 1. Get the Current Working Directory (CWD)

current_dir = Path.cwd()
print(f"Current Directory: {current_dir}")

# 2. Define a target folder path inside the working directory
# Pathlib overloads the '/' operator to securely join paths cross-platform.

output_folder = current_dir / "my_docs"

# 3. Create a Directory safely if it does not exist
# 'parents=True' creates missing parent folders. 'exist_ok=True' ignores error if it exists.
output_folder.mkdir(parents=True, exist_ok=True)
print(f"Ensured folder exists: {output_folder}")

# 4. Define our target files
text_file_path = output_folder / "sample_text.txt"
binary_file_path = output_folder / "sample_data.bin"
```

# 2: WRITING TO FILES

```python
# APPROACH A: Traditional open() with Context Manager ('with' statement)
# The 'with' statement ensures the file auto-closes safely, even on exceptions.
# Modes: 'w' (Write/Overwrite), 'a' (Append), 'x' (Exclusive creation)
# Encoding: Explicitly setting 'utf-8' prevents platform-dependent text bugs.
print("\n--- Writing to File ---")
lines_to_write = ["Line 1: Hello Python!\n", "Line 2: Learning file handling.\n"]

with open(text_file_path, mode="w", encoding="utf-8") as file:
    # write() writes a single string
    file.write("Header: Document Initialization\n")
    # writelines() accepts an iterable of strings
    file.writelines(lines_to_write)

# APPROACH B: Quick Modern Pathlib Methods
# Ideal for writing an entire string or bytes block in one command without open().
text_file_path.write_text("Overwritten text using pathlib!", encoding="utf-8")
```

# 3: APPENDING TO FILES

```python
# Open the file in 'a' (append) mode to add new data to the bottom without erasing.
with open(text_file_path, mode="a", encoding="utf-8") as file:
    file.write("\nLine 3: This sentence was appended.")
```

# 4: READING FROM FILES

```python
print("\n--- Reading Methods ---")

# Method 1: Read the entire file as a single string (.read())
with open(text_file_path, mode="r", encoding="utf-8") as file:
    entire_content = file.read()
    print(f"Method 1 Output:\n{entire_content}")

# Method 2: Read line-by-line using a memory-efficient loop
# Highly recommended for massive files so you don't load gigabytes into RAM at once.
with open(text_file_path, mode="r", encoding="utf-8") as file:
    print("Method 2 Line Loop:")
    for line_number, line in enumerate(file, start=1):
        # .strip() removes trailing newlines (\n) or whitespaces
        print(f"  {line_number}: {line.strip()}")

# Method 3: Quick read with Pathlib
quick_read = text_file_path.read_text(encoding="utf-8")
```

# 5: WRITING & READING BINARY DATA

```python
# Use 'wb' (write binary) and 'rb' (read binary) modes for non-text (images, zipped, raw bytes).
# Notice: No 'encoding' parameter is allowed when dealing with raw bytes.
print("\n--- Binary Mode ---")
raw_bytes = b"\x48\x65\x6c\x6c\x6f"  # Hexadecimal bytes for "Hello"

with open(binary_file_path, mode="wb") as b_file:
    b_file.write(raw_bytes)

with open(binary_file_path, mode="rb") as b_file:
    binary_content = b_file.read()
    print(f"Read Binary Data: {binary_content} -> Decoded: {binary_content.decode('utf-8')}")
```

# 6: FILE METADATA AND CLEANUP

```python
print("\n--- Metadata & Cleanup ---")

# Check file existence and type
if text_file_path.exists():
    print(f"File Name: {text_file_path.name}")
    print(f"File Extension: {text_file_path.suffix}")
    print(f"Is it a file? {text_file_path.is_file()}")
    print(f"File Size: {text_file_path.stat().st_size} bytes")

# Optional Cleanup: Delete files and directory safely
# To test cleanup, uncomment the 3 lines below:
# text_file_path.unlink(missing_ok=True)       # Deletes file
# binary_file_path.unlink(missing_ok=True)     # Deletes file
# output_folder.rmdir()                        # Deletes folder (must be empty first)

```