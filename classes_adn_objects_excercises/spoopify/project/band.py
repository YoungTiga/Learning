from project.album import Album
class Band:

    def __init__(self,name):
        self.name = name
        self.albums = []

    def add_album(self,album: Album):
        if any([x.name == album.name for x in self.albums]):
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self,album_name):
        if not any([x.name == album_name for x in self.albums]):
            return f"Album {album_name} is not found."
        curr_album = [x for x in self.albums if x.name == album_name][0]
        if curr_album.published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(curr_album)
        return f"Album {curr_album.name} has been removed."
    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()+"\n"
        return  result