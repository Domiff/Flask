import unittest
from datetime import date as dt

from second_module.financial_accounting import (app, storage, info_spending_money_in_year,
                                                info_spending_money_in_year_and_month,
                                                info_spending_money)


class TestFinanceAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.add_url = "/add/"
        cls.calculate_url = "/calculate/"

    def test_info_spending_money(self):
        date = "2025-2-3"
        money = 2000

        response = self.client.get(self.add_url + date + "/" + str(money))
        year, month, day = date.split("-")
        expected_massage = f"Траты за текущий день {dt(int(year), int(month), int(day))} составляют {money}"

        self.assertEqual(response.data.decode(), expected_massage)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(storage[year][month][day], money)

    def test_info_spending_money_in_year(self):
        year = "2025"

        response = self.client.get(self.calculate_url + year)
        result = 0

        list_money = list((sum(elem.values()) for elem in storage[year].values()))

        for elem in list_money:
            result += elem

        expected_massage = f"Траты за указанный год: {result}"

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), expected_massage)

    def test_info_spending_money_in_year_and_month(self):
        year, month = "2025", "2"

        response = self.client.get(self.calculate_url + year + "/" + month)

        list_money = list((sum(elem.values()) for elem in storage[year].values()))
        sum_money_in_year = 0
        sum_money_in_month = sum(storage[year][month].values())

        for elem in list_money:
            sum_money_in_year += elem

        expected_massage = (f"Траты за указанный год: {sum_money_in_year} \n "
                            f"Траты за указанный месяц составляют {sum_money_in_month}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), expected_massage)


if __name__ == '__main__':
    unittest.main()
