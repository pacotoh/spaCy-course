import spacy
from spacy.tokens import Doc, DocBin, Span
import random


def create_corpus(docs: list[Doc], prop: int) -> tuple[DocBin, DocBin]:
    """
    Creates a corpus from a list of Doc and the proportional division for train and dev
    :param docs: list of spacy documents that creates a Corpus
    :param prop: proportional value to divide train and dev examples
    :return: a tuple that represents train and dev DocBin created from docs
    """
    random.shuffle(docs)
    train_docs = docs[:len(docs) // prop]  # floor division
    dev_docs = docs[len(docs) // prop:]

    train_docbin = DocBin(docs=train_docs)
    train_docbin.to_disk("./files/train.spacy")

    dev_docbin = DocBin(docs=dev_docs)
    dev_docbin.to_disk("./files/dev.spacy")
    return train_docbin, dev_docbin

# TODO: create load_corpus function


if __name__ == '__main__':
    nlp = spacy.blank('es')
    doc = nlp('el iPhone X está por salir y va a ser un desastre, como todos')
    doc.ents = [Span(doc, 1, 3, 'GADGET')]

    doc2 = nlp('¡Necesito un nuevo teléfono! ¿Alguien tiene recomendaciones?')

    # Creating a collection of documents
    docs = [doc, doc2]

    train_docbin, dev_docbin = create_corpus(docs, 2)

    print(train_docbin.tokens)
    print(dev_docbin.tokens)
