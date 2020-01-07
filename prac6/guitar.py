class Guitar:
    """Represent to a Guitar class"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""

        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):

        """return the detail of the guitar objects in string format """

        return "{} ({}) :{:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):

        """return age of guitar"""

        return 2019-self.year

    def is_vintage(self):

        """ return true if age is greater than 50"""

        if self.get_age() > 50:
            return True
        return False
