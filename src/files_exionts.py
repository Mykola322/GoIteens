import os

from files import list_files


if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8"):
        pass


if not os.path.exists(list_files.ANIMALS_CURED):
    with open(list_files.ANIMALS_CURED, "w", encoding="utf-8"):
        pass


def open_animals(path: str = list_files.ANIMALS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        animals = file.readlines()

    return animals


def open_animals_cured(path: str = list_files.ANIMALS_CURED)-> list:
    with open(path, "r", encoding="utf-8") as file:
        animals_cured = file.readlines()

    return animals_cured