export PYTHONPATH=$PYTHONPATH:/python

python class_server.py & disown
python login_server.py & disown