from flask import Flask


app = Flask(__name__)



@app.route('/hello_world')
def hello_world():
    return "Привет мир!"


count = 0

@app.route('/counter')
def counter():
    global count
    count += 1
    return f"{count}" 
