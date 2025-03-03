# Archivos de Proyecto
import os

from rich import print

CURRENT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def set_db_root(db_name):
    return os.path.join(CURRENT_DIRECTORY, "db", db_name)


if __name__ == "__main__":
    print(CURRENT_DIRECTORY)
    print(set_db_root("ProjectDB.db"))
