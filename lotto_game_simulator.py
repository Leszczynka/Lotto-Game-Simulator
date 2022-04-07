from random import randint


def take_numbers():
    return int(input("Podaj liczbę: "))


def drukuj_kupon():
    kupon = []
    while len(kupon) < 6:
        typowany_numer = take_numbers()
        if typowany_numer not in kupon:
            kupon.append(typowany_numer)
        else:
            print("Już podałeś tą liczbę. Wytypuj inną.")
    return set(kupon)


def losowanie_lotto():
    wylosowane = []
    liczba_wylosowanych_liczb = 0
    while liczba_wylosowanych_liczb < 6:
        wylosowana_liczba = randint(1, 50)
        if wylosowana_liczba in wylosowane:
            wylosowana_liczba = randint(1, 50)
        wylosowane.append(wylosowana_liczba)
        liczba_wylosowanych_liczb += 1
    return set(wylosowane)


def sprawdz():
    if len(drukuj_kupon() & losowanie_lotto()) == 6:
        return "Trafiłeś 6 w lotto!"
    else:
        return "Nie tym razem..."


print(sprawdz())