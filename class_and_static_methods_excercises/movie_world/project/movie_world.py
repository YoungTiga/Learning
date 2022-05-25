from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self,name: str):
        self.name = name
        self.customers = []
        self.dvds = []
    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10


    def add_customer(self,customer: Customer):
        if len(self.customers) == MovieWorld.customer_capacity():
            return
        self.customers.append(customer)
    def add_dvd(self,dvd: DVD):
        if len(self.dvds) == MovieWorld.dvd_capacity():
            return
        self.dvds.append(dvd)
    def rent_dvd(self,customer_id: int, dvd_id: int):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self,customer_id, dvd_id):
        customer = self.__get_customer(customer_id)
        dvd = self.__get_dvd(dvd_id)
        if dvd not in customer.rented_dvds:
           return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __get_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
    def __get_dvd(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def __repr__(self):
        result = ''
        result += '\n'.join(repr(x) for x in self.customers)+"\n"
        result += '\n'.join(repr(x) for x in self.dvds)
        return  result



