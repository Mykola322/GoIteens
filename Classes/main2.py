class Dodge:
    def __init__(self):
        self.dodge = "Public attribute"
        self._fuel = "72L"
        self.__range = "500Km"

    def change_range(self, new_range):
        print(f"Print private range: {self.__range = }")
        self.__range = new_range
        print(f"Print private range: {self.__range = }")
        print("This is a public method")

    def _protected_method(self):
        print("This is a protected method")

    def __private_method(self):
        print("This is a private method")

    def start(self):
        self._protected_method()

print("ніц")



dodge = Dodge()
dodge.change_range(new_range=768)
dodge._protected_method()
dodge.__private_method()
