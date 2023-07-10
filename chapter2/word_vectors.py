import spacy
from spacy.tokens.doc import Doc
from spacy.tokens.span import Span
from spacy.tokens.token import Token

# word vector: words or phrases vinculated with vectors
# we need md models to include the word vectors, small models doesn't indlude it

if __name__ == '__main__':
    nlp = spacy.load("es_core_news_md")

    doc: Doc = nlp('Soy el que ser será y siendo quien eres soy quien seré')
    doc2: Doc = nlp('Siendo quien eres, soy quien soy')
    doc3: Doc = nlp('Me gustan los pimientos fritos')

    # Similarity between docs
    print(doc.similarity(doc2))
    print(doc.similarity(doc3))

    # Similarity between doc words
    for word in doc:
        print(word.text, word.similarity(doc[0]))

    # Similarity between different entities
    word: Token = doc3[3]
    print('[', word.text, '- doc2 ]', 'similarity:', word.similarity(doc2))
    print('[', word.text, '- doc3 ]', 'similarity:', word.similarity(doc3))

    # New similarity example
    doc_ch: Doc = nlp('Me gustan los chorizos parrilleros')
    doc_pz: Doc = nlp('Me gusta la pizza barbacoa')

    # between docs
    print(doc_ch.similarity(doc_pz))

    # Between words/tokens
    for word in doc_pz:
        print(doc_ch[1], word.text, doc_ch[1].similarity(word))

    # Between spans
    span_ch: Span = Span(doc_ch, 0, 3)
    span_pz: Span = Span(doc_pz, 0, 3)

    print(span_pz.similarity(span_ch))

    # word vectors -> word2vec using cosine
    print(doc_ch[3].vector, len(doc_ch[3].vector))
