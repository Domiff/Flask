from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange

from create_validator import NumRange, StringType


app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(),
                                     NumRange(min_=1000000000,
                                              max_=9999999999,
                                              message="Invalid value, field must be less then 10 character")])
    name = StringField(validators=[InputRequired(), StringType(message="Invalid value")])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    name = form.name.data

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Пользователь {name} зарегистрирован с электронной почтой {email} и номером телефоном {phone}\n"

    return f"Bad request {form.errors}\n", 400
