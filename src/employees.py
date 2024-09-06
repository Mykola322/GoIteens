from datetime import datetime


def add_employee(employees: dict) -> dict:
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
            }
    print("Користувача успішно додано!")
    return employees


def del_employees(employees: dict) -> dict:
    login = input("Ввудіть логін користувача для видалення: ")

    if login in employees:
        del employees[login]
        print(f"Користувача '{login}' успішно видалено!")
    else:
        print("Такого користувача не знайдено. Спробуйте ше раз!")

    return employees


def change_salary(employees: dict) -> dict:
    login = input("Введіть логін користувача: ")

    if login in employees:
        salary = input("Введіть нову суму ЗП: ")
        employees[login]["salary"] = salary
        print("Зарплату успішно змінено!")
    else:
        print("Такого користувача не знайдено! Спробуйте ще раз")

    return employees


def change_position(employees: dict) -> dict:
    login = input("Введіть логін працівника: ")

    if login in employees:
        position = input("Введіть нову посаду: ")
        employees[login]["position"] = position
        input("Посаду користувача успішно змінено!")
    else:
        input("Такого користувача не знайдено!")

    return employees
