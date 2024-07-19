from fastapi import FastAPI, Body
from model import Carolina


MODEL_PRETRAINED_PATH = "./bloom-fine-tuned"

app = FastAPI()
model = Carolina(MODEL_PRETRAINED_PATH)


@app.get("/")
def greet_json()->None:
    return "Hello from Carolina"

@app.post("/classify")
def classify_text(input:str=Body(...))->None:
    return model.predict(input)
