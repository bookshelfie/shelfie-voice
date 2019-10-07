#!/usr/bin/env python

"""Alexa extension"""
import random
from flask_ask import Ask, statement

from shelfie_voice.logger import logger
from shelfie_voice import utils

ask = Ask(route="/")


@ask.intent("BookFinderIntent")
def find_book(book):
    """Receives the book query string from alexa
    Sample queries:

    >>> Ask my bookshelf where I've placed {book}
    >>> Ask my bookshelf where is my copy of {book}
    >>> Ask my bookshelf where's {book}
    >>> Ask my bookshelf where I've kept {book}
    >>> Ask my bookshelf where is {book}
    """
    logger.debug("Trying to find books with title containing '{}'".format(book))
    book = utils.find_books(book)
    if book is not None:
        responses = [
            "Oh! I know where that book is! Let me show you.",
            "Ah, here you go.",
            "That is easy. I'll point it out to you.",
            "One book, coming right up.",
            "There it is."
        ]
        text = random.choice(responses)
    else:
        responses = [
            "I don't know where you put that book. Do you have it?",
            "If you kept your books better organized, you'd know that you probably don't have that book.",
            "Do you own that book? I don't see it anywhere.",
        ]
        text = random.choice(responses)
    return statement(text).simple_card('Hello', text)


@ask.intent("AuthorIntent")
def find_author(author):
    """Receives the author query string from alexa
    Sample queries:
    >>> Ask my bookshelf where are the books by {author}
    >>> Ask my bookshelf where are {author}'s books
    >>> Ask my bookshelf where I've placed books by {author}.
    """
    logger.debug(
        "Trying to find books by author: '{}'".format(author))
    books = utils.find_books_by_author(author)
    if books is not None:
        text = "I found some books by {}! Here they are.".format(author)
    else:
        text = "I don't know where you put books by {}. Are you sure you have any?".format(author)
    return statement(text).simple_card("Hello", text)


@ask.intent("ReadCountIntent")
def find_books_by_read_count(read_count):
    """Finds books by read count.
    >>> Ask my bookshelf to show me books I have read {at least once}.
    >>> Ask my bookshelf to show me books I've {never} read
    >>> Ask my bookshelf to show me books I've read {more than five times}.
    """
    return not_implemented()


@ask.intent("LastReadIntent")
def find_books_by_last_read(last_read):
    """Finds books by last read date
    Example queries:
    >>> Ask my bookshelf to show me books I have read {in the last six months}.
    >>> Ask my bookshelf to show me books I read {this year}.
    """
    return not_implemented()


def not_implemented():
    """Placeholder function for unimplemented features."""
    text = "This feature is not yet implemented."
    return statement(text).simple_card("Hello", text)
