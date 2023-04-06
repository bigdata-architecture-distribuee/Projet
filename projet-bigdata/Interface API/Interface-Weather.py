import pymongo
from pymongo import MongoClient
import tkinter as tk
from tkinter import ttk

# Connexion à la base de données MongoDB locale
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase_weather']
collection = db['openweather_collection']

# Récupérer toutes les données de MongoDB
data = collection.find()

# Fonction pour afficher les données dans le tableau
def show_data(data):
    for i, row in enumerate(data):
        country = row.get('Country')
        description = row.get('Description')
        temperature = row.get('Temperature (K)')
        pressure = row.get('Pressure (hPa)')
        humidity = row.get('Humidity (%)')
        wind_speed = row.get('Wind Speed (m/s)')

        table.insert('', 'end', iid=i, values=(country, description, temperature, pressure, humidity, wind_speed))

# Interface graphique Tkinter
root = tk.Tk()
root.title("Données MongoDB")

frame = ttk.Frame(root)
frame.pack()

# Créer un tableau avec des en-têtes de colonne
headers = ['Country', 'Description', 'Temperature (K)', 'Pressure (hPa)', 'Humidity (%)', 'Wind Speed (m/s)']
table = ttk.Treeview(frame, columns=headers, show='headings')
table.pack()

for header in headers:
    table.heading(header, text=header)

# Bouton pour afficher les données
button = tk.Button(root, text="Afficher les données", command=lambda: show_data(data))
button.pack()

root.mainloop()
