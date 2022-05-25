class Smartphone:
    def __init__(self,memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def install(self, app, memory_needed):
        if self.memory >= memory_needed and self.is_on:
            self.apps.append(app)
            self.memory-=memory_needed
            return  f"Installing {app}"
        elif self.memory>=memory_needed and not self.is_on:
            return f"Turn on your phone to install {app}"
        else:
            return f"Not enough memory to install {app}"

    def power(self):
        self.is_on = not self.is_on

    def status(self):
        return  f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
