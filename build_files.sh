echo "BUILD START"
Python 3.10 -m pip install -r requirements.txt
Python 3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"