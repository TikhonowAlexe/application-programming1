import unittest
from freezegun import freeze_time
import datetime

def get_username(greeting):
    weekday = datetime.datetime.now().strftime('%A')
    return f'{greeting} {weekday}'

class GreetingTest(unittest.TestCase):

    @freeze_time("2025-04-14")  # Понедельник
    def test_correct_weekday_in_username(self):
        expected = "Хорошего дня Monday"
        result = get_username("Хорошего дня")
        self.assertEqual(result, expected)

    @freeze_time("2025-04-16")  # Среда
    def test_custom_input_username_contains_weekday(self):
        username = "Хорошей среды"
        weekday = datetime.datetime.now().strftime("%A")
        self.assertIn(weekday, get_username(username))

if __name__ == '__main__':
    unittest.main()
