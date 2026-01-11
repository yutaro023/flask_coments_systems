let button = document.getElementsByTagName("form")[0]

button.addEventListener("submit", (event) => {
    let dataNascimento = new Date(document.getElementById("data-nascimento").value)
    let hoje = new Date()
    let idade = Math.abs(dataNascimento.getFullYear() - hoje.getFullYear())
    let mesAtual = hoje.getMonth()
    let diaAtual = hoje.getDay()
    let mesNascimento = dataNascimento.getMonth()
    let diaNascimento = dataNascimento.getDay()
    if(mesAtual < mesNascimento || (mesAtual === mesNascimento && diaAtual < diaNascimento)) idade--
    if(idade < 18) {
        event.preventDefault() //impede o submit
        alert("Você não tem a idade necessária para prosseguir")
    }
});


