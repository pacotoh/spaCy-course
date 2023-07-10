import spacy
from spacy.matcher import Matcher, PhraseMatcher

if __name__ == '__main__':
    nlp = spacy.load('es_core_news_md')
    doc = nlp('Me gusta comer pizza y soy muy muy feliz')

    pattern_pizza = [{'LEMMA': 'comer', 'POS': 'VERB'}, {'LOWER': 'pizza'}]
    pattern_feliz = [{'TEXT': 'muy', 'OP': '+'}, {'TEXT': 'feliz'}]

    matcher = Matcher(nlp.vocab)
    matcher.add('PIZZA', [pattern_pizza])
    matcher.add('MUY_FELIZ', [pattern_feliz])

    matches = matcher(doc)

    for match in matches:
        print(match, '->', doc[match[1]:match[2]])

    # Another way to access the matches
    for match_id, start, end in matcher(doc):
        print(doc[start:end])

    # Dog matcher example
    matcher = Matcher(nlp.vocab)
    matcher.add("PERRO", [[{"LOWER": "labrador"}, {"LOWER": "dorado"}]])
    doc = nlp("Tengo un labrador dorado")

    for match_id, start, end in matcher(doc):
        span = doc[start:end]
        print("span encontrado:", span.text)
        print("Token raíz:", span.root.text)
        print("Token raíz cabeza:", span.root.head.text)
        print("Token anterior:", doc[start - 1].text, doc[start - 1].pos_)

    # phrase matching -> more efficient than the matcher
    matcher = PhraseMatcher(nlp.vocab)

    # The pattern will be exactly the nlp text created
    pattern = nlp('labrador dorado')
    matcher.add('PERRO', [pattern])

    doc = nlp('Tengo un labrador dorado')
    matches = matcher(doc)

    for match_id, start, end in matches:
        span = doc[start:end]
        print(span.text, span.root, span.root.head)


