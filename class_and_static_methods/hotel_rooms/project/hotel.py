from project.room import Room


class Hotel:

    def __init__(self,name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([x.guests for x in self.rooms])
    @classmethod
    def from_stars(cls,stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self,room: Room):
        self.rooms.append(room)

    def take_room(self,room_number, people):
        room = [x for x in self.rooms if x.number == room_number][0]
        return room.take_room(people)
    def free_room(self,room_number):
        room = [x for x in self.rooms if x.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = [str(x.number) for x in self.rooms if x.is_taken == False]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken == True]
        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join(free_rooms)}
Taken rooms: {', '.join(taken_rooms)}"""


