from flask import Flask
from random import choice
from datetime import datetime, timedelta
import re


app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return "Привет мир!"


list_car = ['Chevrolet', 'Renault', 'Ford', 'Lada']

@app.route('/cars')
def cars():
    return list_car


list_cats = ['корниш-рекс', 'русская голубая', 
             'шотландская вислоухая', 'мейн-кун', 'манчкин']

@app.route('/cats')
def cats():
    return choice(list_cats)


@app.route('/get_time/now')
def time_now():
    current_time = datetime.now()
    return f"Текущее время сейчас: {current_time}"


@app.route('/get_time/future')
def time_future():
    current_time = datetime.now()
    delta = timedelta(hours=1)
    current_time_after_hour = current_time + delta 
    return f"Точное время через час будет {current_time_after_hour}"    

print(time_future())

def get_word():
    with open('war_and_peace.txt', 'r', encoding='utf-8') as book:
        list_words = re.findall(r'\b\w+\b', book.read())
        word = choice(list_words)
        return word
    

@app.route('/war_and_piece')
def random_word():
    return get_word()
        

count = 0

@app.route('/counter')
def counter():
    global count
    count += 1
    return f"{count}" 


if __name__ == '__main__':
    app.run()
