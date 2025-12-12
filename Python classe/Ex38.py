"""Escriure un programa que ens permeti jugar a una versió simplificada del joc de MasterMind, el joc consisteix en crear un codi de 4 xifres i
 demanar a l’usuari que vagi introduint codis de 4 xifres fins que l’endevini. En cada jugada, li direm quants número ha encertat 
 (estan en la posició correcte) i quants coincideixen 
(i són, però no estan en la posició correcte)."""
import random
def generar_codi():
    codi = ""
    for _ in range(4):
        codi += str(random.randint(0, 9))
    return codi 
def avaluar_jugada(codi_secret, codi_usuari):
    encertats = 0
    coincidencies = 0
    codi_secret_usat = [False] * 4
    codi_usuari_usat = [False] * 4
    for i in range(4):
        if codi_usuari[i] == codi_secret[i]:
            encertats += 1
            codi_secret_usat[i] = True
            codi_usuari_usat[i] = True
    for i in range(4):
        if not codi_usuari_usat[i]:
            for j in range(4):
                if not codi_secret_usat[j] and codi_usuari[i] == codi_secret[j]:
                    coincidencies += 1
                    codi_secret_usat[j] = True
                    break
    return encertats, coincidencies
def jugar_mastermind():
    codi_secret = generar_codi()
    print("Benvingut al MasterMind! Intenta endevinar el codi de 4 xifres.")
    intents = 0
    while True:
        codi_usuari = input("Introdueix un codi de 4 xifres: ")
        if len(codi_usuari) != 4 or not codi_usuari.isdigit():
            print("Codi invàlid. Assegura't que té 4 xifres.")
            continue
        intents += 1
        encertats, coincidencies = avaluar_jugada(codi_secret, codi_usuari)
        print(f"Has encertat {encertats} xifres en la posició correcta i {coincidencies} xifres que coincideixen però no estan en la posició correcta.")
        if encertats == 4:
            print(f"Felicitats! Has endevinat el codi {codi_secret} en {intents} intents.")
            break
jugar_mastermind()
