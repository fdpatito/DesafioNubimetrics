import json
import requests
import pandas as pd
from os import mkdir,makedirs, getcwd
from datetime import date as dt


site_id = "MLA"
category_id = "MLA1144"
current_dir = getcwd()
fecha = dt.today().strftime("%Y/%m/%d")

# Desafio 2
# Obtengo los datos de la API
r = requests.get(f"https://api.mercadolibre.com/sites/{site_id}/search?category={category_id}")
json_data = r.json()
json_folder = ''.join(["search","json",fecha.split('/')[0], fecha.split('/')[1]])
json_name = '/'.join([current_dir, json_folder, "data.json"])

# Creo la carpeta para el archivo
try:
    mkdir(json_folder)
except:
    pass

# Guardo los datos obtenidos en un archivo JSON
with open(json_name, 'w+') as outputfile:
    json.dump(json_data, outputfile)

# Desafio 3
# Obtengo los datos del archivo creado anteriormente
with open(json_name, "r") as f:
    json_file = json.load(f)

# Extraigo y guardo los datos que se necesitan en un dataframe
df = pd.DataFrame(json_file["results"])

# Genero el arbol de directorios y creo el archivo final
folders_tree = '/'.join([site_id, fecha]) 
csv_name = '/'.join([folders_tree, "data.csv"])

try:
    makedirs(folders_tree)
except FileExistsError:
    pass

df.to_csv(csv_name)