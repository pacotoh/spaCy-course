import spacy


if __name__ == '__main__':
    nlp = spacy.load('es_core_news_md')
    # shows: ['tok2vec', 'morphologizer', 'parser', 'attribute_ruler', 'lemmatizer', 'ner']
    print(nlp.pipe_names)

    # tuples with (name, component)
    print(nlp.pipeline)
