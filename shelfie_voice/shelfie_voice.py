#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Shelfie voice app.
"""
from flask import Flask
from flask import render_template
from flask_ask import Ask, statement
from shelfie_voice.logger import logger

def create_app(config=""):
    """App creation factory"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.base")
    if config:
        app.config.from_object(config)
    app.config.from_pyfile("config.py", silent=True)
    app.config.from_envvar("SHELFIE_VOICE", silent=True)


    ask = Ask(app, "/")

    @ask.intent("BookFinderIntent")
    def hello(book):
        logger.debug(f"query: {} {}".format(book, type(book)))
        # send request to shelfie to highlight LOTR

        text = 'the book you asked for is {}'.format(book)
        return statement(text).simple_card('Hello', text)

    return app
