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

import json
from pathlib import Path
from dubslib.io.exceptions import UnsupportedFormatError

# WORK [ ]: Module doc string.
class Persistence:
    """
    Provides a unified entry point for data structure Input and output.
    
    Persistence provides an ergonomic API file input and output.
    """
    def __init__(self):

        self._loaders = {
            "json":(json, json.load)
            }

        self._dumpers = {
            "json": (json.dump, {"indent": 4, "default": str})
            }

    def to_file(self, pydict: dict, file_path: (Path | str), format: str):
        """
        Write the provided dictionary to file, using the chosen format.

        Params:
            pydict(dict): The python dictionary to be saved to file.
            file_path(str | Path): Path to file.
            format(str): Format for saved dictionary if None default is used.

        Raises:
            UnsupportedFormatError(format; AcceptedFormats)
        """

        if format not in self._dumpers:
            raise UnsupportedFormatError(format, self._loaders.keys())
        else:

            with open(file_path, 'w', encoding="utf-8") as dict_file:
                self._dumpers[format][0](pydict, dict_file, **self._dumpers[format][1])

    def from_file(self, file_path, format):
        """
        Reads a data set from file and returns a dictionary.

        Params:
            file_path(str | path): Path to a file.
            format: The format of the saved file.

        Raises:
            UnsupportedFormatError: If format not Supported
        """

        if format not in self._loaders:
            raise UnsupportedFormatError(format, self._loaders.keys())
        else:
            with open(file_path, 'r', encoding="utf-8") as config_file:
                return self._loaders[format](config_file)

