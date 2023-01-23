function mascaraCNPJ(cnpj){
    let texto = cnpj.value.toString()

    if(texto.length == 2) {
        texto += "."

    }else if (texto.length == 6){
         texto += "."
    }else if (texto.length == 10){
         texto += "/"
    }else if (texto.length == 15){
         texto += "-"
    }

    cnpj.value = texto
}