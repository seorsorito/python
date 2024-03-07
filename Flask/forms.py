from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Email,Length
from wtforms.widgets import TextArea


class SignupForm(FlaskForm):
    name=StringField('nombre',validators=[DataRequired(),Length(max=10)])
    password=PasswordField('contra',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired(),Email()])
    remember_me = BooleanField('recuerdame')
    submit=SubmitField('Envio_formulario')

class PostForm(FlaskForm):
    title=StringField('Titulo',validators=[DataRequired(),Length(max=30)])
    title_slug=StringField('Titulo_slug',validators=[Length(max=128)])
    content=StringField('Contenido',widget=TextArea())
    submit=SubmitField('Envio_formulario')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('contra',validators=[DataRequired()])
    remember_me = BooleanField('recuerdame')
    submit=SubmitField('Envio_formulario')


    
   