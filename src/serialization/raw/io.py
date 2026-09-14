from exceptions.serializationerror import *

def raw_from_file(file_path: str, format: str):
    """
    Provides the data within a file, dependent on the provided format. 
    Defaults to utf-8 encoding.

    Params:
        file_path(str): Path to the file.

    Yields:
        str: Each line in the file (including newline characters).
    
    Returns:
        list[str]: A list of strings, each entry representing a line from the file.

    Returns:
        str: The file contained within one string.

    Raises:    
        UnsupportedFormatError(format; AcceptedFormats)
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        if format == "Yield":
            yield from rawtext
        elif format =="list":
            return list(rawtext)
        elif format == "string":
            return rawtext.read()
        else:
            raise UnsupportedFormatError(format, ("Yield", "list", "string"))

def write_to_file(file_path: str, content: str | list[str]):
    """
    Overwrite a file with a single str or a list of strings
    
    Params:
        file_path(str): Path to the file to overwrite or create.
        content(str): String or list of strings to write to file.

    Raises:    
        UnsupportedFormatError(format; AcceptedFormats)
    """

    with open(file_path, "w", encoding="utf-8") as f:
        if type(content) == str:
            f.write(content)
        elif type(content) == list:
            f.writelines(content)
        else:
            raise UnsupportedFormatError(format, ("str", "list"))

def append_to_file(file_path: str, content: str | list[str]):
    """
    Append either a single str or a list of strings to the end of a file.

    Params:
        file_path(str): Path to the file to be appended.
        content(str): String or list of strings to append to file.

    Raises:    
        UnsupportedFormatError(format; AcceptedFormats)
    """

    with open(file_path, "a", encoding="utf-8") as f:
        if type(content) == str:
            f.write(content)
        elif type(content) == list:
            f.writelines(content)
        else:
            raise UnsupportedFormatError(format, ("str", "list"))

# Archive        
def yield_from_file(file_path: str):
    """
    Yeild lines from the provided file. Defaults to utf-8 encoding.

    Params:
        file_path(str): Path to the file.

    Yields:
        str: Each line in the file (including newline characters).
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        yield from rawtext
# Archive
def list_from_file(file_path: str)-> list:
    """
    Read all lines from a file into a list.

    Params:
        file_path(str): Path to the file.

    Returns:
        list[str]: List of lines (including newline characters).
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        return list(rawtext)
# Archive
def string_from_file(file_path: str)-> str:
    """
    Read entire file contents as a single string.

    Params:
        file_path(str): Path to the file.

    Returns:
        str: Full file contents.
    """

    with open(file_path, mode="r", encoding="utf-8") as rawtext:
        return rawtext.read()
# Archive
def write_string_to_file(file_path: str, content: str):
    """
    Overwrite a file with a string.

    Params:
        file_path(str): Path to the file.
        content(str): Text to write.
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
# Archive
def write_lines_to_file(file_path: str, lines: list[str]):
    """
    Overwrite a file with a sequence of lines.

    Params:
        file_path(str): Path to the file.
        lines (Iterable[str]): Lines to write (must include newline characters if desired).
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
# Archive
def append_string_to_file(file_path: str, content: str):
    """
    Append a string to the end of a file.

    Params:
        file_path(str): Path to the file.
        content(str): Text to append.
    """

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)
# Archive
def append_lines_to_file(file_path: str, lines: list[str]):
    """
    Append multiple lines to the end of a file.

    Params:
        file_path(str): Path to the file.
        lines(Iterable[str]): Lines to append (must include newline characters if desired).
    """

    with open(file_path, "a", encoding="utf-8") as f:
        f.writelines(lines)
