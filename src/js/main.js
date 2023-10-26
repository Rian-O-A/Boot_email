let tbody = document.querySelector('tbody')

let selecionados = {}

async function desenhoNaTela() {

    const dados = await pegarDados()
    let dados_filtrados = Object.values(dados.informacao)

    const dadosE = await pegarEmails()
    const emails_filtrados = Object.values(dadosE)

    dados_filtrados = dados_filtrados.map((dado, i) => {
        dado.email = dadosE[dado.nome]
        return dado
    })

   

    for (let i = 0; i < 50; i++) {

        let tr = document.createElement('tr')

        let contato = dados_filtrados[i].contato?.replace("(", "").replace(" ", "").replace(")", "").replace("-", "");

        let nFiltrado

        if (contato && contato.length == 11) {
            nFiltrado = "55" + contato
        }

        let nCerto = contato

        if (nCerto && nCerto.length > 9) {
            nCerto = nCerto.split('').filter(element => element != ' ').join('')
        }

        if (nCerto) {
            nCerto = nCerto.replace()
            nCerto = '(' + nCerto
            nCerto = nCerto.replace(nCerto[2], nCerto[2] + ') ')

            nCerto = nCerto.split('')
            nCerto[nCerto.length - 5] = nCerto[nCerto.length - 5].replace(/\w$/, nCerto[nCerto.length - 5] + '-')
            nCerto = nCerto.join('')
        }

        tr.innerHTML += `       

                                <td scope="row" class="d-flex">
                                <label for="check-box${i}" class="label-checkbox d-flex">
                                <input type="checkbox" id="check-box${i}" class="form-check-input">
                                
                                </label>

                                <button type="button" class="btn w-30" data-bs-toggle="modal" data-bs-target="#staticBackdrop${i}" style="margin:0 auto;">
                                    ${dados_filtrados[i].nome}
                                </button>
                                
                                <div class="modal fade modal-xl" id="staticBackdrop${i}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel${i}" aria-hidden="true">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="staticBackdropLabel${i}">Modal title</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        ...
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary">Understood</button>
                                    </div>
                                    </div>
                                </div>
                                </div>

                                </td>

                                <td colspan="2"><a class="nTelefone" id="nTelefone${i}" ${nFiltrado ? `target="_blank"` : `target="unset"`} href="${nFiltrado ? "https://wa.me/" + nFiltrado + "?text=Tenho%20interesse%20em%20comprar%20seu%20carro" : "#"}">${nCerto ?? "-"}</a></td>

                                <td colspan="1">
                                    <a href="${dados_filtrados[i].email ? `mailto:` + dados_filtrados[i].email[0] : `#`}">
                                        <svg width="36" height="36" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M33.334 6.66797H6.66732C4.83398 6.66797 3.35065 8.16797 3.35065 10.0013L3.33398 30.0013C3.33398 31.8346 4.83398 33.3346 6.66732 33.3346H33.334C35.1673 33.3346 36.6673 31.8346 36.6673 30.0013V10.0013C36.6673 8.16797 35.1673 6.66797 33.334 6.66797ZM33.334 13.3346L20.0007 21.668L6.66732 13.3346V10.0013L20.0007 18.3346L33.334 10.0013V13.3346Z" 
                                            fill="${dados_filtrados[i].email != null ? "green" : "black"}"/>
                                        </svg>
                                    </a>
                                </td>

                                <td colspan="2">
                                <a href="${dados_filtrados[i].site != null ? dados_filtrados[i].site : "#"}">
                                    <svg width="35px" height="35px" viewBox="0 0 40 40" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <g clip-path="url(#clip0_14_144)">
                                            <path
                                                d="M18 0C13.2261 0 8.64773 1.89642 5.27208 5.27208C1.89642 8.64773 0 13.2261 0 18C0 22.7739 1.89642 27.3523 5.27208 30.7279C8.64773 34.1036 13.2261 36 18 36C22.7739 36 27.3523 34.1036 30.7279 30.7279C34.1036 27.3523 36 22.7739 36 18C36 13.2261 34.1036 8.64773 30.7279 5.27208C27.3523 1.89642 22.7739 0 18 0V0ZM33 12.96C32.729 13.8469 32.2785 14.6686 31.6764 15.374C31.0742 16.0793 30.3334 16.6532 29.5 17.06C29.056 15.393 28.2355 13.8501 27.1017 12.5498C25.9679 11.2496 24.551 10.2268 22.96 9.56C23.2189 8.67259 23.7773 7.90226 24.54 7.38C23.68 6.82 22.54 6.54 21.86 7.52C20.8 8.9 21.86 10.74 22.28 11.52V11.8C21.1695 11.1265 20.3013 10.1181 19.8 8.92C17.8675 8.85793 15.9559 9.33582 14.28 10.3C14.106 9.1708 14.216 8.01606 14.6 6.94C15.3222 7.00894 16.0503 6.89904 16.72 6.62C17.3897 6.34096 17.9804 5.90136 18.44 5.34C19.36 4.3 18.18 2.98 17.26 2.18H17.98C20.7028 2.16163 23.3836 2.8508 25.76 4.18C27.1032 5.1727 28.2078 6.45275 28.9932 7.92674C29.7787 9.40073 30.2251 11.0315 30.3 12.7C30.78 12.7 31.7 11.6 32.12 10.86C32.464 11.538 32.758 12.24 33 12.96ZM18 33.68C13.9 29.52 18.5 26.18 16 23.2C14.16 21.5 11.42 22.68 9.78 20.74C9.50316 19.2937 9.62283 17.7995 10.1263 16.4157C10.6299 15.0319 11.4984 13.8102 12.64 12.88C13.68 12 20.64 10.88 23.48 13.32C25.1411 14.7507 26.3096 16.668 26.82 18.8C27.7378 18.8693 28.6558 18.6677 29.46 18.22C30.28 24.18 23.16 31.7 18 33.68ZM10.3 4.18C11.0644 3.88858 11.904 3.86014 12.6864 4.09919C13.4687 4.33823 14.1491 4.83112 14.62 5.5C13.78 6.26 12.74 6.76 11.62 6.94C11.6614 6.35109 11.7894 5.77152 12 5.22L10.3 4.18Z"
                                                fill="${dados_filtrados[i].site != null ? "green" : "black"}" />
                                        </g>
                                        <defs>
                                            <clipPath id="clip0_14_144">
                                                <rect width="40" height="40" fill="white" />
                                            </clipPath>
                                        </defs>
                                    </svg>
                                    </a>
                                </td>
                                <td style="">
                                    <select class="form-select bomba" id="${i}" value="1" aria-label="Default select example"
                                        style="width: 35px; height: 35px; border-radius: 50%; padding: 0; background-image: none; text-align-last:center; margin:auto">
                                        <option selected value="1" style="background-color: grey;"></option>
                                        <option value="2" style="background-color: #FFA500;"></option>
                                        <option value="3" style="background-color: #FF0000;"></option>
                                        <option value="4" style="background-color: #008937;"></option>
                                    </select>
                                </td>
                                
                            `;

        tbody.appendChild(tr)

        if (nFiltrado) {
            document.getElementById(`nTelefone${i}`).className = "nTelefone"
        }
        else {
            document.getElementById(`nTelefone${i}`).className = "noTelefone"
        }

        let sendButtons = document.querySelectorAll('.sendButtons')
        let checkId = document.getElementById(`check-box${i}`)

        checkId.addEventListener('change', aparece)

        selecionados[checkId.id] = false

        function aparece(event) {
            selecionados[event.target.id] = event.target.checked
            verificaChecked()
        }
    }

    function verificaChecked(){
        if (Object.values(selecionados).filter(item => item).length > 0){
            document.getElementById(`bototes`).style.display = 'flex'
        }
        else {
            document.getElementById(`bototes`).style.display = 'none'
        }
    }

    let bomba = document.querySelectorAll('.bomba')

    for (let i = 0; i < bomba.length; i++) {

        const element = bomba[i];

        element.addEventListener('change', bombinha)

        element.style.background = 'gray'

        localStorage.getItem(element.id)

        if (localStorage.getItem(element.id) == 1) {
            element.style.background = 'gray'
        }

        if (localStorage.getItem(element.id) == 2) {
            element.style.background = '#FFA500'
        }

        if (localStorage.getItem(element.id) == 3) {
            element.style.background = '#FF0000'
        }

        if (localStorage.getItem(element.id) == 4) {
            element.style.background = '#008937'
        }
    }
}

desenhoNaTela()

function bombinha(event) {

    console.log(event.target.value)

    if (event.target.value == 1) {
        event.target.style.background = 'gray'
    }

    if (event.target.value == 2) {
        event.target.style.background = '#FFA500'
    }

    if (event.target.value == 3) {
        event.target.style.background = '#FF0000'
    }

    if (event.target.value == 4) {
        event.target.style.background = '#008937'
    }

    localStorage.setItem(event.target.id, event.target.value);
}

async function pegarDados() {
    const response = await fetch('src/dados_filtrados.json');
    const data = await response.json();

    return data
}

async function pegarEmails() {
    const responseEmail = await fetch('src/e_mail-final.json');
    const dataEmail = await responseEmail.json();

    return dataEmail
}
