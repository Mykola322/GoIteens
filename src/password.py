import string


def is_verify_password(password: str) ->bool:
    if len(password) >= 8:
            is_len_pass = True
    else:
                is_len_pass = False

    is_have_digit = False
    is_have_char = False

    for char in password:
        if char.isalpha():
            is_have_char = True
        elif char.isdigit():
            is_have_digit = True

    if is_len_pass and is_have_digit and is_have_char:
        return True
    else:
         return False

def password() -> str:
    while True:
        command = input("Створіть пароль для можливості працювати в системі.\n"
                        "Введіть 1 для введення придуманого вами паролю\n->")
        if command == "1":
            password = input("Введіть пароль\n"
                            "**ВАЖЛИВО** |\n"
                            "____________V________________________________________________________________________________\n"
                            "пароль має містити хочаб 1 цифру та 1 літеру також пароль має містити не менш ніж 8 символів.\n Введіть пароль-> ")

            is_verify_password(password)

            return password
        else:
                input("Пароль не відповідає вимогам. Натисніть 'Enter' для повторної спроби ")