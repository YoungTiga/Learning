
class Zoo:
    def __init__(self,name: str,budget: int,animal_capacity: int,workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
    def add_animal(self,animal, price):
        if self.__budget < price:
            return  "Not enough budget"
        if len(self.animals)+1 > self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
    def hire_worker(self,worker):

        if len(self.workers)+1 > self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    def fire_worker(self,worker_name):
        if not any([x.name == worker_name for x in self.workers]):
            return f"There is no {worker_name} in the zoo"
        worker_to_remove = [x for x in self.workers if x.name == worker_name][0]
        self.workers.remove(worker_to_remove)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_salaries = sum([x.salary for x in self.workers])
        if self.__budget < sum_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_animal_money_care = sum([x.money_for_care for x in self.animals])
        if self.__budget < sum_animal_money_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_animal_money_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
    def profit(self,amount):
        self.__budget += amount
    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion.__repr__()+"\n"
        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger.__repr__()+"\n"
        cheetahs = [x for x in self.animals if x.__class__.__name__== "Cheetah"]
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(cheetah.__repr__() for cheetah in cheetahs)
        return result
    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper.__repr__()+'\n'
        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker.__repr__()+"\n"
        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += vet.__repr__()
        return result

