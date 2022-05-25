
class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self,decoration):
        self.decorations.append(decoration)

    def remove(self,decoration):
        if not decoration in self.decorations:
            return False

        self.decorations.remove(decoration)
        return True

    def find_by_type(self,decoration_type: str):
        if not any(x.__class__.__name__ == decoration_type for x in self.decorations):
            return "None"
        return [x for x in self.decorations if x.__class__.__name__ == decoration_type][0]
