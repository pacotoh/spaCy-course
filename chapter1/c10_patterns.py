import spacy
from spacy.matcher import Matcher


def show_matches(matches) -> None:
    for match_id, start, end in matches:
        matched_span = doc[start:end]
        print(matched_span.text, ':', match_id, start, end)


if __name__ == '__main__':
    nlp = spacy.load("es_core_news_sm")

    matcher = Matcher(nlp.vocab)

    # Pattern creation
    pattern = [{'TEXT': 'adidas'}, {'TEXT': 'zx'}]
    pattern_fifa = [
        {"IS_DIGIT": True},
        {"LOWER": "copa"},
        {"LOWER": "mundial"},
        {"LOWER": "fifa"},
        {"IS_PUNCT": True}
    ]

    pattern_comer = [
        {"LEMMA": "comer", "POS": "VERB"},
        {"POS": "NOUN"}
    ]

    pattern_comprar = [
        {"LEMMA": "comprar"},
        {"POS": "DET", "OP": "?"},
        {"POS": "NOUN"}
    ]

    matcher.add('ADIDAS_PATTERN', [pattern])

    doc = nlp('Nuevos diseños de zapatillas en la colección adidas zx')

    matches_adidas = matcher(doc)
    print(matches_adidas)

    show_matches(matches_adidas)

    matcher.add('COMER', [pattern_comer])
    matcher.add('COMPRAR', [pattern_comprar])

    doc = nlp('Camila prefería comer sushi. Pero ahora está comiendo pasta.')
    matches_comer = matcher(doc)
    show_matches(matches_comer)

    doc = nlp("Me compré un smartphone. Ahora le estoy comprando aplicaciones.")
    matches_comprar = matcher(doc)
    show_matches(matches_comprar)
