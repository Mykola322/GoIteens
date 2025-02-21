from flask_wtf import FlaskForm
import wtforms


class SignUpForm(FlaskForm):
    first_name = wtforms.StringField("Введіть ім'я")
    last_name = wtforms.StringField("Введіть прізвище")
    email = wtforms.EmailField("Email", validators=[wtforms.validators.Email(), wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Введіть пароль", validators=[wtforms.validators.lenght(8)])


class LoginForm(FlaskForm):
    email = wtforms.EmailField("Email", validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    passsword = wtforms.PasswordField("Пароль", validators=[wtforms.validators.length(8)])