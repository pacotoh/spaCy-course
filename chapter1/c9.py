import spacy


if __name__ == '__main__':
    nlp = spacy.load("es_core_news_sm")

    text = (
        "Los Olímpicos de Tokio 2020 son la inspiración para la nueva "
        "colección de zapatillas adidas zx."
    )

    doc = nlp(text)

    for ent in doc.ents:
        print(ent.text, ent.label_)

    adidas_zx = doc[14:16]
    print("Entidad faltante:", adidas_zx.text)
