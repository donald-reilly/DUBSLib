import json
from pathlib import Path
from ..exceptions.serializationerror import *
# WORK [ ]: Module doc string.
class Persistence:
    """
    Provides a unified entry point for data structure Input and output.\
    
    Persistence provides two generalized functions for data structure input and output, using a mapping this allows for \"configuraitons\" to be preloaded, registered and possibly even read from file if the use and need grows.
    """
    def __init__(self):

        self._loaders = {
            "json":(json, json.load)
            }

        self._dumpers = {
            "json": (json, json.dump, {"indent": 4, "default": str})
            }

    def to_file(self, pydict: dict, file_path: (Path | str), format: str):
        """
        Write the provided dictionary to file, using the chosen format.

        Params:
            pydict(dict): The python dictionary to be saved to file.
            file_path(str | path): Path to file.
            format(str): Format for saved dictionary if None default is used.

        Raises:
            UnsupportedFormatError(format; AcceptedFormats)
        """

        if format not in self._dumpers:
            raise UnsupportedFormatError(format, self._loaders.keys())
        else:
            with open(file_path, 'w', encoding="utf-8") as dict_file:
                self._dumpers[format][0](pydict, dict_file, **self._dumpers[format][2])

    def from_file(self, file_path, format):
        """
        Reads a data set from file and returns a dictionary.

        Params:
            file_path(str | path): Path to a file.
            format: The format the the saved file.

        Raises:
            UnsupportedFormatError: If format not Supported
        """

        if format not in self._loaders:
            raise UnsupportedFormatError(format, self._loaders.keys())
        else:
            with open(file_path, 'r', encoding="utf-8") as config_file:
                return self._loaders[format](config_file)
