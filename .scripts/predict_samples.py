import joblib
import numpy as np
import pandas as pd

model = joblib.load('models/crop_rf_model.pkl')
le = joblib.load('models/label_encoder.pkl')

FEATURE_NAMES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

samples = [
    [50,50,50,25,70,6.5,150],  # default
    [10,20,10,30,80,6.0,200],  # wetter/higher humidity
    [120,80,60,35,40,7.5,50],  # hot/dry
]

for i,s in enumerate(samples,1):
    probs = model.predict_proba(pd.DataFrame([s], columns=FEATURE_NAMES))[0]
    classes = le.inverse_transform(model.classes_)
    top = sorted(zip(classes, probs*100), key=lambda x:-x[1])[:3]
    print(f"Sample {i}: {s}")
    for rank,(c,p) in enumerate(top,1):
        print(f"  {rank}. {c}: {p:.2f}%")
    print('')
