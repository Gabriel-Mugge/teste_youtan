function submitForm_empresa() {
    const form_empresa = document.getElementById("form_edit_empresa")
    form_empresa.submit()
}

const form_filial = document.getElementById("form_editar_filial")
const input_edit_nome_filial = document.querySelector('.edit_nome_filial')
const input_edit_cnpj_filial = document.querySelector('.edit_cnpj_filial')
const input_edit_situacao_filial = document.querySelector('.edit_situacao_filial')
const input_edit_id_filial = document.querySelector('.edit_id_filial')


//Carrega os dados para o popup de editar filial de forma assincrona
function editar_filial(id){
    fetch(`/editar_filial/${id}`)
        .then(response => response.json())
        .then(data => {
            input_edit_nome_filial.value = data['nome']
            input_edit_cnpj_filial.value = data['CNPJ']
            input_edit_situacao_filial.value = data['situacao']
            input_edit_id_filial.value = data['id']
        })

    abrir_popup_editar_filial()
}


//Efetiva as atualizações da filial de forma assincrona.
form_filial.addEventListener('submit', e => {
    e.preventDefault()

    data = {
        'id_filial': input_edit_id_filial.value,
        'nome_filial': input_edit_nome_filial.value,
        'situacao': input_edit_situacao_filial.value
    }

    fetch(
        "/atualizar_filial",
         {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {'content-type': 'application/json'}
         }
    )

    const mascara1 = document.querySelector('#mascara-pop-up1')
    mascara1.style.display = 'none'

    const nome_filial_pos_edit = document.querySelector(`#nome_filial_id${input_edit_id_filial.value}`)
    const situacao_filial_pos_edit = document.querySelector(`#situacao_filial_id${input_edit_id_filial.value}`)

    nome_filial_pos_edit.innerHTML = input_edit_nome_filial.value
    situacao_filial_pos_edit.innerHTML = input_edit_situacao_filial.value
    situacao_filial_pos_edit.className = input_edit_situacao_filial.value.toString().toLowerCase()


})