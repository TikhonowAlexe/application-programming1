from flask import Flask
import random
import datetime
import os

#Создаем экземпляр веб-приложения Фласк. (__name__) указывает, что этот файл - точка входа
app = Flask(__name__)

#список машин, который будет использоваться в /cars
cars = ['Jeep', 'BMW', 'Ford', 'Lamba']
#Список кошек, который будет использоваться в /сатs
cat_breeds = ['мейн-кун', 'шотландская', 'мейн-кун', 'сфинкс']

#Абсолютный путь к директории
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#Объединяем путь к папке и имя файла, получая полный путь к war_and_peace.txt
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

#Открывает файл книги, переводим в нижний регист, и разбиваем по пробелам, создавая список слов
with open(BOOK_FILE, encoding='utf-8') as f:
    book_words = f.read().lower().split()

#Создаем маршрут и возвращаем машины из списка
@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'


@app.route('/cars')
def cars_page():
    return ', '.join(cars)

#Случайным образом выбирает одну породу кошки и возвращает ее название.
@app.route('/cats')
def random_cat():
    breed = random.choice(cat_breeds)
    return f'Порода кошки: {breed}'

#Создаем маршрут и получаем текущее время и выводит его в нужном формате
@app.route('/get_time/now')
def current_time():
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return f'Точное время: {now}'

#Вычисляет время через 1 часот текущего и выводит в том же формате
@app.route('/get_time/future')
def future_time():
    future = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%H:%M:%S')
    return f'Точное время через час будет: {future}'

#Берем рандомное слово, удаляем все символы кроме букв, возвращаем слово
@app.route('/get_random_word')
def random_word():
    word = random.choice(book_words)
    word = ''.join(c for c in word if c.isalpha())
    return f'Случайное слово: {word}'

#Увеличивает счетчик при каждом входе
@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Страница посещена: {counter.visits} раз(а)'

counter.visits = 0

#Запускает сервер с включенной отладкой
if __name__ == '__main__':
    app.run(debug=True)