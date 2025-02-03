from datetime import date


class Person:
    def __init__(self, name: str, year_of_birth: str, address=None):
        self.name = name
        self.year_of_birth = year_of_birth
        self.address = address

    def get_age(self):
        now = date.today()
        year, month, day = self.year_of_birth.split('-')
        self.year_of_birth = date(int(year), int(month), int(day))
        age = now.year - self.year_of_birth.year

        if (self.year_of_birth.month, self.year_of_birth.day) > (now.month, now.day):
            age -= 1
        return age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
        """returns True if address is not set, false in other case"""
        return self.address is None


if __name__ == '__main__':
    person = Person("name", "2005-12-2", "Ikebokura, 33")
    print(person.get_age())
