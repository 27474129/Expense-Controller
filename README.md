Python version: 3.10.9

Installation process:

1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python deploy/run_migrations.py
5. uvicorn app_backend:app --reload --host 127.0.0.1 --port 8000