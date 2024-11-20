from database import query_database

def maj_database(version_initiale):
    if version_initiale == 0:
        query_database("UPDATE database_version SET version = 1")
    if version_initiale == 1:
        # Add column discogs_id to the artist table
        query_database("ALTER TABLE artist ADD COLUMN discogs_id INTEGER")
        query_database("UPDATE database_version SET version = 2")
    return True
