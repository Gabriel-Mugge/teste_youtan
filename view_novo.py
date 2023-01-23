from main import app, db
from flask import render_template, request, redirect, flash, url_for, jsonify
from models import Filial, Empresa
from helpers import FormularioFilial, FormularioEmpresa


def fomatar_cnpj(cnpj):
    return cnpj[0:2] + "." + cnpj[2:5] + "." + cnpj[5:8] + "/" + cnpj[8:12] + "-" + cnpj[12:]



@app.route('/novo/<string:cnpj_empresa>', methods=['GET', 'POST'])
def novo(cnpj_empresa):


    cnpj_empresa_sujo = cnpj_empresa
    cnpj_empresa = fomatar_cnpj(cnpj_empresa)

    lista_filiais = Filial.query.order_by(
        Filial.Empresa_cnpj_empresa
    ).filter(
        Filial.Empresa_cnpj_empresa == cnpj_empresa
    )


    tabela_filiais = ""
    for dados_filial in lista_filiais:

        situacao = 'ativo' if dados_filial.situacao_filial == 'Ativo' else 'inativo'
        rota_exclusao = url_for(
            'deletar_filial',
            id_filial=dados_filial.id_filial,
            cnpj_empresa=cnpj_empresa_sujo
        )

        tabela_filiais += \
        f'''
            <tr>
                <td>{cnpj_empresa}</td>
                <td id="nome_filial_id{dados_filial.id_filial}" class="nome_filial">{dados_filial.nome_filial}</td>
                <td><span id="situacao_filial_id{dados_filial.id_filial}" class="{situacao}">{dados_filial.situacao_filial}</span></td>
                <td><a id="editar_filial" class="editar_in_table" href="#" onclick="editar_filial({dados_filial.id_filial})"><span class="material-icons">edit_note</span>Editar</a></td>
                <td><a class="excluir_in_table" href="{rota_exclusao}"><span class="material-icons">delete_outline</span>Excluir</td>
            </tr>
        '''

    form_empresa = FormularioEmpresa(request.form)
    dados_empresa = Empresa.query.filter(
        Empresa.cnpj_empresa == cnpj_empresa
    ).first()



    form_empresa.nome_empresa.data = dados_empresa.nome_empresa
    form_empresa.situacao_empresa.data = dados_empresa.situacao_empresa

    form_filial = FormularioFilial(request.form)

    if request.args.get('editar') != None:
        id_filial = request.args.get('id_filial')
        filial = Filial.query.filter(
            Filial.id_filial == id_filial
        ).first()
        form_filial.nome_filial.data = filial.nome_filial
        form_filial.situacao_filial.data = filial.situacao_filial



    return render_template(
        'novo.html',
        tabela_filiais=tabela_filiais,
        cnpj_empresa=cnpj_empresa_sujo,
        form_empresa=form_empresa,
        form_filial=form_filial
    )



@app.route('/cadastrar_filial/<string:cnpj_empresa>', methods=['GET', 'POST',])
def cadastrar_filial(cnpj_empresa):


    form = FormularioFilial(request.form)

    cnpj_empresa_sujo = cnpj_empresa
    cnpj_empresa = fomatar_cnpj(cnpj_empresa)
    nome_filial = form.nome_filial.data
    situacao_filial = form.situacao_filial.data


    nova_filial = Filial(
        nome_filial=nome_filial,
        situacao_filial=situacao_filial,
        Empresa_cnpj_empresa=cnpj_empresa
    )
    db.session.add(nova_filial)
    db.session.commit()



    return redirect(url_for('novo', cnpj_empresa=cnpj_empresa_sujo))



@app.route('/deletar_filial/<int:id_filial>/<string:cnpj_empresa>')
def deletar_filial(id_filial, cnpj_empresa):

    Filial.query.filter_by(id_filial=id_filial).delete()
    db.session.commit()


    return redirect(url_for('novo', cnpj_empresa=cnpj_empresa))




@app.route('/editar_filial/<int:id_filial>', methods=['GET', 'POST'])
def editar_filial(id_filial):

    filial = Filial.query.filter_by(id_filial=id_filial).first()


    dicio = {
        "nome": filial.nome_filial,
        "CNPJ": filial.Empresa_cnpj_empresa,
        "situacao": filial.situacao_filial,
        "id": id_filial
    }


    return dicio



@app.route('/atualizar_filial', methods=['GET', 'POST'])
def atualizar_filial():

    data = request.get_json()

    filial = Filial.query.filter_by(id_filial=data['id_filial']).first()
    filial.nome_filial = data['nome_filial']
    filial.situacao_filial = data['situacao']


    #PERSISTINDO ALTERAÇÕES
    db.session.add(filial)
    db.session.commit()

    return {}



