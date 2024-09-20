
---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- VVA-project2/autotrain-data
---

# Model Trained Using AutoTrain

- Problem type: Tabular regression

## Validation Metrics

- r2: 0.9202287197113037
- mse: 2.480766030974698
- mae: 1.1680808128312576
- rmse: 1.5750447711016655
- rmsle: 0.15227428737164778
- loss: 1.5750447711016655

## Best Params

- learning_rate: 0.1536315284792532
- reg_lambda: 0.18193248295021622
- reg_alpha: 6.60576691258007e-05
- subsample: 0.8676522947680911
- colsample_bytree: 0.6592590281734657
- max_depth: 4
- early_stopping_rounds: 265
- n_estimators: 7000
- eval_metric: rmse

## Usage

```python
import json
import joblib
import pandas as pd

model = joblib.load('model.joblib')
config = json.load(open('config.json'))

features = config['features']

# data = pd.read_csv("data.csv")
data = data[features]

predictions = model.predict(data)  # or model.predict_proba(data)

# predictions can be converted to original labels using label_encoders.pkl

```
