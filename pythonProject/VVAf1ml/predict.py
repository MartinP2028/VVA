import json
import joblib
import pandas as pd

model = joblib.load('model.joblib')
data = pd.read_csv("data.csv")
driver_names = data['driver'].tolist()
predictions = model.predict(data)
result_final = []
for i in range(len(driver_names)):
    result = driver_names[i] + ": " + str(predictions[i])
    result_final.append(result)
sorted_result_final = sorted(result_final, key=lambda x: float(x.split(": ")[1]))
print(sorted_result_final)
