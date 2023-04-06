import pymongo
from pymongo import MongoClient
import tkinter as tk
from tkinter import ttk

# Connexion à la base de données MongoDB locale
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase_weather']

openweather_collection = db['openweather_collection']
opensky_collection = db['opensky_collection']
waqi_collection = db['waqi_collection']

# Pipeline d'agrégation pour regrouper par pays et compter le nombre d'occurrences
opensky_pipeline = [
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

waqi_pipeline = [
    {
        "$group": {
            "_id": "$country",
            "avg_aqi": {"$avg": "$aqi"},
        }
    },
    {
        "$sort": {
            "_id": 1
        }
    }
]

# Récupérer les données agrégées de MongoDB
openweather_data = {row['Country']: row for row in openweather_collection.find()}
opensky_data = {row['_id']: row['count'] for row in opensky_collection.aggregate(opensky_pipeline)}
waqi_data = {row['_id']: row['avg_aqi'] for row in waqi_collection.aggregate(waqi_pipeline)}

all_countries = set(openweather_data) | set(opensky_data) | set(waqi_data)

# Fusionner les données des collections
merged_data = []

for country in sorted(all_countries):
    ow_row = openweather_data.get(country, {})
    description = ow_row.get('Description', '')
    temperature = ow_row.get('Temperature (K)', '')
    pressure = ow_row.get('Pressure (hPa)', '')
    humidity = ow_row.get('Humidity (%)', '')
    wind_speed = ow_row.get('Wind Speed (m/s)', '')

    total = opensky_data.get(country, '')
    avg_aqi = waqi_data.get(country, '')

    # Vérifier si la ligne est vide en comparant les données aux chaînes vides
    if description or temperature or pressure or humidity or wind_speed or total or avg_aqi:
        merged_data.append((country, description, temperature, pressure, humidity, wind_speed, total, avg_aqi))

# Interface graphique Tkinter
root = tk.Tk()
root.title("Données MongoDB")

frame = ttk.Frame(root)
frame.pack()

# Créer un tableau avec des en-têtes de colonne
headers = ['Country', 'Description', 'Temperature (K)', 'Pressure (hPa)', 'Humidity (%)', 'Wind Speed (m/s)', 'Total', 'AQI']
table = ttk.Treeview(frame, columns=headers, show='headings')
table.pack()

for header in headers:
    table.heading(header, text=header)

# Fonction pour afficher les données dans le tableau
def show_data():
    table.delete(*table.get_children())
    for i, row in enumerate(merged_data):
        table.insert('', 'end', iid=i, values=row)

# Bouton pour afficher les données
button = tk.Button(root, text="Afficher les données", command=show_data)
button.pack()

# Charger les données lors du lancement de l'application
show_data()

root.mainloop()
