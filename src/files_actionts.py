import os

from files import list_files


if not os.path.exists(list_files.ANIMALS):
    with open(list_files.ANIMALS, "w", encoding="utf-8"):
        pass


if not os.path.exists(list_files.ANIMALS_CURED):
    with open(list_files.ANIMALS_CURED, "w", encoding="utf-8"):
        pass

if not os.path.exists(list_files.EMPLOYEES):
    with open(list_files.EMPLOYEES, "w", encoding="utf-8") as file:
        json.dump({}, file)

if not os.path.exists(list_files.LOG):
    with open(list_files.LOG, "w", encoding="utf-8") as file:
        json.dump([], file)

if not os.path.exists(list_files.USING_COMMANDS):
    with open(list_files.USING_COMMANDS, "w", encoding="utf-8") as file:
        json.dump({}, file)


def open_animals(path: str = list_files.ANIMALS) -> list:
    with open(path, "r", encoding="utf-8") as file:
        animals = file.readlines()

    animals = [animal.strip() for animal in animals]
    return animals


def save_animals(animals: list, path: str = list_files.ANIMALS) -> None:
    animals = [f"{animal}\n" for animal in animals]
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(animals)




def open_animals_cured(path: str = list_files.ANIMALS_CURED)-> list:
    with open(path, "r", encoding="utf-8") as file:
        animals_cured = file.readlines()
        animals = file.readlines()
        animals = [animal.strip() for animal in animals]

    return animals_cured

def save_animals_cured(animals_cured: list, path: str = list_files.ANIMALS_CURED) -> str:
    animals_cured = [f"{animals_cured}\n" for animals_cured in animals_cured]
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(animals_cured)

def open_employees(path: str = list_files.EMPLOYEES) -> dict[dict]:
    with open(path, "r" encoding="utf-8") as file:
        employees = json.load(file)

    return employees

def save_employees(employees: dict[dict], path: str = list_files.EMPLOYEES)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(employees, ensure_ascii=False, indent=4)