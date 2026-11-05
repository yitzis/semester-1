# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        Initializes a Person with a name and a date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if name == "":
            raise ValueError("Name cannot be an empty string.")
        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object.")

        self.name = name
        self.birth = birth
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """
        Returns the uppercased initial letters of each part of the person's name.
        """
        parts = self.name.split()
        result = ""
        for part in parts:
            result += part[0].upper()
        return result

    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        today = date.today()
        return today.day == self.birth.day and today.month == self.birth.month