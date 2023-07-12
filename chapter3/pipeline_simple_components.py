import spacy
from spacy.tokens import Doc
from spacy.language import Language


# Using decorators to create components -> steps in doc creation

@Language.component('show_length')
def custom_component_function(doc: Doc) -> Doc:
    print('Doc length:', len(doc))
    return doc


@Language.component('show_tokens')
def show_tokens_function(doc: Doc) -> Doc:
    print([token.text for token in doc])
    return doc


if __name__ == '__main__':
    nlp = spacy.load('es_core_news_sm')
    # use last, first or before/after to include the step in the desired position
    nlp.add_pipe('show_length', before='morphologizer')
    nlp.add_pipe('show_tokens', last=True)

    my_doc = nlp('Esta, es una prueba')

    print(nlp.pipe_names)
