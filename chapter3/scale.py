import spacy
from spacy.tokens import Doc

if __name__ == '__main__':
    # Use: docs = list(nlp.pipe(MUCHOS_TEXTOS)) -> this process text as a stream
    # instead of docs = [nlp(texto) for texto in MUCHOS_TEXTOS]

    nlp = spacy.load('es_core_news_sm')

    # Adding context
    data = [
        ('Esto es un texto', {'id': 1, 'page': 15}),
        ('y otro texto', {'id': 2, 'page': 16}),
    ]

    for doc, context in nlp.pipe(data, as_tuples=True):
        print(doc.text, context['page'])

    Doc.set_extension('id', default=None)
    Doc.set_extension('page', default=None)

    for doc, context in nlp.pipe(data, as_tuples=True):
        doc._.id = context['id']
        doc._.page = context['page']

    # Use nlp.make_doc instead nlp if we want to tokenize a text (only using the tokenizer)
    doc = nlp.make_doc("¡Hola Mundo!")

    print([token.text for token in doc])

    # To disable components (only in with blocks)
    with nlp.select_pipes(disable=["parser"]):
        print(nlp.pipeline)
        doc = nlp('Hola mundo')
        print(doc.ents)
