from flask import Flask


app = Flask(__name__)


@app.route('/max_number/<path:number>')
def max_number(number: str):
    num = (int(i) for i in number.split('/'))
    return f"Максимальное число: <i>{max(num)}<i>"


if __name__ == '__main__':
    app.run(debug=True)