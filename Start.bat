@echo off
start pythonw Core\Mailer\stub.py
start pip install -r requirements.txt
python PhishMailer.py
