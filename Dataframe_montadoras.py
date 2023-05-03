import pandas as pd
import pymongo

data = {'Montadora' : ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
        'País' : ['EUA', 'Alemanhã', 'França', 'EUA', 'Japão']}

df = pd.DataFrame(data)
df


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['Avaliacao']

collection = db['Montadoras']
collection.insertOne(data)