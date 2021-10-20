class Animal:
    def __init__(self):
        self.eyes = 2
    def can_breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def can_swim(self):
        print("Can swim")
    def can_breathe(self):
        super().can_breathe()
        print("Underwater too")


fish = Fish()
fish.can_swim()
fish.can_breathe()


