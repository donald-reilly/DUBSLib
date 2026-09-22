# This file is part of dubslib
# Copyright (C) 2026 Donald Raymond Reilly Jr.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path
from dubslib.io.exceptions import UnsupportedReadModeError

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
    supported_modes = (
        "String", "List", "Yield",
        "string", "list", "yield",
        'S', 'L', 'Y',
        's', 'l', 'y'
    )
    from_file = {
        "s": _string_from_file,
        "l": _list_from_file,
        "y": _yield_from_file
    }

    if read_mode in supported_modes:
        rm = read_mode[0].lower()
        return from_file[rm](file_path)
    else:
        raise UnsupportedReadModeError(read_mode, supported_modes)
