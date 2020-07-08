import pickle
from typing import Generator, List
import os
from gensim.models import Phrases
from gensim.models.phrases import Phraser
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from spacy.lang.en import English
import re
from langdetect import detect,DetectorFactory

#Funcion para realizar data cleaning
def clean_data(data : List[str]) -> List:
    # Eliminar emails
    datos = [re.sub(r'\S*@\S*\s?', '', sent) for sent in data]

    # Eliminar newlines
    datos = [re.sub(r'\s+', ' ', sent) for sent in datos]

    # Eliminar comillas
    datos = [re.sub(r"\'", "", sent) for sent in datos]

    # Eliminar datos que no esten en ingles
    DetectorFactory.seed = 0
    datos = [sent for sent in datos if detect(sent)=='en']
    
    return datos

#Metodo para transformar oraciones a palabras
def sentences_to_words(sentences: List[str]) -> Generator:
    for sentence in sentences:
        yield(simple_preprocess(str(sentence), deacc=True))  # deacc=True elimina la puntuación

#Metodo para eliminar stopwords
def remove_stopwords(documents: List[List[str]]) -> List[List[str]]:
    return [[word for word in simple_preprocess(str(doc)) if word not in stopwords.words('english')]
            for doc in documents]

#Metodo para crear un modelo de bigrams
def bigrams_model(documents: List[List[str]], save: bool = False) -> Phraser:
    # We learn bigrams
    bigram = Phrases(documents, min_count=5, threshold=10)

    # we reduce the bigram model to its minimal functionality
    bigram_mod = Phraser(bigram)
    basePath = os.path.dirname(os.path.abspath(__file__))
    if save:
        with open(basePath+'/../../models/bigrams.pkl', 'wb') as output_file:
            pickle.dump(bigram_mod, output_file)

    return bigram_mod

#Metodo para aplicar el modelo de bigrams a nuestros documentos
def extend_bigrams(documents: List[List[str]], bigram_mod: Phraser) -> List[List[str]]:
    # we apply the bigram model to our documents
    return [bigram_mod[doc] for doc in documents]

#Metodo para realizar lematizacion
def lemmatization(nlp: English, texts: List[List[str]], allowed_postags: List = None) -> List[List[str]]:
    if allowed_postags is None:
        allowed_postags = ['NOUN', 'ADJ', 'VERB', 'ADV']

    """https://spacy.io/api/annotation"""
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out