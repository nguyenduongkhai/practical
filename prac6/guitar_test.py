from guitar import Guitar

def main():

    """Demo a guitar"""
    guitar_a=Guitar("Gibson L-5 CES",50,16035.40)
    print("{} get age()-Excepted {}.got {}".format(guitar_a.name,guitar_a.get_age(),guitar_a.get_age()))
    print("{} get is vintage()-Excepted {}.Got {}".format(guitar_a.name, guitar_a.is_vintage(), not(guitar_a.is_vintage())))


if __name__ == '__main__':
    main()