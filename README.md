# shelfie-voice
Alexa Skill

## Installation

Run the following Commands

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn -w 1 manage:app

```

# Production Deployment
## Systemctl file for gunicorn

```ini
[Unit]
Description=shelfie voice gunicorn
After=network.target

[Service]
User=user
Group=nginx
WorkingDirectory=/home/user/shelfie-voice
Environment="PATH=/home/user/shelfie-voice/env/bin"
ExecStart=/home/user/shelfie-voice/env/bin/gunicorn --workers 1 --bind 0.0.0.0:13001 wsgi:app

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

ngrok http 5000
```


###
