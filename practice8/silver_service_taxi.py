from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel, price_per_km)

        self.fanciness = fanciness * self.price_per_km

    def get_fare(self, km):
        return self.fanciness * km + self.flagfall

    def __str__(self):
        return "{} plus of {}".format(super().__str__(), self.fanciness, self.flagfall)
