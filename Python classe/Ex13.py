def menu_principal():
    opcio=0
    while opcio<1 or opcio>3: 
        opcio=int(input("""Elegeix una opció:
                    1. Calculadora decimal
                    2. Calculadora real (floats)
                    3. Sortir \n"""))
        if opcio>0 and opcio<4:
             return opcio
        else:
            print("L'opcio seleccionada no és correcte, torn-ho a provar!!\n")
def menu_calculadora():
    opcio=0
    while opcio<1 or opcio>5:
        opcio=int(input("""Elegeixi una opció:
                1. Suma
                2. Resta
                3. Multiplicació
                4. Divisió
                5. Sortir 
                """))
        if opcio>0 and opcio<6:
            return opcio 
        else:
            print("Gràcies per utilitzar la meva calculadora, fins un altre dia!\n")
def calculadora_decimal(opcio):
    if opcio>0 and opcio<5:
        a= int(input("Introdueix el primer numero:"))
        b= int(input("Introdueix el segon numero:"))
    match(opcio):
        case 1:
            #Suma
            print("Estic fent la suma!\n")
            c= a+b
            print("El resultat de suma {} + {}és {}".format(a, b, c))
        case 2:
            #Resta
            print("Estic fent la resta!\n")
            c= a-b
            print("El resultat de resta {} - {}és {}".format(a, b, c))
        case 3:
            #multiplicacio
            print("Estic fent la multiplicació!\n")
            c= a*b
            print("El resultat de multiplicació {} * {}és {}".format(a, b, c))
        case 4:
            #Divisió
            print("Estic fent la divisió!\n")
            c= a//b
            print("El resultat de divisió {} // {}és {}".format(a, b, c))
        case _:
            print("Opció no vàlida! Torni_ho a provar!\n")        
def calculadora_real(opcio):
    if opcio>0 and opcio<5:
        a= float(input("Introdueix el primer numero:"))
        b= float(input("Introdueix el segon numero:"))
    match(opcio):
        case 1:
            #Suma
            print("Estic fent la suma!\n")
            c= a+b
            print("El resultat de suma {} + {}és {}".format(a, b, c))
        case 2:
            #Resta
            print("Estic fent la resta!\n")
            c= a-b
            print("El resultat de resta {} - {}és {}".format(a, b, c))
        case 3:
            #multiplicacio
            print("Estic fent la multiplicació!\n")
            c= a*b
            print("El resultat de multiplicació {} * {}és {}".format(a, b, c))
        case 4:
            #Divisió
            print("Estic fent la divisió!\n")
            c= a/b
            print("El resultat de divisió {} / {}és {}".format(a, b, c))
        case _:
            print("Opció no vàlida! Torni_ho a provar!\n")        

# Programa Principal

op=1
while op!=0:
    op=menu_principal()
    if op==1:
        # Calculadora decimal
        print("Estic passant per la calculadora decimal!\n")
        calculadora_decimal(menu_calculadora())
    elif op==2:
        # Calculadora real
        print("Estic passant per la calculadora real!\n")
        calculadora_real(menu_calculadora())
    else:
        print("Gràcies per a utilitzar la meva calculadora, fins un altre dia!\n")
        op=0
