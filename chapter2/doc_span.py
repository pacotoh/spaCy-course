import spacy
from spacy.tokens import Doc, Span


nlp = spacy.blank('es')

words = ['¡', 'Hola', 'mundo', '!']
spaces = [False, True, False, False]

doc = Doc(nlp.vocab, words=words, spaces=spaces)
span = Span(doc, 1, 3)
span_with_label = Span(doc, 1, 3, label='SALUDO')

doc.ents = [span_with_label]

print(span, doc[1:3])

for ent in doc.ents:
    print(ent.text, ent.label_, ent.root)
