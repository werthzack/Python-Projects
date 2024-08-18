from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class NewPostForm(FlaskForm):
    title = StringField("Blog Title", validators=[DataRequired()])
    sub_title = StringField("Blog Sub-Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    image_url = StringField("Image Url", validators=[DataRequired(), URL()])
    body = CKEditorField("Content", validators=[DataRequired()])
    submit = SubmitField("Post Blog")
