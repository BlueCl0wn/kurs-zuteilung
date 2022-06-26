from workshop import Workshop

kurse = ["Tanzen", "Boxen", "Rhönrad", "Tischtennis", "Handball", "Fußball", "Salsa", "Schwimmen", "Sprinten",
         "Karate"]

workshops = []

for i in kurse:
    workshops.append(Workshop(i, 15))
