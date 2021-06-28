from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import DateField, FloatField
from wtforms.validators import DataRequired, Length

'''
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')
'''
campoObrigatorioMensagem = "Campo obrigatório"

class ContasapagarForm(FlaskForm):
    valor = FloatField('Valor', validators=[DataRequired(campoObrigatorioMensagem)])
    emissao = DateField('Emissão', validators=[DataRequired(campoObrigatorioMensagem)], format='%d/%m/%Y')
