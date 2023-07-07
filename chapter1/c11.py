import spacy
from spacy.matcher import Matcher


if __name__ == '__main__':
    nlp = spacy.load("es_core_news_sm")
    doc = nlp("Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
              "colección de zapatillas adidas zx.")

    matcher = Matcher(nlp.vocab)
    pattern = [
        {'LOWER': 'adidas'},
        {'LOWER': 'zx'}
    ]

    matcher.add('ADIDAS_ZX_PATTERN', [pattern])
    matches = matcher(doc)

    print("Resultados:", [doc[start:end].text for match_id, start, end in matches])
