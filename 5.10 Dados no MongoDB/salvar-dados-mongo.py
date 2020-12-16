import csv
import json

import pandas
import pymongo

conexoes_json = open('connections.json').read()
conexoes = json.loads(conexoes_json)

mongoclient = pymongo.MongoClient(conexoes["DbConnection"])
database = mongoclient["ovni"]
collection = database["ovnis"]
        
def csv_to_dict():
    header = [ "City", "State", "Shape", "sight_Date", "sight_Time", "sight_Weekdays", "sight_Day", "sight_Month" ]
    with open('.\\df_OVNI_preparado.csv', mode="r", encoding="utf-8-sig") as csv_file:    
        reader = csv.DictReader(csv_file)
        result = []
        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]
            result.append(row)    
        return result

dicionario_dados = csv_to_dict()
collection.insert_many(dicionario_dados)

print('Dados inseridos com sucesso 🎆')


