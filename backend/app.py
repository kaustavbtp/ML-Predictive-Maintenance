from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load the model
model = pickle.load(open('model.pk26', 'rb'))

class Item(BaseModel):
    voltage: int
    runtime: int
    speed: int
    vibration: int
    weight: int
    temperature: int

@app.post("/predict")
def predict(item: Item):
    try:
        int_features = [item.voltage, item.runtime, item.speed, item.vibration, item.weight, item.temperature]
        final = [np.array(int_features)]
        prediction = model.predict_proba(final)
        output = '{0:.2f}'.format(prediction[0][1])

        if float(output) > 0.5:
            return {"message": f"Machine | Motor MC1 is in Danger! Probability of failure/downtime is {output}"}
        else:
            return {"message": f"Machine | Motor MC1 is safe. Probability of failure/downtime is {output}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))