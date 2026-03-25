F1 = ["F1", "VW Off-Road-Bug", 185, (104,142), 6000, 9, 1880, 4]
D3 = ["D3", "Seat Toledo Marathon", 220, (195,330), 8400, 5.2, 2100, 5]
F2 = ["F2", "Mitsubishi Galant", 180, (216, 294), 5800, 6.3, 3395, 4]
E1 = ["E1", "Mitsubishi Carisma GT", 225, (213, 290), 6000, 5.2, 1996, 4]
F3 = ["F3", "Renault Megane", 218, (198, 270), 8400, 5.9, 1995, 4]
G4 = ["G4", "Fait Punto Kit-Car", 165, (161, 220), 7500, 9.8, 1600, 4]
E3 = ["E3", "Skoda Octavia WRC", 230, (221, 300), 7500, 5.3, 2000, 4]
D2 = ["D2", "Toyota Celia GT-Four", 245, (220, 299), 5600, 5.3, 1998, 4]
C1 = ["C1", "Subaru Impreza WRC", 220, (221, 300), 5500, 5.4, 1994, 4]
G3 = ["G2", "Mitsibishi Pajero", 185, (153, 208), 7000, 9.6, 3497, 6]

cars = [F1, D3, F2, E1, F3, G4, E3, D2, C1, G3]


def print_car(c):
    print("__________________________")
    print(f"|{c[0]}      {c[1]} |")
    print(f"|speed:{c[2]}        0-60: {c[5]}|")
    print(f"|Hp:{c[3]}  CCs: {c[6]}|")
    print(f"|RRM:{c[4]}    Cylinders: {c[7]}|")
    print("|________________________|")

i = 1
for car in cars:
    print(i, car[1])
    i += 1

while True:
    choice = int(input("Select car number(stop if want to end): "))
    print_car(cars[choice-1])
    if choice == 1:
        print(i, car[1])
