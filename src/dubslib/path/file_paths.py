from pathlib import Path
from importlib.metadata import metadata
from time import strftime

# TEST [ ]
def add_date_time(string, month = False, day = False, year = False, 
                  hour = False, minute = False, extension = None):
    """
    Create string with an specified time/date stamp.
    """
    # NOTES: I think a decent fix is definitely gonna be to wrap functions with a too lower 
    accepted_extensions = {
        ".md": ".md",
        "md": ".md",
        "markdown": ".md",
        "MarkDown": ".md",
        "Markdown": ".md",
        ".py": ".py",
        "py": ".py",
        "python": ".py",
        "Python": ".py",
        ".json": ".json",
        "json": ".json",
        "Json": ".json",
        "JSON": ".json",
    }
    file_parts = [
        string,
        strftime("%m") if month else None,
        strftime("%d") if day else None,
        strftime("%Y") if year else None,
        strftime("%H") if hour else None,
        strftime("%M") if minute else None
    ]
    file_name = "_".join(part for part in file_parts if part is not None)

    if extension in accepted_extensions:
        file_name += accepted_extensions[extension]

    return file_name
# TEST [ ]
def get_object_name(object_to_inspect):

    try:
        object_name = object_to_inspect.__name__
        return object_name

    except AttributeError:
        object_name = object_to_inspect.__class.__name__
        return object_name
# TEST [ ]
def _get_package_version(package_name):

    version = metadata(package_name)["version"]
    return version
# TEST [ ]
def _get_module_version(module):
    """
    This provides the version number of the imported package without blindly 
    importing the entire package, which would be the only way to find the 
    version number outside of this function.

    Params:
        module_name(str): The name of the imported module.
    
    Returns:
        The version of the package to which the imported module belongs.]
    """
    
    package_name = module.__module__.split(".")[0]

    version = _get_package_version(package_name)
    return version
# TEST [ ]
def add_version(package_name = None, module_name = None):
    """
    This is just a temp structure. It only works with installed packages which 
    may or may not be the case with user packages. So this is a placeholder. 
    Eventually I'll need to either enforce versioning, or versioning could be 
    setup when this is package is intiailized. Kind of like git init, how that 
    works. Someting like HereIsYou init. This creates a versioning system if 
    one doesnt' already exist, or goes off he current system if one is already 
    in place.
    """

    if package_name:
        version = _get_package_version(package_name)
        if type(package_name) == str:
            return package_name + "_" + "V." + version
        else:
            package_name = get_object_name(package_name)
            return package_name + "_" + "V." + version

    elif module_name:
        version = _get_module_version(module_name)
        if type(module_name) == str:
            return module_name + "_" + "V." + version
        else:    
            module_name = get_object_name(module_name)
            return module_name + "_" + "V." + version
# TEST [ ]
def search_path(file , search) -> tuple[Path, Path]:
    """
    Retrieves the project root path and the main file path based on the provided file path and depth.

    Params:
        file (str): the __file__ of the main script held in src/.
        depth (int): The depth of src, defaults to 3.

    Returns:
        tuple: A tuple containing the project root path and the main file path.
    """

    new_path = Path(file)
    for parent in new_path.parents:
        if parent.name == search:
            return parent
    else:
        raise ValueError(f"{search} is not in path")

# TEST [ ]
def ensure_path(path_obj: Path):
    """
    Ensures that the specified path exists. If it doesn't, the path is created.

    Params:
        path_obj (Path): The path to ensure.
        month_year_components (str): Provide optional args to append month or 
        year to file in order provided

    Example:
        ensure_path("./some_path", "year", "month") = "./some_path_2026_07
    Returns:
        bool: True if the path was created, False if it already existed.
    """

    if not path_obj.exists():
        path_obj.parent.mkdir(parents=True, exist_ok=True)
        return True
    else:
        raise OSError(f"Failed to create or access the path: {path_obj}")
