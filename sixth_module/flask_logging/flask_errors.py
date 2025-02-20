import logging.config

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired

from flask_logger import dict_logger


app = Flask(__name__)

logging.config.dictConfig(dict_logger)
logger = logging.getLogger("flask_app_logger")

class NumberForm(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])


@app.route("/numbers", methods=["POST"])
def divide():
    form = NumberForm()

    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        result = a / b
        logger.info("All good")

        return f"a / b = {result}"

    return f"Bad request. Errors = {form.errors}", 400


@app.errorhandler(ZeroDivisionError)
def zero_division_handler(exception: ZeroDivisionError):
    logger.warning(exception)
    return "На ноль делить нельзя", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()
