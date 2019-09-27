from shelfie_voice import create_app

if __name__ == "__main__":
    app = create_app(config="config.base")
    app.run()
