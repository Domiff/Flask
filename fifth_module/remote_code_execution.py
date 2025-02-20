import os
import subprocess

import flask_wtf
from flask import Flask, request
from wtforms.fields.simple import StringField
from wtforms.validators import InputRequired


app = Flask(__name__)


class CmdForm(flask_wtf.FlaskForm):
    command = StringField(validators=[InputRequired()])


@app.route("/ex", methods=["POST"])
def remote_cod_execution():
    form = CmdForm()

    if form.validate_on_submit():
        code = request.form.get("command")
        command = ["prlimit", "--nproc=1:1", "python3", "-c", code]

        result = subprocess.Popen(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            stdout, stderr = result.communicate(timeout=1)
        except subprocess.TimeoutExpired:
            return "Время вышло"

        return f"Результат команды: {stdout}"

    return form.errors


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
