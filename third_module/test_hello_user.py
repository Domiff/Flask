from freezegun import freeze_time
import unittest

from second_module import hello_user


class TestSecondModule(unittest.TestCase):

    def setUp(self):
        self.name = 'Gintoki'

    @freeze_time('2025-1-20')
    def test_correct_monday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошего понедельника!")

    @freeze_time('2025-1-21')
    def test_correct_tuesday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошего вторника!")

    @freeze_time('2025-1-22')
    def test_correct_wednesday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошей среды!")

    @freeze_time('2025-1-23')
    def test_correct_thursday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошего четверга!")

    @freeze_time('2025-1-24')
    def test_correct_friday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошей пятницы!")

    @freeze_time('2025-1-25')
    def test_correct_saturday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошей субботы!")

    @freeze_time('2025-1-26')
    def test_correct_sunday(self):
        self.assertEqual(hello_user.hello_world(self.name), "Привет, Gintoki. Хорошего воскресенья!")

    def tearDown(self):
        del self.name


if __name__ == '__main__':
    unittest.main()