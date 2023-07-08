from typing import Any
import spacy


def get_lexeme(word: str) -> tuple[str, Any, Any]:
    """
    Lexemes are entries in vocabulary context independent
    :param word: word to get lexeme
    :return: text, orth (hash) and is_alpha from lexeme
    """
    lexeme = nlp.vocab[word]
    return lexeme.text, lexeme.orth, lexeme.is_alpha


def get_hash(word: str) -> int:
    """
    Access to vocab and get the hash of word
    :param word: word to obtain the hash
    :return: hash as an int that represent the hash from the word
    """
    return nlp.vocab.strings[word]


def get_string(hs: int) -> str:
    """
    Access to the String Store and get the string asociated with hs
    :param hs: hash to obtain a word from String Store
    :return: a str that represents the word asociated with hs
    """
    return nlp.vocab.strings[hs]


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

    print(get_hash('gato'))
    print(get_string(9565357104409163886))
