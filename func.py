from random import sample


def get_avg(students: list, workshops: list) -> int:
    return int(len(students) / len(workshops) + 0.5)


def output(workshops: list) -> None:
    """
    Zeigt die Teilnehmer aller Workshops in gegebener Liste an.

    :param workshops: Liste mit Workshops
    :return: None
    """
    for ws in workshops:
        print(f"{ws.name}:")
        for i in ws.students:
            print(f"\t{i.name};  wished for: {[x.name for x in i.subjects]}")
        print("")


def get_current_avg(workshops: list) -> int:
    """
    !!!redundant!!!
    :param workshops:
    :return:
    """
    temp = 0
    for ws in workshops:
        temp += ws.get_length()
    return int(temp / len(workshops))


def first_fill(students: list, workshops: list) -> None:
    """
    Erste Befüllung der Workshops ohne Rücksichtnahme auf jegliche Beschränkungen.

    :param students:
    :param workshops:
    :return:
    """
    for st in students:
        for ws in workshops:
            if st == ws:
                if ws.schueler_hinzufuegen_inf(st):  # , avg, distance):
                    break


def first_remove(workshops: list, avg: int, distance=0) -> list:
    """
    Entfernt alle Teilnehmer, die zu viel sind.

    :param workshops:
    :param avg:
    :param distance:
    :return:
    """

    # entferne personen aus workshop, wenn diese zu voll sind
    rem_students = []
    for ws in workshops:
        within_distance = ws.within_distance(avg, distance)
        if within_distance > 0:
            _choices = sample(ws.students, k=within_distance)
            for c in _choices:
                ws.students.remove(c)

            rem_students += _choices

    return rem_students


def second_fill(students: list, workshops: list, avg: int, distance=0) -> list:
    if len(students) != 0:
        rem_students = []
        t = len(students)
        for i in range(t):
            st = students.pop()
            for ws in workshops:
                if ws.schueler_hinzufuegen_max(st, avg, distance):
                    break
            rem_students.append(st)

        return rem_students


def keep_fill():
    pass


def do_stuff(students: list, workshops: list, distance: int) -> list:

    if distance == -1:
        distance = 10000000000
    elif distance < -1:
        raise ValueError("Parameter 'distance' must be positive int or '-1' for infinite distance.")

    avg = get_avg(students, workshops)

    first_fill(students, workshops)

    remain = first_remove(workshops, avg, distance)

    return second_fill(remain, workshops, avg, distance)
