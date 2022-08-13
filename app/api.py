import uvicorn
import pandas as pd
from fastapi import FastAPI, Response
from joblib import load
from .schemas import Features, FraudLabel
from os.path import dirname, abspath

APP_ROOT_DIR  = dirname(dirname(abspath(__file__)))
model = load(APP_ROOT_DIR +"/artifacts/model.pkl")
app = FastAPI()

@app.get("/")
async def root():
    return "ML inference server run by fastAPI"

@app.post("/predict",response_model=FraudLabel)
async def predict(response: Response, payload:Features):
    payload_dict = payload.dict()
    payload_df = pd.DataFrame([payload_dict])
    prediction = model.predict(payload_df)[0]
    response.headers["X-model-score"] = str(prediction)
    return FraudLabel(label=prediction)

@app.get("/ping")
async def healthcheck():
    return {"status": "ok","server":"1"}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=5004, reload=True)
