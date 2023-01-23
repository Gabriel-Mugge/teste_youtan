from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField



class FormularioEmpresa(FlaskForm):
    opcoes = [
        ('Ativo', 'Sim'),
        ('Inativo', 'Não')
    ]

    cnpj_empresa = StringField('CNPJ', [validators.DataRequired()])
    nome_empresa = StringField('Nome', [validators.DataRequired()])
    situacao_empresa = SelectField('Situação', [validators.DataRequired()], choices=opcoes)

    cadastrar = SubmitField('Cadastrar')



class FormularioFilial(FlaskForm):

    opcoes = [
        ('Ativo', 'Sim'),
        ('Inativo', 'Não')
    ]

    cnpj_empresa = StringField('CNPJ', [validators.DataRequired()])
    nome_filial = StringField('Nome', [validators.DataRequired()])
    situacao_filial = SelectField('Situação', [validators.DataRequired()], choices=opcoes)

    cadastrar = SubmitField('Cadastrar')






