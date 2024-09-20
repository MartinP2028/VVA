
---
tags:
- autotrain
- tabular
- regression
- tabular-regression
datasets:
- VVA-project/autotrain-data
---

# Model Trained Using AutoTrain

- Problem type: Tabular regression

## Validation Metrics

- r2: 0.8879646062850952
- mse: 3.484130141890152
- mae: 1.5436409577380779
- rmse: 1.8665824765839178
- rmsle: 0.29089951221255994
- loss: 1.8665824765839178

## Best Params

- learning_rate: 0.16660332992939494
- reg_lambda: 0.002215423910583248
- reg_alpha: 0.38257669800423344
- subsample: 0.4058395025585836
- colsample_bytree: 0.14699403254736293
- max_depth: 2
- early_stopping_rounds: 119
- n_estimators: 20000
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
