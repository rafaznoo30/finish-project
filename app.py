from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import forms

plt.switch_backend('Agg')
app = Flask(__name__)


def dfDB(departamento, apartado):
    # Carga los archivos CSV seleccionando solo las columnas necesarias
    # Animales
    df = ''
    if departamento == 'Boyacá':

        if apartado == 'Animales':

            invEspecies = pd.read_csv('Data/Boyaca/animalesInvasoresEspeciesBoyaca.csv',
                                      usecols=['label_region', 'especies_invasoras'])
            invRegistros = pd.read_csv('Data/Boyaca/animalesInvasoresRegistrosBoyaca.csv',
                                       usecols=['registros_invasoras'])
            # rename(columns) ---> Cambia el nombre de la columna
            endEspecies = pd.read_csv('Data/Boyaca/animalesEndemicasEspeciesBoyaca.csv', usecols=['count']).rename(
                columns={'count': 'especies_endemicas'})
            endObservaciones = pd.read_csv('Data/Boyaca/animalesEndemicasObservacionesBoyaca.csv',
                                           usecols=['count']).rename(
                columns={'count': 'registros_endemicas'})
            exoEspecies = pd.read_csv('Data/Boyaca/animalesExoticasEspeciesBoyaca.csv', usecols=['especies_exoticas'])
            exoObservaciones = pd.read_csv('Data/Boyaca/animalesExoticasObservacionesBoyaca.csv',
                                           usecols=['registros_exoticas'])

            df = pd.concat([invEspecies, invRegistros, endEspecies, endObservaciones, exoEspecies, exoObservaciones],
                           axis=1)

        else:

            print('PLantas')

    elif departamento == 'Cundinamarca':

        print('Hola mundo')
        if apartado == 'Animales':
            print('cundinamarca animales')
        else:
            print('cundinamarca plantas')

    return df


def municipiosDB():
    municipiosBoyaca = pd.read_csv('Data/Boyaca/animalesInvasoresEspeciesBoyaca.csv',
                                   usecols=['label_region'])

    # Falta municipios de Cundinamarca
    return municipiosBoyaca['label_region'].tolist()


@app.route('/')
def test():
    municipiosBoyaca = municipiosDB()

    return render_template('index.html', municipiosBoyaca=municipiosBoyaca)


@app.route('/dataBoyaca', methods=['POST'])
def dataBoyaca():
    data = request.get_json()
    departamento = data['departamento']
    municipio = data['municipio']
    apartado = data['apartado']

    datos = dfDB(departamento, apartado)

    # Filtrar por el municipio de interés (en este caso, 'Almeida')
    datos = datos[datos['label_region'] == municipio]

    # Extraer datos para graficar
    especies = datos[['especies_invasoras', 'especies_endemicas', 'especies_exoticas']].iloc[0]
    registros = datos[['registros_invasoras', 'registros_endemicas', 'registros_exoticas']].iloc[0]

    # Configurar la gráfica de barras
    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.35  # Ancho de las barras
    index = range(len(especies))  # Índices para las barras

    # Graficar las barras
    bars1 = ax.bar(index, especies, bar_width, label='Especies')
    bars2 = ax.bar([i + bar_width for i in index], registros, bar_width, label='Registros')

    # Etiquetas y título
    ax.set_xlabel('Tipo de Especies')
    ax.set_ylabel('Cantidad')
    ax.set_title(f'Distribución de Especies y Registros en {municipio}')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(['Invasoras', 'Endémicas', 'Exóticas'])
    ax.legend()

    grafica = 'static/img/grafica.png'
    plt.savefig(grafica)
    plt.close()

    response = {
        'status': 'success',
        'srcImage': grafica
    }

    return jsonify(response)
