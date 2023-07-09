import spacy


def propn_after_verb_wrong() -> None:
    """
    This method is using strings instead token attributes in spaCy
    :return: None
    """
    nlp_ = spacy.load("es_core_news_sm")
    doc_ = nlp_("Por Berlín fluye el río Esprea.")

    token_texts = [token_.text for token_ in doc_]
    pos_tags = [token_.pos_ for token_ in doc_]

    for index, pos in enumerate(pos_tags):
        if pos == "PROPN":
            if pos_tags[index + 1] == "VERB":
                result = token_texts[index]
                print(result)


if __name__ == '__main__':
    # This is the solution using token information -> OK
    nlp = spacy.load("es_core_news_sm")
    doc = nlp("Por Berlín fluye el río Esprea.")

    for token in doc:
        if token.pos_ == "PROPN":
            if doc[token.i + 1].pos_ == "VERB":
                print(token.text)
