from sklearn.feature_extraction.text import CountVectorizer

def one_hot_encode(text: str):
    """"""

    vectorizer = CountVectorizer(binary=True)
    