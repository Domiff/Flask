import os
import sys

from flask import Flask


app = Flask(__name__)


@app.route('/file/<int:size>/<relative_path>')
def show_preview_file(size: int, relative_path):
    abs_path = os.path.abspath(relative_path)
    with open(abs_path, 'r', encoding='utf-8') as file:
        result_text = file.read(size)
        result_size = sys.getsizeof(result_text)
    return (f"Информация о файле: Абсолютный путь к файлу: {abs_path}, "
            f"Размер части файла: {result_size} "
            f"<p>Первые символы из файла: {result_text}</p><b r>")


if __name__ == '__main__':
    app.run(debug=True)

# print(*show_preview_file(12, 'text.txt'))