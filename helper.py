ISBN = "isbn"
KEY_WORD = "key_word"


def is_isbn_or_key(word):
    """
    判断是关键字还是isbn
    isbn isbn13 13个0-9的数字组成, isbn10 10个0-9数字组成,含有一些'-'

    :param word:
    :return:
    """
    if len(word) == 13 and word.isdigit():
        return ISBN
    short_q = word.replace("-", "")
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        return ISBN
    return KEY_WORD
