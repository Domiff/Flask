import unittest

from add_validator import app


class TestRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        cls.client = app.test_client()
        cls.url = "/registration"

    def test_form(self):
        data = {"email": "fmleg@gmail.com",
                    "name": "Triss",
                    "phone": 9066790901}

        response = self.client.post(self.url, data=data)
        expected_message = ("Пользователь Triss зарегистрирован с электронной почтой fmleg@gmail.com "
                            "и номером телефоном 9066790901")

        self.assertEqual(response.status_code, 200)
        self.assertIn(expected_message, response.get_data(as_text=True))

    def test_empty_email_form(self):
        data = {"email": "",
                    "name": "Triss",
                    "phone": 9066790901}

        expected_message = "Bad request {'email': ['This field is required.']}"
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_message, response.get_data(as_text=True))

    def test_empty_name_form(self):
        data = {"email": "fmleg@gmail.com",
                    "name": "",
                    "phone": 9066790901}

        expected_message = "Bad request {'name': ['This field is required.']}"
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_message, response.get_data(as_text=True))

    def test_empty_phone_form(self):
        data = {"email": "fmleg@gmail.com",
                    "name": "Triss",
                    "phone": None}

        expected_message = "Bad request {'phone': ['This field is required.']}"
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_message, response.get_data(as_text=True))

    def test_invalid_email_form(self):
        data = {"email": "fmleggmail.com",
                "name": "Triss",
                "phone": 9066790109}

        expected_message = "Bad request {'email': ['Invalid email address.']}"
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_message, response.get_data(as_text=True))

    def test_invalid_phone_form(self):
        data = {"email": "fmleg@gmail.com",
                "name": "Triss",
                "phone": "r"}

        expected_message = "Bad request {'phone': ['Not a valid integer value.'"
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_message, response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
