function buscar_preencher(id){
    fetch('/motorista_login/buscar_motorista_login/' + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('id').value = result.data.id
        document.getElementById('celular').value = result.data.telefone
        document.getElementById('usuario').value = result.data.usuario
        document.getElementById('motorista').value = result.data.motorista

    }).catch(error => console.error(error))

    document.getElementById('btn_alterar').disabled = false
    document.getElementById('btn_cadastrar').disabled = true

}
