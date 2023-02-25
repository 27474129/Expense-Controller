Python version: 3.10.9

Установка:

1. python -m venv venv
2. source venv/bin/activate / venv/Scripts/activate
3. export PYTHONPATH=.
4. pip install -r requirements.txt
5. в psql консоли: "set time zone 'Europe/Moscow';"
6. python deploy/run_migrations.py
7. uvicorn app_backend:app --reload --host 127.0.0.1 --port 8000