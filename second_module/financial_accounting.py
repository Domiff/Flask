import sys
from datetime import date as dt

from flask import Flask


app = Flask(__name__)

storage = dict()

@app.route('/add/<date>/<int:number>')
def info_spending_money(date: str, number: int):
    year, month, day = date.split('-')
    current_date = dt(int(year), int(month), int(day))
    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number

    return f"Траты за текущий день {current_date} составляют {storage[year][month][day]}"


@app.route('/calculate/<int:year>')
def info_spending_money_in_year(year):
    new_year = str(year)

    spent_money_in_year = list((sum(elem.values()) for elem in storage[new_year].values()))
    result = 0

    for elem in spent_money_in_year:
        result += elem

    return f"Траты за указанный год: {result}"

@app.route('/calculate/<int:year>/<int:month>')
def info_spending_money_in_year_and_month(year, month):
    new_year, new_month = str(year), str(month)
    spent_money_in_month = sum(storage[new_year][new_month].values())
    spent_money_in_year = list((sum(elem.values()) for elem in storage[new_year].values()))
    result = 0

    for elem in spent_money_in_year:
        result += elem

    return f"Траты за указанный год: {result} \n Траты за указанный месяц составляют {spent_money_in_month}"


if __name__ == '__main__':
    app.run(debug=True)
