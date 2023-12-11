const getList = async () => {
    let url = 'http://127.0.0.1:5000/index.html';
    fetch(url,{
        method: 'get',
    })
        .then((response) => response.json())
        .then((data) => {
            data.index.forEach(item => insertList(item.nome, item.tel))
        })
}
getList()

const postItem = async (inputNome, inputTelefone, inputEmail, inputEnd, inputT_imovel, inputArea, inputQuartos, 
    inputBanheiros, inputVagas, inputValor, inputImagens) => {
    const formData = new FormData();
    formData.append('nome', inputNome);
    formData.append('tel', inputTelefone);
    formData.append('email', inputEmail);
    formData.append('endereco', inputEnd);
    formData.append('tipo_do_imovel', inputT_imovel);
    formData.append('area', inputArea);
    formData.append('quartos', inputQuartos);
    formData.append('banheiros', inputBanheiros);
    formData.append('vagas', inputVagas);
    formData.append('valor', inputValor);
    formData.append('imagens', inputImagens);

    let url = 'http://127.0.0.1:5000/index.html';
    fetch(url,{
        method: 'post',
        body: formData
    })
        .then((response) => response.json())
        .catch((error) => {
            console.error('Error:', error);
        });
}

const newItem = () => {
    let inputNome = document.getElementById("f_nome").value;
    let inputTelefone = document.getElementById("f_tel").value;
    let inputEmail = document.getElementById("f_mail").value;
    let inputEnd = document.getElementById("f_end").value;
    let inputT_imovel = document.getElementById("f_tipo").value;
    let inputArea = document.getElementById("f_area").value;
    let inputQuartos= document.getElementById("f_quartos").value;
    let inputBanheiros = document.getElementById("f_banheiros").value;
    let inputVagas = document.getElementById("f_vagas").value;
    let inputValor = document.getElementById("f_valor").value;

    
    insertItem("Nome: " + inputNome,"Telefone: "+ inputTelefone,"E-mail: " + inputEmail,"Endereço: "+inputEnd,
            "Tipo de Imóvel: "+inputT_imovel, "Área do Imóvel: "+inputArea,"Quartos: "+inputQuartos,
            "Banheiros: "+inputBanheiros,"Vagas de Garagem: "+inputVagas,"Valor do Aluguel: R$"+ inputValor+ ",00"
            )
    postItem(inputNome, inputTelefone, inputEmail, inputEnd, inputT_imovel, inputArea, inputQuartos, inputBanheiros,
        inputVagas, inputValor)
    };
    
const insertItem = (nome, tel, email, endereco, t_imovel, area,
                    quartos, banheiros, vagas, valor) => {
    var item = [nome, tel, email, endereco, t_imovel, area, quartos, banheiros, vagas, valor];
    var table = document.getElementById('my_table');
    var row = table.insertRow();

    for (var i = 0; i < item.length; i++) {
        var cel = row.insertCell(i);
        cel.textContent = item[i];
    }
}

const f_imagens = document.getElementById("f_imagens")
const preview = document.getElementById("preview")

f_imagens.addEventListener("change", function (e) {
    preview.innerHTML ="";
    for (const imagem of e.target.files){
        console.log(imagem);

        const imagemHTML = `<img src="${URL.createObjectURL(imagem)}" alt="${imagem.name}" style="max-width: 200px;
        max-height: 300px; margin: 10px; object-fit: cover" >`;

        preview.insertAdjacentHTML("beforeend", imagemHTML)
    }
})

