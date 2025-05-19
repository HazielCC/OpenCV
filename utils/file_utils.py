import os

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


def get_asset_path():
    """
    Obtiene la ruta de la carpeta assets, buscando una carpeta arriba.
    :return: str
    """

    current_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(os.path.dirname(current_path))  # Sube un nivel
    asset_path = os.path.join(parent_directory, "assets")
    if not os.path.exists(asset_path):
        raise FileNotFoundError(f"Assets directory not found at {asset_path}")

    return asset_path
print(get_directory_used())
print(get_asset_path())
