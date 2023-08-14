from neo4j    import GraphDatabase
from decouple import config


DB_PORT = config("PORT", cast=str)
DB_HOST = config("HOST", cast=str)
DB_USER = config("USER", cast=str)
DB_PASS = config("PASS", cast=str)


driver = GraphDatabase.driver(f"bolt://{DB_HOST}:{DB_PORT}", auth=(DB_USER, DB_PASS))