from flask_security.forms import (
    ConfirmRegisterForm, NextFormMixin)
from wtforms.validators import Required
from wtforms import TextField
from flask import request


class ExtendedRegisterForm(
        ConfirmRegisterForm, NextFormMixin):
    name = TextField('Name', [Required()])
    phone = TextField('Phone Number')

    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None)
        self.phone = kwargs.pop('phone', None)
        super(ExtendedRegisterForm, self).__init__(*args, **kwargs)
        if not self.next.data:
            self.next.data = request.args.get('next', '')