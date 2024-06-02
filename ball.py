import pygame as pg
import random as rd
import math


class Ball(pg.sprite.Sprite):
    
    def __init__(self, game, right):
        super().__init__()
        self.game = game
        self.speed = 10
        self.angle = 45
               
        self.images = {
            "Ball": pg.image.load("assets/Ball.png"),
            "blast" : pg.image.load("assets/blast.png")
        }
        
        self.ball_img("Ball")
        self.rect = self.image.get_rect()
        # self.rect = self.image.get_rect(center=self.rect.center)
        
        self.screen_h = self.game.screen.get_height()
        
        #Positionne la balle
        self.ball_pos()
        self.launch()
        
        self.up = True
        self.right = right
        
            
    def ball_pos(self):
        self.rect.centerx = self.game.player.rect.centerx
        self.rect.centery = self.game.player.rect.centery - 25
            
    def ball_img(self, name):
        self.image = self.images[name]
        self.image = pg.transform.scale(self.image, (20, 20))
        self.base_pic = self.image
        self.name = name
            
    def move(self):
        if not self.game.playing:
            self.ball_pos()
            
        else:
            #Déplacement de la balle
            self.rect.centerx += self.speed * math.sin(math.radians(self.angle))
            self.rect.centery -= self.speed * math.cos(math.radians(self.angle))
            
            for brick in self.game.collision(self, self.game.bricks):
                brick.destroy()
                if self.name == "Ball":
                    self.up = False
                    self.find_direction()
                
                if len(self.game.bricks) == 0:
                    self.game.victory()
                
            if self.game.collision(self, self.game.players) and (self.rect.bottom > self.game.player.rect.top):
                self.up = True
                self.rect.centery -= 3
                self.find_direction()
                self.game.sound.play("bound")
                
            if self.rect.x < 140:
                self.right = True
                self.rect.centerx += 3
                self.find_direction()
                self.game.sound.play("bound")
            
            if (self.rect.right > 940):
                self.right = False
                self.rect.centerx -= 3
                self.find_direction()
                self.game.sound.play("bound")
            
            if self.rect.y <= 0:
                self.up = False
                self.rect.centery += 3
                self.find_direction()
                self.game.sound.play("bound")
                
            elif self.rect.y >= self.screen_h:
                self.up = True
                
                if self.name == "Ball":
                    if len(self.game.balls) == 1:
                        self.game.sound.play("die")
                        if self.game.live > 0:
                            self.game.live -= 1
                            self.game.playing = False
                        else:
                            self.game.game_over()
                    
                    else:
                        self.destroy()
                    
                else:
                    self.rect.centery -= 3
                    self.find_direction()
            
    def launch(self):
        self.right = rd.choice([False, True, False, True])
                    
    def destroy(self):
        self.game.balls.remove(self)
        for ball in self.game.balls:
            self.game.ball = ball
        
    def find_direction(self):
        #Direction en fonction de l'orientation
        if self.up:
            if self.right:
                self.angle = rd.randint(40, 50)
            else:
                self.angle = - rd.randint(40, 50)
                
        else:
            if self.right:
                self.angle = 180 - rd.randint(40, 50)
            else:
                self.angle = 180 + rd.randint(40, 50)