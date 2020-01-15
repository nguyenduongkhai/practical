from taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100, 1.23)

    taxi.drive(40)

    print(taxi)
    print("The current fare is ", taxi.get_fare())

    taxi.drive(100)

    print(taxi)
    print("The current fare is ", taxi.get_fare())

    print(taxi.price_per_km)


if __name__ == '__main__':
    main()
