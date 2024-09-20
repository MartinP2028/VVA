import pandas as pd
from datetime import datetime

# Charger le fichier CSV
df = pd.read_csv('races.csv')

# Obtenir l'année actuelle
current_year = datetime.now().year

# Filtrer les lignes où la colonne "year" est entre 2018 et l'année actuelle
df_filtered = df[(df['year'] >= 2018) & (df['year'] <= current_year)]

# Sauvegarder le DataFrame filtré dans un nouveau fichier CSV
df_filtered.to_csv('race_filtered.csv', index=False)
