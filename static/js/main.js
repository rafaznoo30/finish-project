console.log(document.getElementById('formDataBoyaca'))
document.addEventListener("DOMContentLoaded", () => {
    //Cambio de data en Boyaca
    document.getElementById('formDataBoyaca').addEventListener('submit', function (event) {
        event.preventDefault();

        const apartado = document.getElementById('apartado-boyaca').value;
        const municipio = document.getElementById('municipios-boyaca').value;

        const data = {
            apartado: apartado,
            departamento: 'Boyacá',
            municipio: municipio
        };

        fetch('/dataBoyaca', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const imgDataBoyaca = document.getElementById('imgDataBoyaca');
                if (imgDataBoyaca) {
                    imgDataBoyaca.remove();
                }
                const container = document.getElementById('containerDataBoyaca');
                container.insertAdjacentHTML('afterbegin', `<img id='imgDataBoyaca' class="rounded mx-auto d-block img-fluid" src="${data.srcImage}?${new Date().getTime()}">`);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });
})
