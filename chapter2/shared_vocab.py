from typing import Any
import spacy


def get_lexeme(word: str) -> tuple[str, Any, Any]:
    """
    Lexemes are entries in vocabulary context independent
    :param word:
    :return:
    """
    lexeme = nlp.vocab[word]
    return lexeme.text, lexeme.orth, lexeme.is_alpha


if __name__ == '__main__':
    nlp = spacy.load("es_core_news_sm")
    print([word for word in nlp.vocab.strings if word == 'café'])
    cafe_hash = nlp.vocab.strings['café']

    print(cafe_hash)

    string = nlp.vocab.strings[32833993555699147]
    print(string)

    doc = nlp('Esta es una prueba tomando café')
    string_doc = doc.vocab.strings['café']
    print(string_doc)

    print(get_lexeme('café'))
