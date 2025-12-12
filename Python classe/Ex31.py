"""Escriure un programa on donats l’any actual, i l’any de naixement i el nom de 4 persones, calculi els anys que farà cada un d’ells l’any actual i imprimeixi totes les dades tabulades per pantalla. Ex:
Any actual 2022
Nom			Data naixement	Anys que farà aquest any
Pere			2000			22
Maria			1999			23
Anna			2005			17"""
any_actual = 2022
persones = [("Pere", 2000),
           ("Maria", 1999),
           ("Anna", 2005),
           ("Joan", 1985)] 
print("Any actual:", any_actual)
print("{:<15} {:<15} {:<20}".format("Nom", "Data naixement", "Anys que farà aquest any"))
for nom, any_naixement in persones:
    anys_que_fara = any_actual - any_naixement
    print("{:<15} {:<15} {:<20}".format(nom, any_naixement, anys_que_fara))