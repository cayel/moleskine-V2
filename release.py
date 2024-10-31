class Release:
    def __init__(self, release_artist, release_title, release_date, release_image=None):
        self.title = release_title
        self.date = release_date
        self.artist = release_artist
        self.image = release_image
    
    def __str__(self):
        return f"{self.title} ({self.date}) - {self.artist.name}"