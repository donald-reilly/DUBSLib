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

class SerializationError(Exception):
    """
    Base exception for all serialization errors.
    """

    pass

class UnsupportedFormatError(SerializationError):
    
    def __init__(self, format, supported_formats):
        """
        Unsupported serialization format.
    
        Params:
            format(module): The intended format of the serialized data.
            supported_formats(list[module]): A list of the supported formats.    
        """
        self.format = format

        self.supported_formats = tuple(supported_formats)

        error_message = (f"Unexpected format: {format!r} ." 
                         f"Expected one of; {', '.join(supported_formats)}")
        super().__init__(error_message)

class UnsupportedReadModeError(SerializationError):

    def __init__(self, read_mode, supported_modes):
        """
        Unsupported serialization format.
    
        Params:
            read_mode(str): The read mode requested.
            supported_modes(list[strings]): A list of the supported modes.    
        """

        self.supported_modes = tuple(supported_modes)

        error_message = (f"Unexpected Read Mode: {read_mode!r} ." 
                         f"Expected one of; {', '.join(supported_modes)}")
        super().__init__(error_message)
