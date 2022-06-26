class Student:
    def __init__(self, name, *args):
        self.name = name
        self.subjects = [x for x in args]

    def __eq__(self, other: str):
        return other in self.subjects
