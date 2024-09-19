import pandas as pd

# Read weather
df_weather = pd.read_csv('resources/weather.csv', sep=';')

# Read final F1 DataFrame
df_final = pd.read_csv('f1_datas.csv')

# Filter columns
df_weather = df_weather.rename(columns={'Location': 'circuit_name', 'Year': 'year'})

# Merge DataFrames
df_weather_f1 = pd.merge(df_final, df_weather, on=['circuit_name', 'year'], how='left')

# Save combined DataFrames to CSV
print(df_weather_f1.info())
output_file = "combined_weather_f1_datas.csv"
df_weather_f1.to_csv(output_file, index=False)
print(f"Successfully saved final dataframe to {output_file}")
