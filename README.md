# shelfie-voice
Alexa Skill

## Installation

```bash
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
gunicorn -w 1 manage:app

```

serve via ngrok
```
ngrok http 5000
```
