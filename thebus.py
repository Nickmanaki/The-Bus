def menu():
    print "1. Empty seats", "\n", "2. Reservation", "\n", "3. Window seat reservation", "\n", "4. Cancel reservation", "\n", "5. Reserved seats", "\n", "6. Bus diagram", "\n", "7. End programme"


def emptyseats(lista):
    c = 0
    for i in lista:
        if i == 0:
            c += 1
    return c


def reserved(thesi, listaa):
    if listaa[thesi-1] == 1:
        ans = True
    else:
        ans = False
    return ans


def reserve(lista, seats):
    if 0 not in lista:
        answer = False
        seat = 1
        print "Bus is full :)"
    else:
        answer = True
    while answer:
        seat = input("Poia thesi thes?: ")
        while seat < 1 or seat > seats:
            seat = input("Poia thesi thes re?: ")
        answer = reserved(seat, lista)
        if answer:
            print "H thesi einai kratimenh! Go again"
    lista[seat-1] = 1
    return lista


def windowreserve(lista,seats):
    windowseats = []
    for i in range(1, seats, 4):
        if i == 1:
            windowseats.append(i)
        else:
            windowseats.append(i - 1)
            windowseats.append(i)
        if i == seats-4:
            windowseats.append(i+4)
    found = False
    for j in windowseats:
        if lista[j - 1] == 0 and not found:
            lista[j - 1] = 1
            found = True
            if found:
                print "Brethike thesh", j
    if not found:
        print "den brethike thesi"
    return lista


def cancelreservation(lista, seats):
    if 1 not in lista:
        answer = True
        seat = 1
        print "Bus is empty :)"
    else:
        answer = False
    while not answer:
        seat = input("Poia thesi na akyrothei?: ")
        while seat < 1 or seat > seats:
            seat = input("Poia thesi na akyrothei re?: ")
        answer = reserved(seat, lista)
        if not answer:
            print "H thesi den einai piasmenh blaka"
    lista[seat-1] = 0
    return lista


def reservedseats(lista):
    print "Reserved Seats: "
    for i in range(len(lista)):
        if lista[i] == 1:
            print i+1,;
    print "\n"


def diagram(lista, plate, seats):
    print plate
    parlista = []
    for i in range(len(lista)):
        if lista[i] == 0:
            parlista.append("-")
        else:
            parlista.append("X")
    for i in range(0, len(lista) - 5, 4):
        print parlista[i], parlista[i + 1], " ", parlista[i + 2], parlista[i + 3]
    for i in range(seats-5, seats):
        print parlista[i],;
    print "\n"


cwrong = 0
plate = raw_input("Dose pinakida: ")
seatnum = input("Dose theseis: ")

while (seatnum % 4 != 1 or seatnum/4 > 13) or seatnum <= 5 and cwrong < 9:
    seatnum = input("Dose theseis re: ")
    cwrong += 1

if cwrong == 10:
    print "Eisai blakas"

seats = []

for i in range(seatnum):
    seats.append(0)

choice = "I can do this in python :)"

while choice != 7:
    menu()
    choice = input("Ti tha itheles na kaneis? (1-7): ")
    if choice == 1:
        empty = emptyseats(seats)
        print empty
    elif choice == 2:
        seats = reserve(seats, seatnum)
    elif choice == 3:
        seats = windowreserve(seats, seatnum)
    elif choice == 4:
        seats = cancelreservation(seats, seatnum)
    elif choice == 5:
        reservedseats(seats)
    elif choice == 6:
        diagram(seats, plate, seatnum)
    else:
        print "We cooked"

print "We made a 3 michelin star dish"

