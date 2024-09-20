import fastf1
import pandas as pd
import logging

logging.getLogger('fastf1').setLevel(logging.CRITICAL)  # Supprimer les logs de fastf1

# Listes des années et du nombre de courses par année
years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
num_races = [22, 22, 18, 22, 23, 23, 12]

# Initialiser un DataFrame vide pour les données météorologiques
weather = pd.DataFrame()

# Parcourir chaque année et le nombre de courses correspondant
for year, num_race in zip(years, num_races):
    # Initialiser un DataFrame vide pour chaque année
    df = pd.DataFrame()

    # Obtenir les données de course pour chaque tour
    for x in range(1, num_race + 1):  # Ajouter +1 pour inclure la dernière course
        try:
            race_session = fastf1.get_session(year, x, 'R').event
            df = pd.concat([df, pd.DataFrame([race_session])], ignore_index=True)
        except Exception as e:
            print(f"Erreur lors de la récupération des données pour le tour {x} de l'année {year}: {e}")

    # Obtenir les données météorologiques pour chaque course
    for index, row in df.iterrows():
        track = row['Location']
        try:
            race_session = fastf1.get_session(year, track, 'R')
            race_session.load()  # Charger les données avant d'y accéder
            weather_data = race_session.weather_data
            round_number = row['RoundNumber']
            weather_data['Round Number'] = round_number
            weather_data['Year'] = year
            weather = pd.concat([weather, weather_data])
            print(f"{track}, Année : {year}")
        except Exception as e:
            print(f"Erreur lors de la récupération des données météorologiques pour {track} - {year}: {e}")

# Calculer les moyennes des données météorologiques par Grand Prix
avg_weather_data = weather.groupby(['Year', 'Location']).mean().reset_index()

# Sauvegarder les données météorologiques moyennes dans un fichier CSV unique
avg_weather_data.to_csv('average_weather_data_2018_2023.csv', index=False, encoding='utf-8')

# Message de réussite
print("Les moyennes des données météorologiques ont été sauvegardées dans 'average_weather_data_2018_2023.csv'.")
