from student import Student
from random import sample
from kurse import workshops

kurse = ["Tanzen", "Boxen", "Rhönrad", "Tischtennis", "Handball", "Fußball", "Salsa", "Schwimmen", "Sprinten", "Karate"]

student_list = []

for i in range(500):
    name = i
    wunsch = sample(workshops, 6)
    student_list.append(Student(name, wunsch))