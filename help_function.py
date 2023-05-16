# input number from 0 to 12, return motnh name
import numpy as np


def getMonthName(monthNumber):
    return {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }.get(monthNumber, "Invalid month")

def oblicz_ile_mam_wydatkow(musze_zaplacic):
    musze_zaplacic_np = np.array(musze_zaplacic)
    values = musze_zaplacic_np[:,1].astype(int)
    sum_of_all_expenditures = np.sum(values)
    return sum_of_all_expenditures


def urlop_material(musze_zaplacic):
    # get only the second column

    wydatik = oblicz_ile_mam_wydatkow(musze_zaplacic)

    konto = 686 - 25 + 180
    kasa = wydatik + konto

    litry = 120
    cena = 1.71

    benzyna = cena * litry / 2
    hotel = 180
    restauracje = 75
    zakupy_do_domu = 50
    jedzenie = restauracje + zakupy_do_domu
    atrakcje = 70

    urlop = benzyna + hotel + jedzenie + atrakcje

    budget = kasa - urlop
    print(budget)
