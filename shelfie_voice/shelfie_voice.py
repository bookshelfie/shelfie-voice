#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""shelfie_voice Alexa Skill"""

from flask import Flask

from shelfie_voice.logger import logger
from shelfie_voice.extensions import ask

def create_app(config="config.base"):
    """App creation factory
    Pass configuration from instance folder to
    setup links to the shelfie_server.
    See README.md for more info.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.base")
    if config:
        app.config.from_object(config)
    app.config.from_pyfile("config.py", silent=True)
    app.config.from_envvar("SHELFIE_VOICE", silent=True)
    ask.init_app(app)
    return app
