import spacy

if __name__ == '__main__':
    nlp = spacy.blank("en")

    # Created by processing a string of text with the nlp object
    doc = nlp("Hello world!")

    # Iterate over tokens in a Doc
    for token in doc:
        print(token.text)

    doc = nlp("I like tree kangaroos and narwhals.")
    tree_kangaroos = doc[2:4]
    print(tree_kangaroos.text)

