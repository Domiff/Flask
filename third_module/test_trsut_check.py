import unittest

from trust_check import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("name", "2005-12-2", "Ikebokura, 33")

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), 19, msg="Ожидался другой возраст")

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "name", msg="Ожидалось другое имя")

    def test_set_name(self):
        self.new_name = "name2"
        self.person.set_name(self.new_name)
        self.assertEqual(self.person.name, self.new_name, msg="Ожидалось другое имя")

    def test_set_address(self):
        self.new_address = "Osaka, 78"
        self.person.set_address(self.new_address)
        self.assertEqual(self.person.address, self.new_address, msg="Ожидался другой адрес")

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), "Ikebokura, 33", msg="Ожидался другой адрес")

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())
        

if __name__ == "__main__":
    unittest.main()