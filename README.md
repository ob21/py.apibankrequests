sudo apt install python
sudo apt install pip
sudo apt install virtualenv

mkdir myproject
cd myproject

virtualenv -p /usr/bin/python3.6 venv

source venv/bin/activate
deactivate

pip freeze > requirements.txt
pip install -r requirements.txt
