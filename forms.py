from wtforms import Form, StringField, PasswordField, BooleanField, validators, TextAreaField


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])


class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20), validators.DataRequired()])
    email = StringField('Email Address', [validators.Email(), validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=8, message='password must be longer than 8 characters'),
        validators.EqualTo('confirm', message='Passwords Must match')
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])

    accept_tos = BooleanField('I accept the terms of service', [validators.DataRequired()])


class MessageForm(Form):
    name = StringField('Name', [validators.Length(min=1), validators.DataRequired()])
    email = StringField('Email Address', [validators.Email(), validators.DataRequired()])
    message = TextAreaField('message', [validators.Length(min=1, max=300), validators.DataRequired()])
