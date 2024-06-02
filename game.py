"""This is the module containing all the logic beside the game"""

import pygame as pg
import random as rd
from player import Player
from ball import Ball
from brick import Brick
from bonus import Bonus
from soundmanager import SoundManager as SM


class Game:
    """Ma classe Game 😛"""

    def __init__(self, screen):
        
        #Instancier les sons
        self.sound = SM()
        
        #Récupère l'écran
        self.screen = screen
        
        #initialise le jeu
        self.starting = True
        
        #Création du dictionnaire de couleurs pour les briques
        colors = ["Aqua", "Blue", "DarkGreen", "Green", "Orange", "Purple", "Red"]
        self.bricks_dic = {}
        a = 0
        for i in colors:
            image = pg.image.load(f"assets/Bricks/{i}.png")
            self.bricks_dic[a] = pg.transform.scale(image, (80, 30))
            a += 1
        
        #Crée un joueur et l'ajoute au groupe
        self.players = pg.sprite.Group()
        self.player = Player(self)
        self.players.add(self.player)
        
        #Crée une balle et la rajoute au groupe de balles
        self.balls = pg.sprite.Group()
        self.ball = self.spawn_balls(self)
        self.balls.add(self.ball)
                
        #Vérifie si le joueur lance la partie
        self.playing = False
        
        #Gère le score
        self.font = pg.font.SysFont("Arial Black", 25, True)
        
        #Les vies du joueur
        self.live_image = pg.image.load("assets/Hearth.png")
        self.live_image = pg.transform.scale(self.live_image, (30, 30))
        
        self.start()
        
        #Dictionnaire de bonus
        self.bonus_list = {
            1: "Blast",
            2: "Extend",
            3: "Fast",
            0: "Triple"
        }
        
        #Crée un bonus et l'ajoute au groupe de bonus
        self.bonus_group = pg.sprite.Group()
        self.bonus = Bonus(self)
        self.bonus_group.add(self.bonus)
        
        
        
    def spawn_balls(self, right = rd.choice([False, True, False, True])):
        return Ball(self, right)
        
    def show_score(self):
        scrore_text = self.font.render(f"Level : {self.score}", 1, (0, 0, 0))
        self.screen.blit(scrore_text, (5, 20))
        
    def show_lives(self):
        for i in range(self.live):
            self.screen.blit(self.live_image, (5 + (i*30), 50))
        
    def spawn_brick(self):
        self.bricks = pg.sprite.Group()
        # self.bricks.add(Brick(self, 140, 0))
        x = 140
        y = 0
        for i in range(5):
            for j in range(10):
                self.bricks.add(Brick(self, x, y))
                x += 80
            y += 30
            x = 140
            
    def start(self):
        self.live = 3
        self.score = 1
        self.ball.speed = 10
        self.playing = True
        self.ball.launch()
        
        #Crée les briques et les ajoute au groupe
        self.spawn_brick()
        
    def restart(self):
        self.playing = True
        self.ball.launch()
        
    def update(self):
        #Appliquer les briques
        self.bricks.draw(self.screen)
        
        #Appliquer le joueur
        self.players.draw(self.screen)
        
        #Dessine la balle
        self.balls.draw(self.screen)
        
        #Déplacements de la balle et du joueur
        self.player.move()
        
        for ball in self.balls:
            ball.move()
        
        #Afficher le score
        self.show_score()
        
        #Afficher les vies
        self.show_lives()
        
        self.bonus.move()
        
    def collision(self, sprite, group):
        return pg.sprite.spritecollide(sprite, group, False, pg.sprite.collide_mask)
        
    def victory(self):
        self.score += 1
        self.ball.speed *= 1.15
        self.spawn_brick()
        if self.live < 4:
            self.live += 1
            
        self.playing = False
        
    def game_over(self):
        self.playing = False
        self.starting = True  
        self.bonus.waiting = False
        self.bonus.moving = False
        self.bonus.percent = 0     