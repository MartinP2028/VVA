import pandas as pd

# Charger le fichier CSV avec gestion des erreurs
try:
    df = pd.read_csv('weather.csv')
except FileNotFoundError:
    print("Le fichier 'weather.csv' est introuvable.")
    exit()

# Supprimer la colonne 'Time'
df = df.drop(columns=['Time'])

# Vérifier les valeurs uniques de la colonne 'Rainfall' avant conversion
print("Valeurs uniques de 'Rainfall' avant conversion :", df['Rainfall'].unique())

# Convertir la colonne 'Rainfall' en booléen (0 pour FAUX et 1 pour VRAI)
def convert_rainfall(value):
    if isinstance(value, str):
        return 1 if value.strip().upper() == 'VRAI' else 0
    elif isinstance(value, bool):
        return 1 if value else 0
    return 0

df['Rainfall'] = df['Rainfall'].apply(convert_rainfall)

# Vérifier les valeurs uniques après conversion
print("Valeurs uniques de 'Rainfall' après conversion :", df['Rainfall'].unique())

# Calculer le nombre total de jours et le nombre de jours de pluie pour chaque Grand Prix
rainfall_stats = df.groupby(['Year', 'Location'])['Rainfall'].agg(['count', 'sum']).reset_index()
rainfall_stats.rename(columns={'count': 'Total Days', 'sum': 'Rainy Days'}, inplace=True)

# Calculer le pourcentage de jours de pluie
rainfall_stats['Rainfall Percentage'] = (rainfall_stats['Rainy Days'] / rainfall_stats['Total Days']) * 100

# Conserver les colonnes numériques pour le calcul des moyennes
numeric_cols = df.select_dtypes(include='number').columns

# Calculer la moyenne des colonnes numériques par 'Year' et 'Location'
avg_weather_data = df.groupby(['Year', 'Location'], as_index=False)[numeric_cols].mean()

# Conserver les colonnes non numériques
non_numeric_cols = df.select_dtypes(exclude='number').columns

# Conserver la première occurrence des colonnes non numériques
first_non_numeric = df.groupby(['Year', 'Location'], as_index=False)[non_numeric_cols].first()

# Fusionner les moyennes numériques avec les premières valeurs des colonnes non numériques
final_df = pd.merge(avg_weather_data, first_non_numeric, on=['Year', 'Location'])

# Fusionner le pourcentage de jours de pluie avec les données finales
final_df = pd.merge(final_df, rainfall_stats[['Year', 'Location', 'Rainfall Percentage']], on=['Year', 'Location'])

# Sauvegarder le DataFrame final dans un fichier CSV
final_df.to_csv('average_weather_with_rain_percentage.csv', index=False)

# Message de confirmation
print("Les moyennes des données météorologiques, y compris le pourcentage de jours de pluie, ont été sauvegardées dans 'average_weather_with_rain_percentage.csv'.")
