import pandas as pd
import pymongo


data = {'Carro' : ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
        'Cor' : ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
        'Montadora' : ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']}

df = pd.DataFrame(data)
df


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['Avaliacao']

