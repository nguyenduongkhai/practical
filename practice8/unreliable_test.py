from unreliable import Unreliable


def main():
    unreliable = Unreliable("Porsche", 30, 10)

    drive = unreliable.drive(10)

    if drive < 0:
        print("Your car is unreliable")
    else:
        print("You drive ", drive, "km")


if __name__ == '__main__':
    main()
