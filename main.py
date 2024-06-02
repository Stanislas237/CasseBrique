import pygame as pg
import random as rd
from game import Game

pg.init()

#Définir une clock
clock = pg.time.Clock()
FPS = 60

#Créer la fenêtre
pg.display.set_caption("Casse Briques By Stan.co")
screen = pg.display.set_mode((1080, 600))

#Charger le background

i = rd.randint(1, 5)
background = pg.image.load(f"assets/Backgrounds/bg-{i}.jpg")

#Cherger la bannière et le bouton Start
banner = pg.image.load("assets/Banner.png")
banner = pg.transform.scale(banner, (200, 100))
banner_rect = banner.get_rect()
banner_rect.centerx = screen.get_width() / 2
banner_rect.y = 100

start = pg.image.load("assets/Start.png")
start = pg.transform.scale(start, (150, 100))
start_rect = start.get_rect()
start_rect.centerx = screen.get_width() / 2
start_rect.y = 200

#Charger la classe Game
game = Game(screen)
game.sound.play("game")
sound_loop = 0

running = True

while running:
    sound_loop += 1
    if sound_loop == 3060:
        game.sound.play("game")
        sound_loop = 0
    
    
    #Appliquer le background
    screen.blit(background, (0, 0))
    
    #Créer la zone de jeu
    pg.draw.lines(screen, (0, 0, 0), True, [(140, 0), (940, 0), (940, 600), (140, 600)], 5)

    #Appeler la méthode Update
    if not game.starting:
        game.update()
        
    else:
        #Appliquer la bannière
        screen.blit(banner, banner_rect)
        
        #Appliquer le bouton Start
        screen.blit(start, start_rect)

    #mettre à jour l'écran
    pg.display.flip()
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            print("Le jeu se ferme")
            
        elif pg.mouse.get_pressed()[0]:
            #Vérifier si la souris clique sur le bouton play
            if start_rect.collidepoint(event.pos) and game.starting:
                game.start()
                game.starting = False
                game.playing = False
                
            elif not game.playing and not game.starting:
                game.restart()
                     
    #fixer le nbre de FPS sur la clock
    clock.tick(FPS)