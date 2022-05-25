from project.month_mapper import month_mapper
class DVD:

    def __init__(self,name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented =False
    @classmethod
    def from_date(cls,id: int, name: str, date: str, age_restriction: int):
        _,mouth,year = [int(x) for x in date.split(".")]
        mouth_as_str = month_mapper[mouth]
        return cls(name, id, year, mouth_as_str, age_restriction)
    def __repr__(self):
        rented_not_rented = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented_not_rented}"
