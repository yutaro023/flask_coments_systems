let div = document.getElementById("login-error")
let error = div.dataset.validacao
let email = document.getElementById("i-email")
let password = document.getElementById("i-pass")
let form = document.getElementsByTagName("form")[0]

console.log(error)

form.addEventListener("submit", (event) => {
    if(password.value !== '' || email.value !== '') {
        alert("Suas Credenciais estao erradas!")

    }       
})






