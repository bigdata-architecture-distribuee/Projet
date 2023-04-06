import pymongo
import csv
import tkinter as tk
from tkinter import filedialog

# Connexion à la base de données MongoDB locale
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase_weather']
collection = db['opensky_collection']

# Pipeline d'agrégation pour regrouper par pays et compter le nombre d'occurrences
pipeline = [
    {
        "$group": {
            "_id": "$Country",
            "count": {"$sum": 1}
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
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country', 'Total'])
    for row in data:
        writer.writerow([row['_id'], row['count']])

print(f"Le fichier CSV a été créé avec succès : {file_path}.")