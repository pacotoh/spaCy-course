import spacy


def text_info(document) -> None:
    for token in document:
        # Text, Part of Speech and Dependencies
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_

        print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")


def show_entities(document) -> None:
    for ent in document.ents:
        print(ent.text, ent.label_)


if __name__ == '__main__':
    nlp = spacy.load("es_core_news_sm")

    text = (
        "De acuerdo con la revista Fortune, Apple fue la empresa "
        "más admirada en el mundo entre 2008 y 2012."
    )

    # Processing text
    doc = nlp(text)
    text_info(doc)
    show_entities(doc)
