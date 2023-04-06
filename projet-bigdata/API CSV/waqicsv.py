import pymongo
import csv
import tkinter as tk
from tkinter import filedialog

# Connexion à la base de données MongoDB locale
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase_weather']
collection = db['waqi_collection']

# Pipeline d'agrégation pour regrouper par pays et calculer la moyenne de AQI
pipeline = [
    {
        "$group": {
            "_id": "$country",
            "avg_aqi": {"$avg": "$aqi"}
        }
    },
    {
        "$sort": {
            "_id": 1
        }
    }
]

# Récupérer les données agrégées de MongoDB
data = list(collection.aggregate(pipeline))

# Interface graphique Tkinter pour sélectionner l'emplacement et le nom du fichier CSV de sortie
root = tk.Tk()
root.withdraw()

file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichier CSV", "*.csv")])
if file_path == "":
    print("Annulation de l'exportation.")
    exit()

# Écrire les données dans le fichier CSV
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Country', 'AQI'])
    for row in data:
        writer.writerow([row['_id'], row['avg_aqi']])

print(f"Le fichier CSV a été créé avec succès : {file_path}.")

# Télécharger le fichier CSV
root = tk.Tk()
root.withdraw()

# Ouvrir le fichier en mode lecture binaire pour le télécharger correctement
with open(file_path, mode='rb') as file:
    content = file.read()

download_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichier CSV", "*.csv")])
if download_path == "":
    print("Annulation du téléchargement.")
    exit()

with open(download_path, mode='wb') as file:
    file.write(content)

print(f"Le fichier CSV a été téléchargé avec succès : {download_path}.")
