from dubslib.io import read_from_file, write_to_file, Persistence

from_file_dir = "/home/donald-reilly/Documents/DubsWorkspace/SourceCode/python/DUBSLib/examples/from_file"

to_file_dir = "/home/donald-reilly/Documents/DubsWorkspace/SourceCode/python/DUBSLib/examples/to_file"
from_files = (
    f"{from_file_dir}/main.md",
    f"{from_file_dir}/mock_text.txt"
)

for file in from_files:
    rf = read_from_file(file, "List")
    print(type(rf))
    for line in rf:
        print(line, end="")

for file in from_files:
    rf = read_from_file(file, "String")
    print(type(rf))
    print(rf)

for file in from_files:
    rf = read_from_file(file, "Yield")
    print(type(rf))
    for line in rf:
        print(line, end="")

