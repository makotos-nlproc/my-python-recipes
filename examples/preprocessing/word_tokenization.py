from janome.tokenizer import Tokenizer
# from janome.tokenfilter import POSKeepFilter


def tokenize_by_word(text: str, filter_target: str):
    """"""

    # token_filters = [POSKeepFilter(filter_target)]
    t = Tokenizer(wakati=True)
    return t.tokenize(text)
