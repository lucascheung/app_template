export ROOT_DIR="$HOME/repos/toutiao"
python3 -m gunicorn server.bootstrap:app -b :5000 -w 1 --timeout 900
