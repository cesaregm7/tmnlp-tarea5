from typing import List, Tuple

from gensim.corpora import Dictionary

#Metodo para crear un diccionario
def create_dictionary(documents: List[List[str]]):
    return Dictionary(documents)

#Metodo para crear el term document matrix
def term_document_matrix(documents, dictionary: Dictionary) -> List[List[Tuple[int, int]]]:
    return [dictionary.doc2bow(text) for text in documents]