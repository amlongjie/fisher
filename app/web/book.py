from flask import jsonify

from helper import ISBN
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web


# http://0.0.0.0:8080/book/search/9787501524044/1/
@web.route("/book/search/<q>/<page>/")
def search(q, page):
    """
        q: 普通关键字 isbn
        page
    :return:
    """

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == ISBN:
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
