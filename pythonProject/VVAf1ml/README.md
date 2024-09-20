
---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- VVAf1ml/autotrain-data
---

# Model Trained Using AutoTrain

- Problem type: Tabular regression

## Validation Metrics

- r2: 0.6605597947084276
- mse: 10.431591346843176
- mae: 2.210354051688749
- rmse: 3.2297974157589473
- rmsle: 0.5250779681406293
- loss: 3.2297974157589473

## Best Params

- learning_rate: 0.07216524091934186
- reg_lambda: 0.00011448282142191567
- reg_alpha: 0.03861097279592124
- subsample: 0.7076221003508524
- colsample_bytree: 0.8368089440827335
- max_depth: 4
- early_stopping_rounds: 383
- n_estimators: 15000
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
