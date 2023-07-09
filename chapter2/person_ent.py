import spacy
from spacy.tokens import Doc, Span


def get_spaces(string: str) -> list:
    """
    FIXME:
    Method to obtain an array of Boolean values with spaces info between words. True value indicates that exists space
    between two words; False value indicates that doesn't exist space.
    :param string: text to obtain spaces info
    :return: a list with Boolean values
    """
    sl = []
    for lt in range(len(string) - 1):
        if string[lt].isspace() and not(string[lt + 1].isspace()):
            sl.append(True)
    sl.append(False)
    return sl


if __name__ == '__main__':
    nlp = spacy.load('es_core_news_sm')

    doc = nlp('Me gusta David Bowie')
    words = [token.text for token in doc]
    spaces = get_spaces(doc.text)
    print(spaces)

    doc = Doc(nlp.vocab, words=words, spaces=spaces)
    # Adding new Span to the doc 'DAVID BOWIE'
    span_david_bowie = Span(doc, 2, 4, label='DAVID_BOWIE')
    doc.ents = [span_david_bowie]

    for ent in doc.ents:
        print(ent.text, ent.label_)

    print(get_spaces('Me gusta  David Bowie'))
