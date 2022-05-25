from project.software.software import Software


class Hardware:

    def __init__(self,name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self,software: Software):
        memory_left = self.memory-sum(x.memory_consumption for x in self.software_components)
        capacity_left = self.capacity - sum(x.capacity_consumption for x in self.software_components)

        if software.capacity_consumption<=capacity_left and software.memory_consumption <= memory_left:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self,software: Software):
        self.software_components.remove(software)