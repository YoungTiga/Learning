from project.hardware.power_hardware import PowerHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.heavy_hardware import HeavyHardware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name,capacity,memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        software = ExpressSoftware(name,capacity_consumption,memory_consumption)
        curr_hardware = hardware[0]
        curr_hardware.install(software)
        System._software.append(software)



    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        curr_hardware = hardware[0]

        curr_hardware.install(software)
        System._software.append(software)


    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [ha for ha in System._hardware if ha.name == hardware_name]
        software = [ha for ha in System._software if ha.name == software_name]
        if hardware and software:
            current_hardware = hardware[0]
            current_software = software[0]
            System._software.remove(current_software)
            current_hardware.uninstall(current_software)

        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        res = "System Analysis\n"
        res += f"Hardware Components: {len(System._hardware)}\n"
        res += f"Software Components: {len(System._software)}\n"
        capacity_software = sum(x.capacity_consumption for x in System._software)
        memory_software = sum(x.memory_consumption for x in System._software)
        capacity_hardware = sum(x.capacity for x in System._hardware)
        memory_hardware = sum(x.memory for x in System._hardware)
        res += f"Total Operational Memory: {memory_software} / {memory_hardware}\n"
        res += f"Total Capacity Taken: {capacity_software} / {capacity_hardware}"

        return  res


    @staticmethod
    def system_split():
        res = ""
        for hardware in System._hardware:

            res += f"Hardware Component - {hardware.name}\n"
            express_softwares = [x for x in hardware.software_components if x.software_type == "Express"]
            light_softwares = [x for x in hardware.software_components if x.software_type == "Light"]
            memory_usage = sum(x.memory_consumption  for x in hardware.software_components)
            capacity_usge =  sum(x.capacity_consumption  for x in hardware.software_components)
            res += f"Express Software Components: {len(express_softwares)}\n"
            res += f"Light Software Components: {len(light_softwares)}\n"
            res += f"Memory Usage: {memory_usage} / {hardware.memory}\n"
            res += f"Capacity Usage: {capacity_usge} / {hardware.capacity}\n"
            res += f"Type: {hardware.hardware_type}\n"
            if hardware.software_components:
                res += f"Software Components: {', '.join(x.name for x in hardware.software_components)}\n"
            else:
                res += f"Software Components: None\n"
        return res.strip()
