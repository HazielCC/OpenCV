def get_directory_used():
    """
    Get the current directory of the file.
    :return: str
    """
    import os

    current_path = os.path.abspath(
        __file__
    )  # Get the absolute path of the current file
    current_directory = os.path.dirname(
        current_path
    )  # Get the directory of the current file
    return current_directory


print(get_directory_used())
