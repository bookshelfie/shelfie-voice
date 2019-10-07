#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""utilities"""

import requests
from flask import current_app
from shelfie_voice.logger import logger


def find_books(book):
    """Given a book's name, this function calls the API for the shelf."""
    url = "{}/book/".format(current_app.config["SHELFIE_SERVER_URL"])
    data = {
        "title": book
    }
    response = requests.get(url, params=data)
    logger.debug(response.content)
    return response.json()


def find_books_by_author(author):
    """Given an author's name, find all the books by him."""
    url = "{}/author/".format(current_app.config["SHELFIE_SERVER_URL"])
    data = {
        "author": author
    }
    response = requests.get(url, params=data)
    logger.debug(response.content)
    return response.json()
