class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, filed, typing, reflection, year):
        """Initialise  instances.    """

        self.filed = filed
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """return the detail of the objects in string format """

        return "{} ,{} Typing,Reflection = {},First appeared  in {}".format(self.filed, self.typing, self.reflection,
                                                                            self.year)

    def is_dynamic(self):

        """return true if language is dynamic"""

        if self.typing.lower() == "dynamic":
            self.reflection = "Yes"
            return True
        else:
            self.reflection = "No"
            return False
