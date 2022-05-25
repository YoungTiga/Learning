from project.song import Song


class Album:

    def __init__(self,name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self,song: Song):
        if any([x.name == song.name for x in self.songs]):
            return "Song is already in the album."
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."
    def remove_song(self,song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        elif not any([x.name==song_name for x in self.songs]):
            return "Song is not in the album."
        song_to_remove = [x for x in self.songs if x.name == song_name][0]
        self.songs.remove(song_to_remove)
        return  f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result