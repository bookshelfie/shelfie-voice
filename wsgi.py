from shelfie_voice import create_app


if __name__ == "__main__":
    app = create_app(config="config.base") # pylint: disable=invalid-name
    app.run()
else:
    import logging
    application = create_app(config="config.base") # pylint: disable=invalid-name
    gunicorn_logger = logging.getLogger("gunicorn.error")
    application.logger.handlers = gunicorn_logger.handlers
    application.logger.setLevel(gunicorn_logger.level)
