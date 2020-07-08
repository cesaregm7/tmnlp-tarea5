from typing import List

from fastapi import FastAPI, Query

from src.models.train import train
from src.models.predict import predict

#Creando el app de FastAPI
app = FastAPI()

#Metodo para entrenar el modelo
@app.post('/train')
async def train_model():
    train()
    return {'Result': 'model.pkl produced'}

#Metodo para predecir el sentimiento de un review basado en el modelo entrenado
@app.get('/predict')
async def predict_review(sentences: List[str] = Query(..., description='Sentences to process')):
    predictions = predict(sentences)
    response = [
        {
            'id': idx + 1,
            'sentence': sentence,
            'prediction': sentiment
        }
        for idx, (sentence, sentiment) in enumerate(zip(sentences, predictions))
    ]
    return response
