class Person:
    def __init__(self, name, age, mail, phone_number):
        self._name = name
        self._age = age
        self._mail = mail
        self._phone_number = phone_number

    def __repr__(self):
        return (f"Person(id = '{self._name}', age = {self._age}, mail = '{self._mail}', "
                f"phone_number = {self._phone_number})")

    def get_age(self):
        return self._age
