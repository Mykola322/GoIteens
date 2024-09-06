from pprint import pprint
from datetime import datetime
from src.animals import (
    show_all_animals,
    add_animal,
    cured_animal,
    list_cured_animals,
    del_animal,
    del_animal_by_number,
    sort_animals_by_name,
    change_animal_name,
    search_animal_by_name,
)
from src.employees import (
    add_employee,
    del_employees,
    change_salary,
    change_position,
)
from files.list_files import HELP
from src import files_exionts


DELIMITER = "-" *28
TEMPLATE = "|{:<5}|{:<20}|"


def exit():
    print("\nВи успішно вийшли з програми. До зустрічі!\n")
    quit()


def help(path: str = HELP) -> None:
    with open(path, "r", encoding="utf-8") as file:
        print(file.read())


def main():
    employees = {
        "Andrew": {
        "position": "Менеджер",
        "salary": 30000,
        "start_date": "22.02.2024",
        "name": "Андрій",
        "password": "1234567a"
    },
    "Dima": {
        "position": "Продавець",
        "salary": "14000",
        "start_date":"30.03.2024",
        "name": "Дмитро",
        "password": "1234567b"
    }
}

    animals = files_exionts.open_animals()

    animals_cured = files_exionts.open_animals_cured()

    log = []
    using_commands = {}

    login = input("Введіть свій логін користувача: ")
    password = employees.get(login, {}).get("password")

    if not password:
        login = input("Введіть особистий логін: ")
        position = input("Введіть свою посаду: ")
        salary = input("Введіть свою зарплату: ")
        name = input("Введіть своє ім'я: ")
        start_date = datetime.now().strftime("%d.%m.%Y")

        employees[login] = {
                "position": position,
                "salary": salary,
                "start_date": start_date,
                "name": name,
                "password": password
            }

        employees[login]["password"] = password

    else:
        input(f"\nПароль успішно створено: '{password}'. Запам'ятайте його! 'enter' для продовження")

    password_input = input("\nВведіть пароль: ")

    command = ""
    while password_input == password:
        if not command:
            log.append(f"Користувач з логіном '{login}' ввійшов у систему: {datetime.now()}")
            print("Вітаємо в нашій інформаційній системі!")

        command = input("\nВведіть команду aбо 'help' для списку доступних команд: ")
        log.append(f"Користувач з логіном '{login}' ввів команду '{command}': {datetime.now()}")
        using_commands[command] = using_commands.get(command, 0) + 1

        match command:
            case "show_all_animals":
                show_all_animals(animals)
            case "add_animal":
                add_animal(animals)
            case "cured_animal":
                cured_animal(animals)
            case "list_cured_animals":
                list_cured_animals(animals)
            case "exit":
                exit()
            case "del_animal":
                del_animal(animals)
            case "del_animal_by_number":
                del_animal_by_number(animals)
            case "sort_animals_by_name":
                sort_animals_by_name(animals)
            case "change_animal_name":
                change_animal_name(animals)
            case "search_animal_by_name":
                search_animal_by_name(animals)
            case "add_employee":
                add_employee(employees)
            case "del_employees":
                del_employees(employees)
            case "change_salary":
                change_salary(employees)
            case "change_position":
                change_position(employees)
            case "help":
                help()
            case _:
                print("Невідома команда напишіть 'help' для списку доступних команд")

    else:
        print("пароль не вірний. Доступ не надано")


if __name__ == "__main__":
     main()

