class Artist:
    def __init__(self, artist_name, artist_id, country=None, discogs_id=None):
        self.name = artist_name
        self.id = artist_id
        self.country = country
        self.discogs_id = discogs_id

    def __str__(self):
        return self.name