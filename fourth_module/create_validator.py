from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


class NumRange:
    def __init__(self, min_=-1, max_=-1, message=None):
        self.min = min_
        self.max = max_
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        l = field.data and field.data or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)


class StringType:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        f = field.data
        if not isinstance(f, str):
            raise ValidationError(self.message)