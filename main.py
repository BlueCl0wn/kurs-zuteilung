from workshop import Workshop
from student import Student

tanzen = Workshop("Tanzen", 6)
boxen = Workshop("Boxen", 6)
rennen = Workshop("Rennen", 6)

workshops = [tanzen, boxen, rennen]

a = Student("a", "Tanzen", "Boxen")
b = Student("b", "Tanzen", "Boxen")
c = Student("c", "Tanzen", "Boxen")
d = Student("d", "Tanzen", "Boxen")
e = Student("e", "Tanzen", "Boxen")
f = Student("f", "Tanzen", "Rennen")
g = Student("g", "Tanzen", "Rennen")
h = Student("h", "Tanzen", "Rennen")
i = Student("i", "Tanzen", "Rennen")
j = Student("j", "Tanzen", "Rennen")
k = Student("k", "Boxen", "Rennen")
l = Student("l", "Boxen", "Rennen")
m = Student("m", "Boxen", "Rennen")
n = Student("n", "Boxen", "Rennen")
o = Student("o", "Boxen", "Rennen")

students = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]


def get_avg() -> int:
    return int(len(students) / len(workshops) + 0.5)


avg = get_avg()


def first_fill():
    for st in students:
        for ws in workshops:
            if st == ws.name:
                if ws.schueler_hinzufuegen_generell(st, 6, avg, 0):
                    break


first_fill()


# def remove():
#   remaining = []
#  for ws in workshops:
#     if


def second_fill(avg):
    for st in students:
        for ws in workshops:
            if st == ws.name:
                if ws.schueler_hinzufuegen_generell(st, 6, avg, 1):
                    break


# second_fill(avg)

for ws in workshops:
    print(ws.name)
    for i in ws.students:
        print(i.name)
    print("")
