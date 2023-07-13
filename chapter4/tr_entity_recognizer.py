import random

import spacy
from spacy.tokens import Span


if __name__ == '__main__':
    # Text with entities
    nlp = spacy.load('es_core_news_sm')
    doc = nlp('Los nuevos adidas ZX vienen en camino')
    doc.ents = [Span(doc, 2, 4, "ROPA")]

    # Text without entities
    doc = nlp('Necesito nuevas zapatillas! ¿Qué me recomiendan?')
    doc.ents = []  # entities is empty

    nlp = spacy.blank('es')
    doc = nlp('el iPhone X está por salir y va a ser un desastre, como todos')
    doc.ents = [Span(doc, 1, 3, 'GADGET')]

    doc2 = nlp('¡Necesito un nuevo teléfono! ¿Alguien tiene recomendaciones?')

    # Creating a collection of documents -> we need hundred of thousands
    docs = [doc, doc2]

    # We need to divide (50/50) the examples into training and developing
    random.shuffle(docs)
    train_docs = docs[:len(docs) // 2]  # floor division
    dev_docs = docs[len(docs) // 2:]



