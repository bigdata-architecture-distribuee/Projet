import pymongo
from pymongo import MongoClient
import tkinter as tk
from tkinter import ttk

# Connexion à la base de données MongoDB locale
client = MongoClient('mongodb://localhost:27017/')
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

# Fonction pour afficher les données dans le tableau
def show_data(data):
    for i, row in enumerate(data):
        country = row.get('_id')
        count = row.get('count')

        table.insert('', 'end', iid=i, values=(country, count))

# Interface graphique Tkinter
root = tk.Tk()
root.title("Données MongoDB")

frame = ttk.Frame(root)
frame.pack()

# Créer un tableau avec des en-têtes de colonne
headers = ['Country', 'Total']
table = ttk.Treeview(frame, columns=headers, show='headings')
table.pack()

for header in headers:
    table.heading(header, text=header)

# Bouton pour afficher les données
button = tk.Button(root, text="Afficher les données", command=lambda: show_data(data))
button.pack()

root.mainloop()
