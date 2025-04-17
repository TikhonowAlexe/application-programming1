# app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays = ['понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья']

@app.route('/hello-world/<name>')
def hello(name):
    weekday = weekdays[datetime.today().weekday()]
    return f'Привет, {name}. Хорошей {weekday}!'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    try:
        nums = [int(n) for n in numbers.split('/') if n.isdigit()]
        if nums:
            return f'Максимальное число: {max(nums)}'
        return 'Ошибка: числа не найдены'
    except ValueError:
        return 'Ошибка: переданы нечисловые значения'

import os

@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)
    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            result_text = f.read(size)
        return f"<b>{abs_path}</b> {len(result_text)}<br>{result_text}"
    except Exception as e:
        return f'Ошибка: {e}'

expenses = {}

@app.route('/add/<date>/<int:number>')
def add(date, number):
    year = int(date[:4])
    month = int(date[4:6])
    expenses.setdefault(year, {}).setdefault(month, 0)
    expenses[year][month] += number
    return f'Добавлено: {number} рублей за {date}'

@app.route('/calculate/<int:year>')
@app.route('/calculate/<int:year>/<int:month>')
def calculate(year, month=None):
    if year not in expenses:
        return 'Нет данных'
    if month:
        return str(expenses[year].get(month, 0))
    return str(sum(expenses[year].values()))
