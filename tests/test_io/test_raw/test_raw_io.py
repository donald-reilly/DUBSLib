from dubslib.io import read_from_file, write_to_file
from dubslib.io.exceptions import UnsupportedReadModeError
import pytest

from types import GeneratorType

save_dir = "/home/donald-reilly/Documents/DubsWorkspace/SourceCode/python/DUBSLib/tests/test_io/test_raw/savedir"

read_dir = "/home/donald-reilly/Documents/DubsWorkspace/SourceCode/python/DUBSLib/tests/test_io/test_raw/readdir"

file_1 = f"{read_dir}/whocares.py"
file_2 = f"{read_dir}/pathandwithopen.md"


tests = {
    "returns_pass": {
        "paths": (
            file_1,
            file_2
        ),
        "read_modes": (
            ("String", "string", "S", "s"),
            ("List", "list", "L", "l"),
            ("Yield", "yield", "Y", "y"),
            (str, int, GeneratorType, list),
            ("somethign", "Yellow", "letter"),
        ),
        "expected": (
            str,
            list,
            GeneratorType,
            UnsupportedReadModeError,
            UnsupportedReadModeError
        ),
        "test_type": (
            "pass",
            "pass",
            "pass",
            "raises",
            "raises"
        )
    }
}

test1 = tests["returns_pass"]

def create_params(paths, read_modes, expected, test_type):
    parameters = []
    for path in paths:
        for index in range(0, len(read_modes)):
            for variant in read_modes[index]:
                test = (path, variant, expected[index], test_type[index])
                parameters.append(test)
    return parameters

@pytest.mark.parametrize(
        "file_path, read_mode, expected, test_type",
        create_params(test1["paths"], test1["read_modes"], test1["expected"], test1["test_type"])
)
def test_read_from_file_read_mode(file_path, read_mode, expected, test_type):

    if test_type == "pass":
        read_file = read_from_file(file_path, read_mode)
        assert type(read_file) == expected
    elif test_type == "raises":
        with pytest.raises(expected):
            read_file = read_from_file(file_path, read_mode)
 
