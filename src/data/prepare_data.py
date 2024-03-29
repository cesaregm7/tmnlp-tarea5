import enum
from typing import Dict, List
import os
import pandas as pd
from pandas import DataFrame

#Definiendo las clases de sentimientos a utilizar
class Sentiments(enum.Enum):
    POS = 'POS'
    NEG = 'NEG'

#Metodo para leer la muestra de los datos
def read_sample() -> DataFrame:
    basePath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(basePath+'/../../data/raw/reviews.csv')
    df['rating'] = df['rating'].astype(dtype='int64')
    return df

#Metodo para crear las clases de los reviews basado en el rating
def create_classes(df: DataFrame) -> Dict[str, List[str]]:
    df['sentiment'] = df['rating'].apply(lambda x: Sentiments.POS if x>=40 else Sentiments.NEG)
    review_classes = {
        sentiment.value: df[df['sentiment'] == sentiment]['review'].values.tolist()
        for sentiment in Sentiments
    }
    return review_classes
