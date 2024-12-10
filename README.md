venv creation:
python -m venv doublefortune

venv activation:
.\doublefortune\Scripts\activate

Installed packages:
pip install fastapi uvicorn
pip install mysql-connector-python sqlalchemy
pip install alembic

Generate a requirements.txt file:
pip freeze > requirements.txt

Start your FastAPI application using Uvicorn:
uvicorn main:app --reload



