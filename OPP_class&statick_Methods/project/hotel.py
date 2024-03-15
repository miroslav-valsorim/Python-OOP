from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.find_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room == room_number:
                return room
        return None

    def free_room(self, room_number):
        room = self.find_room_by_number(room_number)
        room_guests = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= room_guests

    def status(self):
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]

        result = f'Hotel {self.name} has {self.guests} total guests' + \
                 '\n' + \
                 f'Fee rooms: {",".join(free_rooms)}' + \
                 '\n' + \
                 f'Taken rooms: {",".join(taken_rooms)}'

        return result


hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)
hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)
hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())