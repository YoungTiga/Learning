from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self,room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.total_cost()
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        res = ""
        for room in self.rooms:
            if room.budget >= room.total_cost():
                room.budget -= room.total_cost()
                res += f"{room.family_name} paid {room.total_cost():.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                res += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return res.strip()

    def status(self):
        res = ""
        res += f"Total population: {sum([x.members_count for x in self.rooms])}\n"
        for room in self.rooms:
            res += f"{room.family_name} with {room.members_count} members. " \
                   f"Budget: {room.budget:.2f}$, " \
                   f"Expenses: {room.expenses:.2f}$\n"

            for number, child in enumerate(room.children):
                res += f"--- Child {number + 1} " \
                       f"monthly cost: {child.get_monthly_expense():.2f}$\n"
            res += f"--- Appliances monthly cost: " \
                   f"{sum(x.get_monthly_expense() for x in room.appliances):.2f}$\n"
        return res.strip()