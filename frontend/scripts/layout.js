`use strict`;

const carregarLayout = async(elemento, arquivo) => {
    const response = await fetch(arquivo);

    if(!response.ok){
        throw new Error(`Não foi possível carregar arquivo ${arquivo}`);
    }

    const html = await response.text();

    document.querySelector(elemento).innerHTML = html;

}

document.addEventListener("DOMContentLoaded", async() => {
    await carregarLayout(`#header`, `../layout/header/header.html`);
    await carregarLayout(`#footer`, `../layout/footer/footer.html`);
});