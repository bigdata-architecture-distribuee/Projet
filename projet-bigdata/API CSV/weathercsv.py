import pymongo
from pymongo import MongoClient
import csv
import tkinter as tk
from tkinter import filedialog

# Connexion à la base de données MongoDB locale
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase_weather']
collection = db['openweather_collection']

# Récupérer toutes les données de MongoDB
data = collection.find()

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
    writer.writerow(['Country', 'Description', 'Temperature (K)', 'Pressure (hPa)', 'Humidity (%)', 'Wind Speed (m/s)'])
    for row in data:
        country = row.get('Country')
        description = row.get('Description')
        temperature = row.get('Temperature (K)')
        pressure = row.get('Pressure (hPa)')
        humidity = row.get('Humidity (%)')
        wind_speed = row.get('Wind Speed (m/s)')

        writer.writerow([country, description, temperature, pressure, humidity, wind_speed])

print(f"Le fichier CSV a été créé avec succès : {file_path}.")
