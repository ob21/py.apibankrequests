# Quickstart

sudo apt install python
sudo apt install pip
sudo apt install virtualenv

mkdir myproject
cd myproject

on linux :

virtualenv -p /usr/bin/python3.6 venv

source venv/bin/activate
deactivate

on windows :

python -m venv env

env\Scripts\activate.bat

pip freeze > requirements.txt
pip install -r requirements.txt
