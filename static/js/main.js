console.log(document.getElementById('formDataBoyaca'))
document.addEventListener("DOMContentLoaded", () => {

    //Fetch de data en Boyaca
    document.getElementById('formDataBoyaca').addEventListener('submit', function (event) {
        event.preventDefault();

        const apartado = document.getElementById('apartado-boyaca').value;
        const municipio = document.getElementById('municipios-boyaca').value;


        let elementValidate = document.getElementById('elementValidateBoyaca');
        if (apartado === 'Seleccione una opción' || municipio === 'Seleccione una opción') {
            elementValidate.classList.remove('hide-element');
        } else {
            if (!elementValidate.classList.contains('hide-element')) {
                elementValidate.classList.add('hide-element');
            }
            const data = {
                apartado: apartado,
                departamento: 'Boyacá',
                municipio: municipio
            };

            fetchGraph(data, 'containerDataBoyaca', 'imgDataBoyaca')
        }


    });

    //Fetch data de Cundinamarca
    document.getElementById('formDataCundinamarca').addEventListener('submit', function (event) {
        event.preventDefault();

        const apartado = document.getElementById('apartado-cundinamarca').value;
        const municipio = document.getElementById('municipios-cundinamarca').value;

        let elementValidate = document.getElementById('elementValidateCundinamarca');
        if (apartado === 'Seleccione una opción' || municipio === 'Seleccione una opción') {
            elementValidate.classList.remove('hide-element');
        } else {
            if (!elementValidate.classList.contains('hide-element')) {
                elementValidate.classList.add('hide-element');
            }
            const data = {
                apartado: apartado,
                departamento: 'Cundinamarca',
                municipio: municipio
            };
            fetchGraph(data, 'containerDataCundinamarca', 'imgDataCundinamarca')
        }

    });


    async function fetchGraph(data, idContainerImg, idImg) {

        await fetch('/dbGraph', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                const imgDataBoyaca = document.getElementById(idImg);
                console.log(imgDataBoyaca)
                if (imgDataBoyaca) {
                    imgDataBoyaca.remove();
                }
                const container = document.getElementById(idContainerImg);
                console.log(container)
                container.insertAdjacentHTML('afterbegin', `<img id='${idImg}' class="rounded mx-auto d-block img-fluid" src="${data.srcImage}?${new Date().getTime()}">`);
            })
            .catch((error) => {
                console.error('Error:', error);
            });

    }


})
