from project.car.car import Car

class MuscleCar(Car):
    min_speed = 250
    max_speed = 450
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model,speed_limit)