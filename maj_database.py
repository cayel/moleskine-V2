from database import query_database

def maj_database(version_initiale):
    version = version_initiale
    if version == 0:
        query_database("UPDATE database_version SET version = 1")
        version = 1
    if version == 1:
        # Add column discogs_id to the artist table
        query_database("ALTER TABLE artist ADD COLUMN discogs_id INTEGER")
        query_database("UPDATE database_version SET version = 2")
        version = 2
    return True
