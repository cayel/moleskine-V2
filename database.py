import sqlite3

class Artist:
    def __init__(self, artist_name, artist_id):
        self.name = artist_name
        self.id = artist_id

    def __str__(self):
        return self.name

class Release:
    def __init__(self, release_artist, release_title, release_date, release_image=None):
        self.title = release_title
        self.date = release_date
        self.artist = release_artist
        self.image = release_image
    
    def __str__(self):
        return f"{self.title} ({self.date}) - {self.artist.name}"

class ReleaseList:
    def __init__(self, list_id, list_name, list_description, is_private):
        self.id = list_id
        self.name = list_name
        self.description = list_description
        self.is_private = is_private
        self.releases = []

    def add_release(self, release):
        self.releases.append(release)

    def __str__(self):
        return f"Liste {self.name} : {len(self.releases)} releases"
    
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
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    create_artist_table(cursor)
    create_release_table(cursor)
    create_list_table(cursor)
    create_list_release_table(cursor)
    
    connection.commit()
    connection.close()

def add_artist(artist_name):
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO artist(name) VALUES (?)", (artist_name,))
    
    connection.commit()
    connection.close()

def add_release(release_title, release_date, artist_id, release_image=None):
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO release(title, date, artist_id, image) VALUES (?, ?, ?, ?)", (release_title, release_date, artist_id, release_image))
    
    connection.commit()
    connection.close()

def add_list(list_name, list_description, is_private):
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO list(name, description, is_private) VALUES (?, ?, ?)", (list_name, list_description, is_private))
    
    connection.commit()
    connection.close()

def add_list_release(list_id, rank, release_id):
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO list_release(list_id, rank, release_id) VALUES (?, ?, ?)", (list_id, rank, release_id))
    
    connection.commit()
    connection.close()

def populate_database():
    add_artist("Nick Cave & The Bad Seeds")
    add_artist("Einstürzende Neubauten")
    add_artist("New Model Army")
    
    add_release("From Her To Eternity", "1984-06-01", 1, "https://upload.wikimedia.org/wikipedia/en/3/38/Fromhertoeternity.jpg")
    add_release("The Firstborn Is Dead", "1985-06-03", 1, "https://upload.wikimedia.org/wikipedia/en/6/6b/The_Firstborn_Is_Dead.png")
    add_release("Kicking Against The Pricks", "1986-08-18", 1, "https://upload.wikimedia.org/wikipedia/en/e/e5/Kickingagainstthepricks.jpeg")
    add_release("Your Funeral... My Trial", "1986-11-03", 1, "https://upload.wikimedia.org/wikipedia/en/1/16/Yourfuneralmytrial.jpg")
    add_release("Tender Prey", "1988-09-19", 1, "https://upload.wikimedia.org/wikipedia/en/2/2e/Tenderprey.jpg")
    add_release("The Good Son", "1990-04-17", 1, "https://upload.wikimedia.org/wikipedia/en/f/f4/Thegoodson.jpg")
    add_release("Henry's Dream", "1992-04-27", 1,"https://upload.wikimedia.org/wikipedia/en/f/ff/Henrysdream.jpg")
    add_release("Let Love In", "1994-04-18", 1, "https://upload.wikimedia.org/wikipedia/en/f/f0/Letlovein.jpg")
    add_release("Murder Ballads", "1996-02-05", 1, "https://upload.wikimedia.org/wikipedia/en/5/56/Murderballads.jpg")
    add_release("The Boatman's Call", "1997-03-03",1,"https://upload.wikimedia.org/wikipedia/en/3/31/Nick_cave_and_the_bad_seeds-the_boatman%27s_call.jpg")
    add_release("No More Shall We Part", "2001-04-02",1, "https://upload.wikimedia.org/wikipedia/en/9/99/No_more_shall_we_part_cover.jpg")
    add_release("Nocturama", "2003-02-03",1, "https://upload.wikimedia.org/wikipedia/en/6/6e/Nocturama.jpg")
    add_release("Abattoir Blues / The Lyre of Orpheus", "2004-09-20",1, "https://upload.wikimedia.org/wikipedia/en/2/27/Abattoir_Blues%2BThe_Lyre_of_Orpheus.jpg")
    add_release("Dig, Lazarus, Dig!!!", "2008-03-03",1, "https://upload.wikimedia.org/wikipedia/en/4/42/Nick_Cave_%26_the_Bad_Seeds_-_Dig%2C_Lazarus%2C_Dig%21%21%21_coverart.JPG")
    add_release("Push The Sky Away", "2013-02-18",1, "https://upload.wikimedia.org/wikipedia/en/f/f3/Push_the_Sky_Away.jpg")
    add_release("Skeleton Tree", "2016-09-09",1, "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Nick_Cave_and_The_Bad_Seeds_-_Skeleton_Tree.jpg/440px-Nick_Cave_and_The_Bad_Seeds_-_Skeleton_Tree.jpg")
    add_release("Ghosteen", "2019-10-04",1, "https://upload.wikimedia.org/wikipedia/en/4/45/Ghosteen_-_Nick_Cave_and_the_Bad_Seeds.jpg")
    add_release("Wild God", "2024-08-30",1, "https://upload.wikimedia.org/wikipedia/en/7/7f/Nick_Cave_and_the_Bad_Seeds_-_Wild_God.png")

    add_release("Kollaps", "1981-10-05", 2, "https://www.fromthearchives.org/en/ENKollaps_LP_f.jpg")
    add_release("Zeichnungen des Patienten O. T.", "1983-11-21", 2, "https://www.fromthearchives.org/en/ENZeichnungen_LP_f.jpg")   
    add_release("80-83 Strategies Against Architecture", "1984-01-23", 2, "https://www.fromthearchives.org/en/ENStrat1CD_f.jpg")

    add_release("Vengeance", "1984-04-04", 3, "https://upload.wikimedia.org/wikipedia/en/9/91/NMA_vengeance.jpg")

    add_list("Albums de Nick Cave & The Bad Seeds", "Tous les albums des Nick Cave avec les Bad Seeds", False)
    add_list("Albums de Einstürzende Neubauten", "Tous les albums de Einstürzende Neubauten", False)
    add_list("Albums de New Model Army", "Tous les albums de New Model Army", False)
    add_list("Top 1988", "Mon top album 1988", True)

    add_list_release(1, 1, 1)
    add_list_release(1, 2, 2)
    add_list_release(1, 3, 3)
    add_list_release(1, 4, 4)
    add_list_release(1, 5, 5)
    add_list_release(1, 6, 6)
    add_list_release(1, 7, 7)
    add_list_release(1, 8, 8)
    add_list_release(1, 9 ,9)
    add_list_release(1, 10, 10)
    add_list_release(1, 11, 11)
    add_list_release(1, 12, 12)
    add_list_release(1, 13, 13)
    add_list_release(1, 14, 14)
    add_list_release(1, 15, 15)
    add_list_release(1, 16, 16)
    add_list_release(1, 17, 17)
    add_list_release(1, 18, 18)

    add_list_release(2, 1, 19)
    add_list_release(2, 2, 20)
    add_list_release(2, 3, 21)

    add_list_release(3, 1, 22)  

    add_list_release(4, 1, 5)

def load_lists():
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT id, name, description, is_private FROM list")
    
    lists = []
    
    for row in cursor.fetchall():
        list_id, list_name, list_description, is_private = row
        lists.append(ReleaseList(list_id, list_name, list_description, is_private))
    
    connection.close()
    
    return lists

def load_list_releases():
    connection = sqlite3.connect("moleskine.db")
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
    connection = sqlite3.connect("moleskine.db")
    cursor = connection.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS list_release")
    cursor.execute("DROP TABLE IF EXISTS list")
    cursor.execute("DROP TABLE IF EXISTS release")
    cursor.execute("DROP TABLE IF EXISTS artist")
    
    connection.commit()
    connection.close()