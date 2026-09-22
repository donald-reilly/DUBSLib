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

from dubslib.io import read_from_file, write_to_file
from dubslib.io.exceptions import UnsupportedReadModeError

import pytest

from types import GeneratorType

save_dir = "/home/donald-reilly/Documents/DubsWorkspace/SourceCode/python/DUBSLib/tests/test_io/test_raw/savedir"

read_dir = "/home/donald-reilly/Documents/DubsWorkspace/SourceCode/python/DUBSLib/tests/test_io/test_raw/readdir"
poem = {
    "string": """Ah!— Oh, ain't it grand
To live and breathe
And let your chest expand
Morning Cab!
[Calloway]
Good Morning Al! Ah!—

The skies are blue, the world's a song
When life is notes to you
I've got eternal youth because
I've got my heart where it belongs
Don't care who makes the nation's laws
Long as I can sing its songs;

I love to sing-a
About the moon-a and the June-a and the spring-a
I love to sing-a
'Bout a sky of blue-a, or a tea for two-a
Anything-a with a swing-a to an I love you-a
I love-a to, I love-a to sing

Give me a song-a
About a son-a-gun, who went and done her wrong-a
But keep it clean-a;
With a cottage small-a by a waterfall-a
Any sob-a that'll throb-a to a bluebird's call-a
I love-a to, I love-a to sing""",
    "list": [
        "Ah!— Oh, ain't it grand\n",
        "To live and breathe\n",
        "And let your chest expand\n",
        "Morning Cab!\n",
        "[Calloway]\n",
        "Good Morning Al! Ah!—\n",
        "\n",
        "The skies are blue, the world's a song\n",
        "When life is notes to you\n",
        "I've got eternal youth because\n",
        "I've got my heart where it belongs\n",
        "Don't care who makes the nation's laws\n",
        "Long as I can sing its songs;\n",
        "\n",
        "I love to sing-a\n",
        "About the moon-a and the June-a and the spring-a\n",
        "I love to sing-a\n",
        "\'Bout a sky of blue-a, or a tea for two-a\n",
        "Anything-a with a swing-a to an I love you-a\n",
        "I love-a to, I love-a to sing\n",
        "\n",
        "Give me a song-a\n",
        "About a son-a-gun, who went and done her wrong-a\n",
        "But keep it clean-a;\n",
        "With a cottage small-a by a waterfall-a\n",
        "Any sob-a that'll throb-a to a bluebird's call-a\n",
        "I love-a to, I love-a to sing"
    ]
}

file_1 = f"{read_dir}/whocares.py"
file_2 = f"{read_dir}/pathandwithopen.md"
file_3 = f"{read_dir}/mock_text.txt"

tests = {
    "return_types": {
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
    },
    "content": {
        "paths": (
            file_3,
        ),
        "read_modes": (
            ("String", "string", "S", "s"),
            ("List", "list", "L", "l")
        ),
        "expected": (
            poem["string"],
            poem["list"]
        ),
        "test_type": (
            "pass",
            "pass"
        )
    }

}

test1 = tests["return_types"]
test2 = tests["content"]
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

@pytest.mark.parametrize(
        "file_path, read_mode, expected, test_type",
        create_params(test2["paths"], test2["read_modes"], test2["expected"], test2["test_type"])
)
def test_read_from_file_content(file_path, read_mode, expected, test_type):

    read_file = read_from_file(file_path, read_mode)

    assert read_file == expected

if __name__ == "__main__":
    
    create_params(test2["paths"], test2["read_modes"], test2["expected"], test2["test_type"])
