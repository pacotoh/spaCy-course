import spacy
from spacy.language import Language
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc


@Language.component('animal_component')
def animal_component_function(doc: Doc) -> Doc:
    """
    Component that creates entities with label 'ANIMAL' in the doc
    :param doc: Doc object to append entities
    :return: doc: Same doc but with entities added
    """
    matches = matcher(doc)
    spans = [Span(doc, start, end, label='ANIMAL') for match_id, start, end in matches]
    doc.ents = spans
    return doc


if __name__ == '__main__':
    nlp = spacy.load('es_core_news_sm')
    animals = ["labrador dorado", "gato", "tortuga", "oso de anteojos"]

    # Alternative to create nlp objects one by one -> Ex: nlp('labrador dorado')
    animal_pattern = list(nlp.pipe(animals))

    matcher = PhraseMatcher(nlp.vocab)
    matcher.add('ANIMAL', animal_pattern)
    print(animal_pattern)

    nlp.add_pipe('animal_component', after='ner')
    print(nlp.pipe_names)

    doc = nlp("Hoy vimos una tortuga y un oso de anteojos en nuestra caminata")
    print([(ent.text, ent.label) for ent in doc.ents])
