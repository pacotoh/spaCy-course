import spacy
from spacy import Language
from spacy.tokens import Doc, Token


def get_is_color(token: Token):
    colors = ['rojo', 'amarillo', 'azul']
    return token.text in colors


def contains(doc: Doc, word: str) -> bool:
    return word in [t.text for t in doc]


def is_palindrom(token: Token) -> bool:
    return token.text == token.text[::-1]


def get_wikipedia_url(span) -> str:
    """
    Check the span label in PER, ORG, LOC to know if the wikipedia article speaks about entities
    :param span: text to search as a wikipedia article
    :return: wikipedia url if its an entity or search page if not
    """
    if span.label_ not in ("PER", "ORG", "LOC"):
        return ''

    entity_text = span.text.replace(" ", "_")
    return "https://es.wikipedia.org/w/index.php?search=" + entity_text


def test_is_color_attr(doc):
    # attr extension
    Token.set_extension('is_color_test', default=False)
    doc[2]._.is_color_test = True

    [print(token._.is_color_test) for token in doc]

    # Only is_color = True for doc, not for other docs
    doc2: Doc = nlp('Eres un perro azul oscuro')
    [print(token._.is_color_test) for token in doc2]


if __name__ == '__main__':
    nlp: Language = spacy.blank('es')

    # doc: Doc = nlp('Hola mundo azul')
    # Doc.set_extension('title', default=None)
    # doc._.title = 'saludo'

    Token.set_extension('is_color', getter=get_is_color)

    doc = nlp('El cielo es azul')
    [print(token.text, token._.is_color) for token in doc]

    Doc.set_extension('contains', method=contains)

    print(doc._.contains('cielo'))
    print(doc._.contains('tierra'))

    # Palindrom test
    Token.set_extension('palindrom', getter=is_palindrom)

    doc2 = nlp('El oso es hermoso como ese animal que tiene dos de cada ojo')

    [print(token.text, token._.palindrom) for token in doc2]
