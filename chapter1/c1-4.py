import spacy


def lex_attr(doc):
    """
    Prints the kind of token for each token in doc
    :param doc: Document generated with nlp
    :return: None
    """
    print("is_alpha:", [token.is_alpha for token in doc])
    print("is_punct:", [token.is_punct for token in doc])
    print("like_num:", [token.like_num for token in doc])


def find_percent(doc):
    """
    Prints the percentage founded in doc
    :param doc: Document generated with nlp
    :return: None
    """
    for token in doc:
        if token.like_num:
            next_token = doc[token.i+1]
            if next_token.text == '%':
                print("Founded %", token.text)


if __name__ == '__main__':
    # nlp includes the processing pipeline (tokenizer and other tools)
    nlp = spacy.blank('es')

    # processing text with nlp object
    d = nlp('Esto es una prueba de texto sencilla.')
    print(type(d))

    # accessing all the tokens (text value) in the doc
    for t in d:
        print(t.text)

    # span is a slice of the document
    span = d[1:3]
    print(d[2:4])
    print(span.text)

    lex_attr(d)

    # Percentage tests
    d2 = nlp("En 1990, más del 60 % de las personas en Asia del Este se encontraban "
             "en extrema pobreza. Ahora, menos del 4 % lo están.")

    find_percent(d2)
