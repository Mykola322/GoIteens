from flask_wtf import FlaskForm
import wtforms


class ReviewForm(FlaskForm):
    text = wtforms.StringField("Введіть свій відгук про даний товар", validators=[wtforms.validators.length(5, message = "Відгук не може містити менше 5-ти символів!")])
    name = wtforms.StringField("Введіть своє ім'я", validators=[wtforms.validators.DataReqired()])
    submit = wtforms.SubmitField("Зберегти")