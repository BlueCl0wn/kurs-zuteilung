from student import Student

class Workshop:
    def __init__(self, name: str, plaetze: int):
        self.name = name
        self.plaetze = plaetze

        self.students = []

    def schueler_hinzufuegen_generell(self, student: Student, size:int, avg:int, distance: int) -> bool:
        if len(self.students) < size and len(self.students) < avg + distance:
            self.students.append(student)
            return True
        else:
            return False

    def schueler_hinzufuegen_max(self, student: Student, avg:int, distance: int) -> bool:
        return self.schueler_hinzufuegen_generell(student, self.plaetze, avg, distance)

    def get_length(self):
        return len(self.students)

