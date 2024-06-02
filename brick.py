import pygame as pg
import random as rd


class Brick(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
            
        #Choix aléatoire de la couleur
        color = rd.randint(0, 6)
        self.image = self.game.bricks_dic[color]
        
        #positionnement de la brique
        self.rect = self.image.get_rect()
        # print(self.rect)
        self.rect.x = x
        self.rect.y = y
        
    def destroy(self):
        self.game.bricks.remove(self)
        self.game.sound.play("break")

            
        