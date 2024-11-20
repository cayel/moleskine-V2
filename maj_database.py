from database import query_database

def maj_database(version_initiale):
    if version_initiale == 0:
        query_database("UPDATE database_version SET version = 1")
    return True
