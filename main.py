## import import getMonthName from help_function
from help_function import getMonthName, oblicz_ile_mam_wydatkow

import numpy as np
musze_zaplacic =  [
    ["Mita", 	        -380],
    ["AOK",		        -121],
    ["internet", 	    -15],
    ["Tel Optional",    -25],
    ["Jedzenie", 	    -450],
    ["Youtube",  	    -7],
    ["kawa", 	        -30],
    ["ciuchy", 	        -50],
    ["Fidor", 	        -5],
    ["Radio",           -8],
    ["urlop", -100],
    ["Studien gebühren", -70]
]



zarobki = [["Mama+", +180], ["CCP", 86 * 16.5 * 0.91]]



def print_budget_management():
    print("Miesiac" + getMonthName(i % 12))
    print("Przychod: ", przychod )
    print( "Wydatki: ", wydatki )
    print("Diff", int(przychod + wydatki))
    print("etoro:" + str(etoro))
    print("odlozone na Urlob:" + str(na_urlaub))
    print("odlozone na Studia:" + str(na_studien))
    print("Wrzystko Razem" + str(etoro + na_urlaub))
    print("");


etoro = 1200
na_urlaub = 0
na_studien = 0

for i in range(1,2):
    wydatki = 0
    przychod = 0

    for x in zarobki:
        przychod += x[1]

    for x in musze_zaplacic:
        wydatki += x[1]

    # na_urlaub += 100
    # na_studien += 151

    etoro = etoro + przychod + wydatki



    print_budget_management()

