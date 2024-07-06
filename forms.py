from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class municipio(Form):
    municipio = StringField('municipios')
    apartado = StringField('apartado')