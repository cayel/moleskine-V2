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