from car import Car


def main():
    """Demo test code to show how to use car class."""
    # my_car = Car(180, "Porsche")
    # my_car.drive(30)
    # print("fuel =", my_car.fuel)
    # print("odo =", my_car.odometer)
    # print(my_car)
    #
    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    """"" Demo Limo Car """
    limo = Car(100, "Porsche")
    limo.add_fuel(20)
    print("The amount of fuel in the car : {} ".format(limo.fuel))
    limo.drive(115)
    print("The car's odometer : {}".format(limo.odometer))
    print(limo)


if __name__ == '__main__':
    main()
