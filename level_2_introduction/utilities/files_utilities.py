# Archivos de Proyecto
import os

CURRENT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

DB_FILE = os.path.join(CURRENT_DIRECTORY, "db")


def set_folder_root(folder):
    return os.path.join(CURRENT_DIRECTORY, folder)


if __name__ == "__main__":
    print(CURRENT_DIRECTORY)
    print(DB_FILE)
