import json

import pymongo
from bson.son import SON

line_divider = "#############################################"

conexoes_json = open('connections.json').read()
conexoes = json.loads(conexoes_json)

mongoclient = pymongo.MongoClient(conexoes["DbConnection"])
database = mongoclient["ovni"]
collection = database["ovnis"]

# 1. Contar e mostrar quantos documentos há na coleção ovnis.
print(collection.count_documents({}))

print(line_divider)

# 2. Resgatar todos os documentos (registros) da coleção ovnis e ordenar por tipo (shape).
todosDocumentos = collection.find(sort=[("Shape", pymongo.ASCENDING)])
#print(list(todosDocumentos))

print(line_divider)
# 3. Verificar quantas ocorrências existem por estado.
docsAgrupados = collection.aggregate([
    {"$unwind": "$State"},
    {"$group": {"Views": {"$sum": 1}, "_id": "$State"}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
])
#print(list(docsAgrupados))

print(line_divider)

# 4. Buscar todas as ocorrências da cidade Phoenix
docsPhoenix = collection.find(filter={'City': 'Phoenix'})
#print(list(docsPhoenix))

print(line_divider)


# 5. Buscar as ocorrências do estado da Califórnia e ocultar o id de cada documento (registro)
docsPhoenix = collection.find(filter={'State': 'CA'}, projection={'_id': False})
print(list(docsPhoenix))
