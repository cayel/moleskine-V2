
class ReleaseList:
    def __init__(self, list_id, list_name, list_description, is_private):
        self.id = list_id
        self.name = list_name
        self.description = list_description
        self.is_private = is_private
        self.releases = []

    def release_exists(self, release_id):
        for release in self.releases:
            if release.id == release_id:
                return True
        return False

    def add_release(self, release):
        if not self.release_exists(release.id):
            self.releases.append(release)
            return True
        else:
            print(f"{release} is already in the list")
            return False

    def get_release_rank(self, release):
        return self.releases.index(release) + 1
    
    def add_release_rank(self, release, rank):
        self.releases.insert(rank-1, release)

    def clear_releases(self):
        self.releases.clear()
        
    def __str__(self):
        return f"({self.id}) - {self.name} : {len(self.releases)} releases"
    

