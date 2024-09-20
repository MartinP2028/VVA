import json
import joblib
import pandas as pd

# Charger le modèle
model = joblib.load('model.joblib')

# Charger les données
data = pd.read_csv("../vva_web/uploads/data_test.csv")
driver_names = data['driver_name'].tolist()

# Faire des prédictions avec le modèle
predictions = model.predict(data)

# Créer la liste des résultats avec conversion en float standard
result_final = []
for i in range(len(driver_names)):
    result = {
        "driver_name": driver_names[i],
        "prediction": float(predictions[i])  # Conversion explicite en float
    }
    result_final.append(result)

# Trier les résultats par la prédiction
sorted_result_final = sorted(result_final, key=lambda x: float(x["prediction"]))

# Définir le chemin où enregistrer le fichier JSON
output_path = "../vva_web/public/result.json"

# Sauvegarder dans un fichier JSON
with open(output_path, "w") as file:
    json.dump(sorted_result_final, file, indent=4)

print(f"Liste triée sauvegardée dans '{output_path}'.")
