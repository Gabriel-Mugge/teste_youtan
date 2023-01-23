const mascara = document.querySelector('#mascara-pop-up')
const mascara1 = document.querySelector('#mascara-pop-up1')
const novo = document.querySelector('.novo')
const editars = document.querySelectorAll('#editar_filial')


novo.addEventListener('click', () => {
    mascara.style.display = 'block'
})


editars.forEach(editar => {
    editar.addEventListener('click', () => {
        mascara1.style.display = 'block'
    })
})


mascara.addEventListener('click', event => {

	const alvo_click = event.target.id

	if (alvo_click == 'mascara-pop-up' || alvo_click == 'pop-up-close'){
		mascara.style.display = 'none'
	}

})



mascara1.addEventListener('click', event => {

	const alvo_click = event.target.id

	if (alvo_click == 'mascara-pop-up1' || alvo_click == 'pop-up-close1'){
		mascara1.style.display = 'none'
	}

})


function abrir_popup_editar_filial(){
     mascara1.style.display = 'block'
}


