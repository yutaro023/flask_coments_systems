let div = document.getElementById("login-error")
let error = div.dataset.validacao

const navType = performance.getEntriesByType("navigation")[0].type;

console.log(navType)

if (error === "True" && navType !== "reload") {
    alert("suas credenciais estao erradas");
}