import spacy


def named_entities(document):
    """
    Receive a document and returns a list of tuples with (text, label)
    """
    return [(ent.text, ent.label_) for ent in document.ents]


if __name__ == '__main__':
    nlp = spacy.load('es_core_news_sm')
    doc = nlp('Ella comió pizza')

    for token in doc:
        # _ to return String value
        print(token.text, token.pos_, token.dep_, token.head)

        # pos_ : Part of Speech -> Job of the word in the sentence
        # dep_ : syntactic dependency
        # head : father token

    doc = nlp(
        "Apple es la marca que más satisfacción genera en EE.UU., "
        "pero el iPhone, fue superado por el Galaxy Note 9"
    )

    print(named_entities(doc))

    # spacy.explain examples -> label definitions
    # glossary.py -> GLOSSARY

    print(spacy.explain('ORG'))
    print(spacy.explain('LOC'))
    print(spacy.explain('MISC'))
    print(spacy.explain('NNP'))
    print(spacy.explain('VERB'))
