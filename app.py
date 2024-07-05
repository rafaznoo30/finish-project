from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)


def dbBoyaca():
    print('-----> Data de Boyaca')
    datos = pd.read_csv('BoyacaDB.csv', sep=',')
    return datos

def dbCundinamarca():
    print('-----> Data de Cundinamarca')
    return True


@app.route('/')
def test():
    datos = dbBoyaca()
    print(datos.head())
    return render_template('index.html')


@app.route('/data/boyaca')
def dataBoyaca():
    datos = dbBoyaca()


@app.route('/data/cundinamarca')
def dataCundinamarca():
    datos = dbBoyaca()

