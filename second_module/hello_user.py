from datetime import datetime, date

from flask import Flask


app = Flask(__name__)


weekday_tuple = ("Хорошего понедельника!", "Хорошего вторника!", "Хорошей среды!",
           "Хорошего четверга!", "Хорошей пятницы!", "Хорошей субботы!", "Хорошего воскресенья!")


@app.route('/hello_world/<name>')
def hello_world(name):
    weekday = datetime.today().weekday()
    match weekday:
        case 0:
            return f"Привет, {name}. {weekday_tuple[0]}"
        case 1:
            return f"Привет, {name}. {weekday_tuple[1]}"
        case 2:
            return f"Привет, {name}. {weekday_tuple[2]}"
        case 3:
            return f"Привет, {name}. {weekday_tuple[3]}"
        case 4:
            return f"Привет, {name}. {weekday_tuple[4]}"
        case 5:
            return f"Привет, {name}. {weekday_tuple[5]}"
        case 6:
            return f"Привет, {name}. {weekday_tuple[6]}"


if __name__ == '__main__':
    app.run(debug=True)
