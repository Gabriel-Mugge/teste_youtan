from flask import render_template, request, redirect, flash, url_for
from main import app, db
from models import Empresa
from helpers import FormularioEmpresa


def fomatar_cnpj(cnpj):
    return cnpj[0:2] + "." + cnpj[2:5] + "." + cnpj[5:8] + "/" + cnpj[8:12] + "-" + cnpj[12:]


@app.route('/')
def index():


    lista_empresas = Empresa.query.order_by(Empresa.cnpj_empresa)

    tabela_empresas = ""
    for dados_empresa in lista_empresas:

        situacao = 'ativo' if dados_empresa.situacao_empresa == 'Ativo' else 'inativo'
        cnpj_empresa_limpo = dados_empresa.\
            cnpj_empresa.replace(".", "").replace("/", "").replace("-", "")

        tabela_empresas += \
        f'''
            <tr>
                <td>{dados_empresa.nome_empresa}</td>
                <td><span class="{situacao}">{dados_empresa.situacao_empresa}</span></td>
                <td><a class="editar_in_table" href="{url_for('novo', cnpj_empresa=cnpj_empresa_limpo)}"><span class="material-icons">edit_note</span>Editar</a></td>
            </tr>
        '''


    form = FormularioEmpresa(request.form)

    return render_template(
        'index.html',
        tabela_empresas=tabela_empresas,
        form=form
    )



@app.route('/cadastrar_empresa', methods=['POST',])
def cadastrar_empresa():
    
    form = FormularioEmpresa(request.form)

    cnpj_empresa = form.cnpj_empresa.data
    nome_empresa = form.nome_empresa.data
    situacao_empresa = form.situacao_empresa.data

    empresa = Empresa.query.filter_by(cnpj_empresa=cnpj_empresa).first()

    if empresa:
        flash('Esse cnpj já existente na base de dados!')
        return redirect(url_for('index'))

    nova_empresa = Empresa(
        cnpj_empresa=cnpj_empresa,
        nome_empresa=nome_empresa,
        situacao_empresa=situacao_empresa                      
    )
    db.session.add(nova_empresa)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/atualizar_empresa/<string:cnpj_empresa>', methods=['POST',])
def atualizar_empresa(cnpj_empresa):



    cnpj_empresa_sujo = cnpj_empresa
    cnpj_empresa = fomatar_cnpj(cnpj_empresa)
    form = FormularioEmpresa(request.form)

    empresa = Empresa.query.filter_by(cnpj_empresa=cnpj_empresa).first()
    empresa.nome_empresa = form.nome_empresa.data
    empresa.situacao_empresa = form.situacao_empresa.data


    db.session.add(empresa)
    db.session.commit()

    return redirect(url_for('novo', cnpj_empresa=cnpj_empresa_sujo))


@app.route('/deletar_empresa/<string:cnpj_empresa>')
def deletar_empresa(cnpj_empresa):

    cnpj_empresa = fomatar_cnpj(cnpj_empresa)
    Empresa.query.filter_by(cnpj_empresa=cnpj_empresa).delete()
    db.session.commit()


    return redirect(url_for('index'))



