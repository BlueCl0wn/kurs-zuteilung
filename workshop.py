
class Workshop:
    """
    Eine Klasse, die eine Workshop darstellt.
    """
    def __init__(self, name: str, plaetze: int):
        self.name = name
        self.plaetze = plaetze

        self.students = []

    def schueler_hinzufuegen_generell(self, teilnehmer: object, size: int, avg: int, distance: int) -> bool:
        """
        Fügt einen Teilnehmer zum Workshop hinzu, wenn folgende Bedingungen erfüllt sind:
            - Die maximale Teilnehmeranzahl ist noch nicht erreicht.
            - Die erwartete Anzahl an Personen pro Workshop bei gleichmäßiger Verteilung ist nicht erreicht.

        :param teilnehmer: Liste mit Teilnehmern
        :param size: Erlaubte Anzahl an Teilnehmern
        :param avg: Zu erwartende Anzahl an Personen pro Workshop bei gleichmäßiger Verteilung.
        :param distance: Erlaubte Variation um die bei gleicher Verteilung zu erwartende Anzahl an Personen pro Workshop.
        :return: bool ob geklappt
        """
        if len(self.students) < size and len(self.students) < avg + distance:
            self.students.append(teilnehmer)
            return True
        else:
            return False

    def schueler_hinzufuegen_max(self, teilnehmer: object, avg: int, distance: int) -> bool:
        """
        Spezifizierung von 'schueler_hinzufuegen_generell'.

        'size' ist automatisch die maximal erlaubte Teilnehmeranzahl.

         siehe docs von 'schueler_hinzufuegen_generell' für weitere Infos
        """
        return self.schueler_hinzufuegen_generell(teilnehmer, self.plaetze, avg, distance)

    def schueler_hinzufuegen_inf(self, student: object) -> bool:
        """
        Spezifizierung von 'schueler_hinzufuegen_generell'.

        'size' und 'avg' sind automatisch Unendlich.

         siehe docs von 'schueler_hinzufuegen_generell' für weitere Infos
        """
        return self.schueler_hinzufuegen_generell(student, size=10000000000, avg=10000000000, distance=0)

    def get_length(self):
        """
        berechnet Teilnehmeranzahl
        :return:
        """
        return len(self.students)

    def within_distance(self, avg: int, distance=0) -> int:
        """
        Berechnet Abstand zu maximalen Teilnehmeranzahl bzw. der durchschnittlichen Teilnehmernazahl.

        Positiver Wert heißt, es sind zu viele vorhanden.

        :param avg: Zu erwartende Anzahl an Personen pro Workshop bei gleichmäßiger Verteilung.
        :param distance: Erlaubte Variation um die bei gleicher Verteilung zu erwartende Anzahl an Personen pro Workshop.
        :return: int
        """
        if avg > self.plaetze:
            return self.get_length() - self.plaetze
        else:
            return self.get_length() - (avg + distance)
