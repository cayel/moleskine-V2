from database import query_database

def update_database_version(new_version):
    """
    Update the database version to the specified new_version.
    
    Args:
        new_version (int): The new version number to update to.
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        query_database("UPDATE database_version SET version = ?", (new_version,))
    except Exception as e:
        print(f"Error updating database version to {new_version}: {e}")
        return False
    return True

def update_database(version_initiale):
    """
    Update the database schema based on the initial version.
    
    Args:
        version_initiale (int): The initial version of the database schema.
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """    
    version = version_initiale
    try:
        if version == 0:
            if update_database_version(1):
                version = 1
            else:
                return False
        if version == 1:
            # Add column discogs_id to the artist table
            query_database("ALTER TABLE artist ADD COLUMN discogs_id INTEGER")
            if update_database_version(2):
                version = 2
            else:
                return False
        if version == 2:
            # Add column discogs_id to the release table
            query_database("ALTER TABLE release ADD COLUMN discogs_id INTEGER")
            if update_database_version(3):
                version = 3
            else:
                return False
    except Exception as e:
        print(f"Error updating database: {e}")
        return False
    return True
