import pandas as pd
import json
from flask import Flask, jsonify
from pandas.core.indexes.api import _new_Index

app = Flask(__name__)

tabela = pd.read_csv('teste_oport.csv')
tb_data = tabela.to_json(orient='records')
tb_json = json.loads(tb_data)


@app.route('/')
def home():
    return 'A API está no ar'


@app.route('/characters')
def characters():
    return tb_json


@app.route('/characters/<int:id>')
def characters_id(id):
    new_id = id - 1
    return tb_json[new_id]


app.run(host='0.0.0.0')
