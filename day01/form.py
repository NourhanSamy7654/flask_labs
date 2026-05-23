from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    content = TextAreaField(
        "Content",
        validators=[DataRequired(), Length(min=10, max=500)],
        render_kw={"class": "form-control"}
    )

    author = StringField(
        "Author",
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )