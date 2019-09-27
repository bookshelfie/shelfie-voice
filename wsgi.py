from shelfie_voice import create_app


application = create_app(config="config.base")

if __name__ == "__main__":
    application.run()
