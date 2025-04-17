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
