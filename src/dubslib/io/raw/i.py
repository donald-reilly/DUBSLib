from pathlib import Path

def _yield_from_file(file_path: str):
    """
    Yeild lines from the provided file. Defaults to utf-8 encoding.

    Params:
        file_path(str): Path to the file.

    Yields:
        str: Each line in the file (including newline characters).
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        yield from rawtext

def _list_from_file(file_path: str)-> list:
    """
    Read all lines from a file into a list.

    Params:
        file_path(str): Path to the file.

    Returns:
        list[str]: List of lines (including newline characters).
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        return list(rawtext)

def _string_from_file(file_path: str | Path)-> str:
    """
    Read entire file contents as a single string.

    Params:
        file_path(str): Path to the file.

    Returns:
        str: Full file contents.
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        return rawtext.read()

def read_from_file(file_path: str | Path, read_mode: str):
    """
    Reads a file, read_from_file either yields a list, reads the entire contents to a single string, or reads the contents to a list of lines.

    Params:
        file_path(str): Path to the file to read from.
        read_mode(str): How the file is to be read. 
            Accepted: "String", "List", "Yield", "string", "list", "yield, 'S', 'L', 'Y', 's', 'l', 'y' 

    Raises:    
        UnsupportedFormatError(format; AcceptedFormats)
    """

    from_file = {
        "s": _string_from_file,
        "l": _list_from_file,
        "y": _yield_from_file
    }

    read_mode = read_mode[0].lower()
    if read_mode in from_file:
        from_file[read_mode](file_path)
