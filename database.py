import os
import sqlite3
from artist import Artist
from release import Release
from release_list import ReleaseList

DATA_DIR = "data"
DATABASE_NAME = os.path.join(DATA_DIR, "moleskine.db")

def create_artist_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS artist (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

def create_release_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS release (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            artist_id INTEGER NOT NULL,
            image TEXT,
            mbid TEXT,
            FOREIGN KEY(artist_id) REFERENCES artist(id)
        )
    """)

def create_list_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS list (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            is_private BOOLEAN NOT NULL
        )
    """)

def create_list_release_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS list_release (
            list_id INTEGER NOT NULL,
            rank INTEGER NOT NULL,
            release_id INTEGER NOT NULL,
            FOREIGN KEY(list_id) REFERENCES list(id),
            FOREIGN KEY(release_id) REFERENCES release(id),
            PRIMARY KEY(list_id, release_id)
        )
    """)    

def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    create_artist_table(cursor)
    create_release_table(cursor)
    create_list_table(cursor)
    create_list_release_table(cursor)
    
    connection.commit()
    connection.close()

def add_artist(artist_name):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO artist(name) VALUES (?)", (artist_name,))
    
    connection.commit()
    connection.close()

def add_release(release_title, release_date, artist_id, release_image=None, release_mbid=None):
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        
        cursor.execute(
            "INSERT INTO release(title, date, artist_id, image, mbid) VALUES (?, ?, ?, ?, ?)",
            (release_title, release_date, artist_id, release_image, release_mbid)
        )
        
        connection.commit()
        return True, "Release added successfully"
    except sqlite3.Error as e:
        return False, f"An error occurred: {e}"
    finally:
        if connection:
            connection.close()

def add_list(list_name, list_description, is_private):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO list(name, description, is_private) VALUES (?, ?, ?)", (list_name, list_description, is_private))
    
    connection.commit()
    connection.close()

def add_list_release(list_id, rank, release_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO list_release(list_id, rank, release_id) VALUES (?, ?, ?)", (list_id, rank, release_id))
    
    connection.commit()
    connection.close()

def load_lists():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, name, description, is_private FROM list")
    
    lists = []
    
    for row in cursor.fetchall():
        list_id, list_name, list_description, is_private = row
        lists.append(ReleaseList(list_id, list_name, list_description, is_private))
    
    connection.close()
    
    return lists

def load_list_releases():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT list.id, list.name, list.description, list.is_private, release.title, release.date, artist.name, release.image
        FROM list
        JOIN list_release ON list.id = list_release.list_id
        JOIN release ON list_release.release_id = release.id
        JOIN artist ON release.artist_id = artist.id
    """)
    
    lists = {}
    
    for row in cursor.fetchall():
        list_id, list_name, list_description, is_private, release_title, release_date, artist_name, release_image = row
        
        if list_id not in lists:
            lists[list_id] = ReleaseList(list_id, list_name, list_description, is_private)
        
        artist = Artist(artist_name, None)
        release = Release(artist, release_title, release_date, release_image)
        
        lists[list_id].add_release(release)
    
    connection.close()
    
    return lists.values()

def drop_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS list_release")
    cursor.execute("DROP TABLE IF EXISTS list")
    cursor.execute("DROP TABLE IF EXISTS release")
    cursor.execute("DROP TABLE IF EXISTS artist")
    
    connection.commit()
    connection.close()
    
def load_all_releases():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT release.id, release.title, release.date, artist.name, release.image
        FROM release
        JOIN artist ON release.artist_id = artist.id
    """)
    
    releases = []
    
    for row in cursor.fetchall():
        release_id, release_title, release_date, artist_name, release_image = row
        
        artist = Artist(artist_name, None)
        release = Release(artist, release_title, release_date, release_image)
        
        releases.append(release)
    
    connection.close()
    
    return releases

def load_artists():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, name FROM artist")
    
    artists = []
    
    for row in cursor.fetchall():
        artist_id, artist_name = row
        artists.append(Artist(artist_name, artist_id))
    
    connection.close()
    
    return artists

def load_releases_from_artists(artists):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    releases = []
    
    for artist in artists:
        cursor.execute("SELECT id, title, date, image FROM release WHERE artist_id = ?", (artist.id,))
        
        for row in cursor.fetchall():
            release_id, release_title, release_date, release_image = row
            release = Release(artist, release_title, release_date, release_image)
            releases.append(release)
    
    connection.close()
    
    return releases

def load_releases_from_artists_and_years(artists, years, sort_order):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    releases = []
    
    for artist in artists:
        cursor.execute("SELECT id, title, date, image FROM release WHERE artist_id = ? AND date BETWEEN ? AND ? ORDER BY date", (artist.id, years[0], years[1]+1))
        
        for row in cursor.fetchall():
            release_id, release_title, release_date, release_image = row
            release = Release(artist, release_title, release_date, release_image)
            releases.append(release)
    
    connection.close()
    # Sort releases by date
    releases.sort(key=lambda release: release.date, reverse=(sort_order == "Descendant"))
    return releases

def get_id_artist(artist_name):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    cursor.execute("SELECT id FROM artist WHERE name = ?", (artist_name,))
    result = cursor.fetchone()
    
    connection.close()
    
    if result is None:
        return -1
    else:
        return result[0]