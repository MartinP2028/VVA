import pandas as pd

# Liste des driverId à garder
drivers_to_keep = [830, 815, 844, 832, 1, 847, 4, 840, 839, 842, 846, 857, 822, 855, 852, 817, 825, 807, 848, 858]

# Read Driver
df_drive = pd.read_csv('resources/drivers.csv')

# Read Constructor
df_const = pd.read_csv('resources/constructors.csv')
df_const_result = pd.read_csv('resources/constructor_results.csv')

# Read Race
df_race = pd.read_csv('resources/races.csv')
df_status = pd.read_csv('resources/status.csv')
df_results = pd.read_csv('resources/results.csv')

# Filter columns and rows

# Drivers
df_drive = df_drive[['driverId', 'driverRef', 'number', 'surname', 'nationality']]
df_drive_filtered = df_drive[df_drive['driverId'].isin(drivers_to_keep)]

# Constructors
df_const_final = pd.merge(df_const_result, df_const, on='constructorId', how='left')
df_const_final = df_const_final[['raceId', 'constructorId', 'points', 'status', 'name', 'nationality']]
df_const_final = df_const_final.rename(columns={"name": "const_name", "nationality": "const_nationality", "points": "const_points"})
print(df_const_final.head())

# Race
df_results_merged = pd.merge(df_status, df_results, on='statusId', how='inner')
df_results = df_results.drop(columns=['statusId'])

df_race = df_race[['raceId', 'circuitId', 'name', 'round', 'date', 'year']]
filtered_race = df_race.loc[(df_race['year'] >= 2018)]

df_race_final = pd.merge(filtered_race, df_results_merged, on='raceId', how='inner')
df_race_final = df_race_final[['raceId', 'year', 'round', 'circuitId', 'name', 'date', 'status',
       'resultId', 'driverId', 'constructorId', 'number', 'grid', 'position',
       'positionOrder', 'points', 'laps', 'time',
       'milliseconds', 'fastestLap', 'rank', 'fastestLapTime',
       'fastestLapSpeed']]

df_driver = pd.merge(df_drive_filtered, df_race_final, on='driverId', how='inner')
df_intermediate = df_driver[['surname', 'nationality', 'constructorId',
                       'year', 'round', 'circuitId', 'name', 'date', 'status', 'grid', 'position',
                       'positionOrder', 'points', 'laps', 'time', 'fastestLap',
                       'rank', 'fastestLapTime', 'fastestLapSpeed']]

# Create final DataFrame
df_final =  pd.merge(df_intermediate, df_const_final[['constructorId','const_name', 'const_nationality']], on='constructorId', how='left')
df_final = df_final.drop(columns=['constructorId', 'circuitId', 'position'])
df_final = df_final.rename(columns={'surname': 'driver_name', 'nationality': 'driver_nationality', 'name': 'circuit_name', 'date': 'race_date', 'grid': 'grid_pos', 'positionOrder': 'finish_order_pos', 'points': 'points_finish', 'time': 'total_time', 'rank': 'rank_fastest_lap_time'})

# Drop duplicates
df_final.drop_duplicates(inplace=True)

# Save final DataFrame to CSV
print(df_final.head())
output_file = "f1_datas.csv"
df_final.to_csv(output_file, index=False)
print(f"Successfully saved final dataframe to {output_file}")
