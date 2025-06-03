from fastapi import FastAPI, Body
from model import AdsMod


MODEL_PRETRAINED_PATH = "venishpatidar/wa-ad-mod"

app = FastAPI()
model = AdsMod(MODEL_PRETRAINED_PATH)


@app.get("/")
def greet_json()->None:
    return "Hello from Ad-Mod"

@app.post("/classify")
def classify_text(input:str=Body(...))->None:
    return model.predict(input)
