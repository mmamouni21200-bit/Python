"""Crear el joc d’arkanoid utilitzant la llibreria pygame.
Enllaç a les imatges que heu de posar al mateix directori que el fitxer.
Canviar la ruta absoluta de les imatges /home/cicles/AO/Tasca11/Nom.png
Es comença pitjant la barra d’espai i es juga pitjant les fletxes esquerra i dreta.
"""
import pygame
import sys
# Inicialitzar Pygame
pygame.init() 
# Configuració de la finestra
amplada = 800
altura = 600  
finestra = pygame.display.set_mode((amplada, altura))
pygame.display.set_caption("Arkanoid")
# Colors
NEGRE = (0, 0, 0)
BLANC = (255, 255, 255)
# Raqueta
raqueta_amplada = 100
raqueta_alçada = 20
raqueta_x = (amplada - raqueta_amplada) // 2
raqueta_y = altura - 40
raqueta_velocitat = 10
# Pilota
pilota_radius = 10
pilota_x = amplada // 2
pilota_y = altura // 2
pilota_velocitat_x = 5
pilota_velocitat_y = -5
pilota_moving = False   
# Blocs
blocs = []
bloc_amplada = 75
bloc_alçada = 30
for fila in range(5):
    for columna in range(10):
        bloc_x = columna * (bloc_amplada + 5) + 35
        bloc_y = fila * (bloc_alçada + 5) + 50
        blocs.append(pygame.Rect(bloc_x, bloc_y, bloc_amplada, bloc_alçada))
# Bucle principal del joc
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pilota_moving = True
    # Moure la raqueta
    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT] and raqueta_x > 0:
        raqueta_x -= raqueta_velocitat
    if tecles[pygame.K_RIGHT] and raqueta_x < amplada - raqueta_amplada:
        raqueta_x += raqueta_velocitat
    # Moure la pilota
    if pilota_moving:
        pilota_x += pilota_velocitat_x
        pilota_y += pilota_velocitat_y
    # Col·lisions amb les parets
    if pilota_x <= pilota_radius or pilota_x >= amplada - pilota_radius:
        pilota_velocitat_x = -pilota_velocitat_x
    if pilota_y <= pilota_radius:
        pilota_velocitat_y = -pilota_velocitat_y
    if pilota_y >= altura - pilota_radius:
        pilota_moving = False
        pilota_x = amplada // 2
        pilota_y = altura // 2
    # Col·lisió amb la raqueta
    raqueta_rect = pygame.Rect(raqueta_x, raqueta_y, raqueta_amplada, raqueta_alçada)
    if raqueta_rect.collidepoint(pilota_x, pilota_y + pilota_radius):
        pilota_velocitat_y = -pilota_velocitat_y
    # Col·lisions amb els blocs
    for bloc in blocs[:]:
        if bloc.collidepoint(pilota_x, pilota_y - pilota_radius):
            blocs.remove(bloc)
            pilota_velocitat_y = -pilota_velocitat_y
            break
    # Dibuixar tot
    finestra.fill(NEGRE)
    pygame.draw.rect(finestra, BLANC, raqueta_rect)
    pygame.draw.circle(finestra, BLANC, (pilota_x, pilota_y), pilota_radius)
    for bloc in blocs:
        pygame.draw.rect(finestra, BLANC, bloc)
    pygame.display.flip()
    pygame.time.delay(30)           