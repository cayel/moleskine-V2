class Artist:
    def __init__(self, artist_name, artist_id):
        self.name = artist_name
        self.id = artist_id

    def __str__(self):
        return self.name