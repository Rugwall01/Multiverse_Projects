from .db_connection import get_database

db = get_database()

def fetch_data(query):
    return list(db.financial_data.find(query))
