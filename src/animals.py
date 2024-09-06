def show_all_animals(animals: list) -> None:
            for i, animal in enumerate(animals, start=1):
                print(f"{i}: {animal}")

            input("\nНатисніть 'enter' для продовження\n")


def add_animal(animals: list) -> list:
            animal = input("\nВведіть назву нової тваринки: ")
            if animal in animals:
                print("\nТаку тваринку вже було додано до списку\nНатисніть 'enter' для продовження\n")
            else:
                animals.append(animal)
                print("\nНова тваринка додана до списку\nНатисніть'enter'для продовження")
            return animals
                      # ANIMALS.remove(animal), ANIMALS_CURED.append(animal)


def cured_animal(animals: list) -> list:
            anim = input("\nВведіть список вилікуваних тваринок через пробіл:\n").split()
            animals_cured.extend(anim)
            print("\nСписок вилікуваних тваринок розширено")
            return animals
                                        # ANIMALS_CURED


def list_cured_animals(animals_cured: list) -> None:
        print("\nCписок проданих товарів\n")
        for i, animal in enumerate(animals_cured, start=4):
                print(f"{i}: {animal}")


def del_animal(animals: list) ->list:
            animal = input("Введіть назву помилково доданої тваринки для видалення: ")

            if animal in animals:
                animals.remove(animal)
                print(f"\nТваринка '{animal}' видалено зі списку")
            else:
                print(f"\nТваринка '{animal}' відсутній у списку")
            return animals


def del_animal_by_number(animals: list) -> list:
            number = input("Введіть номер тваринки для видалення: ")

            if number.isdigit() and 0 < int(number) <= len(animals):
                animal = animals.pop(int(number) - 1)
                print(f"\nТваринка'{animal}' видалено зі списку")
            else:
                print("\nВведено невірний номер\nНатисніть'enter'для продовження")
            return animals


def sort_animals_by_name(animals: list) -> list:
            anim = sorted (animals)
            for i, anim in enumerate(anim, start=1):
                print(f"{i}: {anim}")
            print("\nСписок тваринок успішно відсортовано")


                                        # Видалити та вставити на її місце іншу (ANIMALS.insert(0, animal))
    ######################################################################################


def change_animal_name(animals)->list:
            old_animal = input("Введіть назву тваринки якій хочете замінити ім'я: ")
            new_animal = input("Введіть нову назву тваринки: ")

            if old_animal in animals:
                index = animals.index(old_animal)
                animals.pop(index)
                animals.insert(index, new_animal)
                input("\nІм'я тваринки успішно замінено")
            else:
                input(f"\nТваринка '{old_animal}' відсутня у цьому списку")


def search_animal_by_name(animals: list)-> list:
            animal = input("Введіть назву тваринки для пошуку: ")
            if animal in animals:
                index = animals.index(animal)
                print(f"\nТваринка'{animal}' знаходится під номером'{index + 1}'")
            else:
                print(f"\nТваринка '{animal}' відсутня у цьому списку")

            return None
