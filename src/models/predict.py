import pickle
from typing import List
import os
from src.features.tokenize import tokenize_classes

#Metodo para predecir el sentimiento de una frase
def predict(documents: List[str]):
    document_classes = {
        'UNK': documents
    }

    word_classes = tokenize_classes(document_classes)
    basePath = os.path.dirname(os.path.abspath(__file__))

    with open(basePath+'/../../models/model.pkl', 'rb') as input_file:
        model = pickle.load(input_file)

    document_words = word_classes['UNK']

    predictions = []
    for document in document_words:

        #Calculando las probabilidades de pertenecer a cada clase
        positive_prob = model['POS_PROB']
        negative_prob = model['NEG_PROB']
        for word in document:
            if word in model['COND_POS_PROBS']:
                positive_prob += model['COND_POS_PROBS'][word]['logprob']
            else:
                positive_prob += model['COND_POS_PROBS'][-1]['logprob']

            if word in model['COND_NEG_PROBS']:
                negative_prob += model['COND_NEG_PROBS'][word]['logprob']
            else:
                negative_prob += model['COND_NEG_PROBS'][-1]['logprob']

        #Determinando a que clase pertenece la oracion
        if positive_prob >= negative_prob:
            predictions.append('POS')
        else:
            predictions.append('NEG')

    return predictions
