# shelfie-voice

`shelfie` is my bookshelf search engine project.

## Shelfie Voice API

This repository contains the alexa-skill for `shelfie`

## Installation and testing

Run the following Commands

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:13002 -w 1 wsgi

```

## Production Deployment

Use gunicorn and nginx for deployment.

### Systemctl file for gunicorn

```ini
[Unit]
Description=shelfie voice gunicorn
After=network.target

[Service]
User=user
Group=group
WorkingDirectory=/home/user/shelfie-voice
Environment="PATH=/home/user/shelfie-voice/env/bin"
ExecStart=/home/user/shelfie-voice/env/bin/gunicorn --workers 1 --bind 0.0.0.0:13002 wsgi:app

[Install]
WantedBy=multi-user.target

```

## Systemctl file for ngrok

```
[Unit]
Description=ngrok tunnel for shelfie voice
After=network.target

[Service]
User=user
Group=group
Environment="PATH=/home/user/tools/bin/"
ExecStart=/home/user/tools/bin/ngrok http 13001

[Install]
WantedBy=multi-user.target
```

Ensure that you register the alexa url by checking the url on ngrok.com.



## Development Notes

There's a caveat to how this application works. It is intended to
first ask the other API where the book is and then ask to
highlight it, but for now it just highlights it and then
responds. This is not how I intend it to work. I need to look
into dialogue building with Alexa.
