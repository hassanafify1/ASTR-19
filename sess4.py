
class Platypus:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print(f"Platypus has arms that are {self.arm_length} meters long.")
        print(f"Platypus has legs that are {self.leg_length} meters long.")
        print(f"Platypus has {self.num_eyes} eyes.")
        print(f"Does it have a tail? {'Yes' if self.has_tail else 'No'}")
        print(f"Is it furry? {'Yes' if self.is_furry else 'No'}")

my_platypus = Platypus(1.3, 2.1, 2, True, True)

my_platypus.describe()
