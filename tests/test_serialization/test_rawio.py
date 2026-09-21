from pathlib import Path

from serialization.raw.io import (
                                    from_file,
                                    write_to_file,
                                    append_to_file
                                    )

file = Path(__file__)
mock_dir = file.parents[1] / "mock_data"
mock = {
    "text_file": mock_dir / "mock_text.txt"
}

accepted_returns = {
    "yield": "generator",
    "list": list,
    "string": str
}
def test_from_file(file_path):

    for return_type, expected in accepted_returns.items():
        
        actual = from_file(file_path, return_type)

        try:
            assert type(actual) == expected
            print(f"TEST PASSED: Input: {file_path}, {return_type} Results: {actual} Expected: {expected} ")
        except:
            print(f"Expected: {expected} actual return type was {actual}")    
if __name__ == "__main__":

    test_from_file(mock["text_file"])
    
