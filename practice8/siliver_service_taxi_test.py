from silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Mclaren 720s", 200, 1.23, 2)

    print(silver_service_taxi)

    print(silver_service_taxi.get_fare(18))


if __name__ == '__main__':
    main()
