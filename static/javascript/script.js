let button = document.getElementsByTagName("form")[0]
let error = document.getElementById("error").dataset.error
const navType = performance.getEntriesByType("navigation")[0].type;

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

console.log(navType)

if(error === "email_existe" && navType !== "reload") {
    alert("Esse E-mail já existe")
}