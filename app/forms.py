from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired


class ReviewForm(FlaskForm):
    author = StringField(
        'Ваше имя',
        validators=[DataRequired(message='Поле не должно быть пустым'),
                    Length(max=127, message='Слишком длинное имя')]
    )
    text = TextAreaField(
        'Текст отзыва',
        validators=[DataRequired(message='Поле не должно быть пустым')]
    )
    score = SelectField(
        'Оценка',
        choices=list(range(1, 11))
    )
    submit = SubmitField('Добавить отзыв')


class MovieForm(FlaskForm):
    title = StringField(
        'Название фильма',
        validators=[DataRequired(message='Поле не должно быть пустым'),
                    Length(max=127, message='Слишком длинное название')]
    )
    text = TextAreaField(
        'Описание фильма',
        validators=[DataRequired(message='Поле не должно быть пустым')]
    )
    image = FileField(
        'Изображение',
        validators=[FileRequired(message='Файл не выбран'),
                    FileAllowed(['jpg', 'png', 'jpeg'], message="Неверный формат файла")]
    )
    submit = SubmitField(
        'Добавить фильм'
    )
