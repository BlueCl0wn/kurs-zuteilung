class Student:
    """
    Eine Klasse, die eine(n) Teilnehmer:in darstellt.
    """

    def __init__(self, name, *args):
        self.name = name

        self.subjects = []
        for arg in args:
            if type(arg) == type([]):
                self.subjects += [x for x in arg]
            else:
                self.subjects += [x for x in arg]

    def __eq__(self, other: object) -> bool:
        """
        Überprüft, ob die übergebene Instanz von 'Workshop' in der eigenen Wunschliste vorhanden ist.

        :param other: Instanz von Workshop
        :return: bool
        """
        return other in self.subjects  # [s.name for s in self.subjects]
