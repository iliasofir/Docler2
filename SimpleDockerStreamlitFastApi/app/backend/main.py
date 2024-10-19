from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Initialize FastAPI app
app = FastAPI()

# Hugging Face API information
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-xlm-roberta-base-sentiment"
headers = {"Authorization": "Bearer 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"}

# Define a Pydantic model to parse incoming JSON data
class InputData(BaseModel):
    input_text: str

# Helper function to query Hugging Face API
def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Define FastAPI endpoints
@app.get("/")
async def read_root():
    return {"message": "Welcome to the model API!"}

@app.post("/predict/")
async def predict_sentiment(input_data: InputData):
    # Prepare the input for Hugging Face model
    payload = {"inputs": input_data.input_text}
    
    # Query the Hugging Face API
    response = query_huggingface(payload)
    
    # Process the response and return the result
    return {"result": response}