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

from dubslib.io.exceptions import UnsupportedFormatError
from pathlib import Path

def _write_string_to_file(file_path: str, content: str):
    """
    Overwrite a file with a string.

    Params:
        file_path(str): Path to the file.
        content(str): Text to write.
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def _write_lines_to_file(file_path: str, lines: list[str]):
    """
    Overwrite a file with a sequence of lines.

    Params:
        file_path(str): Path to the file.
        lines (Iterable[str]): Lines to write (must include newline characters if desired).
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def _append_string_to_file(file_path: str, content: str):
    """
    Append a string to the end of a file.

    Params:
        file_path(str): Path to the file.
        content(str): Text to append.
    """

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)

def _append_lines_to_file(file_path: str, lines: list[str]):
    """
    Append multiple lines to the end of a file.

    Params:
        file_path(str): Path to the file.
        lines(Iterable[str]): Lines to append (must include newline characters if desired).
    """

    with open(file_path, "a", encoding="utf-8") as f:
        f.writelines(lines)

def write_to_file(file_path: str| Path,
                  content: str | list[str],
                  write_mode: str
                  ):
    """
    Writes/appends contents of a list or string to the specified file. The 
    write type is not assumed and must be provided. 

    Params:
        file_path(str): Path to the file to overwrite, create or append to.
        content(str): String or list of strings to write to file.
        write_mode(str): How to write the file. 
            Accepted: "Write", "Appened", "write", "appened", 'w', 'a', 'W', 'A'

    Raises:    
        UnsupportedFormatError(format, AcceptedFormats)
    """

    if not isinstance(content, str, list):
        raise TypeError(f"Content is of type: {type(content)}. Must be of type str or list")
    supported_modes = (
        "Write", "Appened",
        "write", "appened",
        'W', 'A',
        'w', 'a'
    )
    to_file = {
        "w": {
            str: _write_string_to_file,
            list: _write_lines_to_file
        },
        "a": {
            str: _append_string_to_file,
            list: _append_lines_to_file
        }
    }

    if write_mode in supported_modes:
        mode = write_mode[0].lower()
        to_file[mode][type(content)](file_path, content)
    else:
        raise UnsupportedFormatError(write_mode, supported_modes)
