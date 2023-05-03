# Import Libraries
import pandas as pd
from pymongo import MongoClient

# create dataframes
df_carros = pd.DataFrame({'carro': ['Onix', "Polo", "Sandero", "Fiesta", "City"], 
                         'cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'], 
                         'montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']})

df_montadoras = pd.DataFrame({'montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'], 'pais': ['EUA', 'Alemanha', 'Franca', 'EUA', 'Japao']})

# create connection with mongodb
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

#create spro_case db
db = client.spro_case

#create collections
col_carros = db['carros']
col_montadoras = db['montadoras']

# save dataframes on collections created
col_carros.insert_many(df_carros.to_dict('records'))
col_montadoras.insert_many(df_montadoras.to_dict('records'))

# close connection
db.close()