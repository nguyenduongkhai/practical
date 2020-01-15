from car import Car

import random


class Unreliable(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability_number = random.uniform(0, 100)
        if reliability_number < self.reliability:
            return -1
        else:
            return super().drive(distance)