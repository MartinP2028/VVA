from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import joblib
import pandas as pd
import os

app = FastAPI()

# Configurer CORS pour autoriser les requêtes depuis Nuxt.js (http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Origine autorisée (Nuxt.js)
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

@app.get("/api/drivers")
async def get_result():
    try:
        # Charger le modèle
        print("Chargement du modèle")
        model_path = os.path.abspath("model.joblib")
        if not os.path.exists(model_path):
            raise HTTPException(status_code=404, detail="Model file not found")
        
        model = joblib.load(model_path)
        print("Modèle chargé")

        # Charger les données
        print("Chargement des données")
        data_path = os.path.abspath("../vva_web/uploads/data_test2.csv")
        if not os.path.exists(data_path):
            raise HTTPException(status_code=404, detail="CSV file not found")

        data = pd.read_csv(data_path)
        print("Données chargées")

        driver_names = data['driver_name'].tolist()

        # Faire des prédictions
        print("Prédictions en cours")
        predictions = model.predict(data)
        print("Prédictions terminées")

        # Créer une liste des résultats
        result_final = []
        for i in range(len(driver_names)):
            result = {
                "driver_name": driver_names[i],
                "prediction": float(predictions[i])
            }
            result_final.append(result)

        # Trier les résultats par la prédiction
        sorted_result_final = sorted(result_final, key=lambda x: float(x["prediction"]))
        return sorted_result_final

    # Définir le chemin où enregistrer le fichier JSON
    #     print("Sauvegarde du fichier JSON")
    #     output_path = os.path.abspath("../vva_web/public/result.json")
    #     with open(output_path, "w") as file:
    #         json.dump(sorted_result_final, file, indent=4)
    #
    #     print(f"Liste triée sauvegardée dans '{output_path}'.")
    #     return sorted_result_final
    except Exception as e:
        print(f"Erreur: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))