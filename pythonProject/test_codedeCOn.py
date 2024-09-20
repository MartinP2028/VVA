import pandas as pd
import os

# Fichiers à exclure et dossier contenant les CSV
files_to_exclude = ["lap_times.csv", "pit_stops.csv", "sprint_results.csv", "seasons.csv", "status.csv"]
csv_folder = "resources"
drivers_to_keep = [830, 815, 844, 832, 1, 847, 4, 840, 839, 842, 846, 857, 822, 855, 852, 817, 825, 807, 848, 858]

# Fonction pour charger et sélectionner les colonnes dans les CSV
def load_and_select_columns(file_name, key_columns, columns_to_keep=None):
    file_path = os.path.join(csv_folder, file_name)
    try:
        df = pd.read_csv(file_path)
        print(f"\nFichier {file_name} lu avec succès ({len(df)} lignes).")
        print(f"Colonnes dans {file_name} : {list(df.columns)}")

        if columns_to_keep:
            df = df[key_columns + columns_to_keep]
            print(f"Colonnes sélectionnées dans {file_name} : {key_columns + columns_to_keep}")
        else:
            df = df[key_columns]
            print(f"Colonnes clés sélectionnées dans {file_name} : {key_columns}")

        return df
    except Exception as e:
        print(f"Échec de traitement du fichier {file_name} : {e}")
        return pd.DataFrame()

# Traitement des différents fichiers CSV
def process_circuits():
    file_name = "circuits.csv"
    key_columns = ['circuitId']
    columns_to_keep = ['name', 'location']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

def process_drivers():
    file_name = "drivers.csv"
    key_columns = ['driverId']
    columns_to_keep = ['driverRef', 'code', 'forename', 'surname']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

def process_races():
    file_name = "races.csv"
    key_columns = ['raceId']
    columns_to_keep = ['year', 'round', 'circuitId', 'name', 'date']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

def process_results():
    file_name = "results.csv"
    key_columns = ['resultId', 'raceId', 'driverId']
    columns_to_keep = ['constructorId', 'grid', 'position', 'points']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

def process_constructors():
    file_name = "constructors.csv"
    key_columns = ['constructorId']
    columns_to_keep = ['name', 'nationality']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

def process_constructor_standings():
    file_name = "constructor_standings.csv"
    key_columns = ['constructorId']
    columns_to_keep = ['points', 'position', 'wins']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

def process_driver_standings():
    file_name = "driver_standings.csv"
    key_columns = ['driverId']
    columns_to_keep = ['points', 'position', 'wins']
    return load_and_select_columns(file_name, key_columns, columns_to_keep)

# Chargement des DataFrames
circuits_df = process_circuits()
drivers_df = process_drivers()
races_df = process_races()
results_df = process_results()
constructors_df = process_constructors()
constructor_standings_df = process_constructor_standings()
driver_standings_df = process_driver_standings()

print("\nDataFrames avant fusion :")
print("Circuits :\n", circuits_df.head())
print("Drivers :\n", drivers_df.head())
print("Races :\n", races_df.head())
print("Results :\n", results_df.head())
print("Constructors :\n", constructors_df.head())
print("Constructor Standings :\n", constructor_standings_df.head())
print("Driver Standings :\n", driver_standings_df.head())

# Fusion des DataFrames
try:
    merged_df = results_df.merge(drivers_df, on='driverId', how='left') \
        .merge(races_df, on='raceId', how='left') \
        .merge(circuits_df, on='circuitId', how='left') \
        .merge(constructors_df, on='constructorId', how='left') \
        .merge(constructor_standings_df, on='constructorId', how='left', suffixes=('', '_constructor')) \
        .merge(driver_standings_df, on='driverId', how='left', suffixes=('', '_driver'))

    print("Fusion des DataFrames réussie avec", len(merged_df), "lignes.")
except Exception as e:
    print(f"Échec de la fusion des DataFrames : {e}")
    merged_df = pd.DataFrame()

print("\nDataFrame fusionné :")
print(merged_df.head())

# Filtrage des drivers
try:
    if 'driverId' in merged_df.columns:
        merged_df = merged_df[merged_df['driverId'].isin(drivers_to_keep)]
        print(f"DataFrame filtré pour les drivers spécifiés. Lignes restantes : {len(merged_df)}")
except Exception as e:
    print(f"Échec du filtrage du DataFrame : {e}")

# Suppression des colonnes dupliquées
merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

print("\nDataFrame final :")
print(merged_df.head())

# Sauvegarde du DataFrame fusionné
try:
    output_file = os.path.join(csv_folder, "f1_datas.csv")
    merged_df.to_csv(output_file, index=False)
    print(f"DataFrame fusionné sauvegardé avec succès dans {output_file}")
except Exception as e:
    print(f"Échec de la sauvegarde du DataFrame fusionné : {e}")

# Sauvegarde de la sauvegarde de secours
try:
    merged_df.to_csv("f1_datas_backup.csv", index=False)
    print("DataFrame fusionné sauvegardé dans f1_datas_backup.csv dans le répertoire courant.")
except Exception as e:
    print(f"Échec de la sauvegarde de secours du DataFrame : {e}")
