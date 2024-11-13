class Release:
    def __init__(self, release_id, release_artist, release_title, release_date, release_image=None):
        self.id = release_id
        self.title = release_title
        self.date = release_date
        self.artist = release_artist
        self.image = release_image
    
    def __str__(self):
        return f"{self.id} - {self.title} ({self.date}) - {self.artist.name}"