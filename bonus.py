import pygame as pg
import random


class Bonus(pg.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        
        self.images = {}
        for i in range(4):
            self.images[game.bonus_list[i]] = pg.image.load(f"assets/Bonus/{game.bonus_list[i]}.png")
        
        self.percent = 0
        
        self.game = game
        
        self.total = random.randint(2000, 3000)
        
        self.moving = False
        
        self.waiting = False
        
        
    def start(self, name, x, speed):
        self.image = self.images[name]
        self.image = pg.transform.scale(self.image, (80, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = -5
        self.speed = speed
        self.percent = 0
        self.moving = True
        
        
    def move(self):
        if self.moving:
            self.rect.y += self.speed
            self.game.screen.blit(self.image, self.rect)
            
            
            if self.rect.y > self.game.screen.get_width():
                self.total = random.randint(2000, 3000)
                self.moving = False
                
            elif self.game.collision(self, self.game.players):
                self.bonus()
        
        else:
            if self.waiting:
                if self.load_bonus(360, (240, 10, 10), False):
                    self.reset()
                
            else:
                if self.load_bonus(self.total):
                    self.name = self.game.bonus_list[
                        random.randint(0, 3)
                    ]
                    self.start(self.name, random.randint(200, 880), random.randint(2, 5))
                
    def bonus(self):
        self.moving = False
        self.waiting = True
        if self.name == "Blast":
            self.game.ball.ball_img("blast")
            
        elif self.name == "Extend":
            self.game.player.image = pg.transform.scale(self.game.player.image, (160, 20))
            
        elif self.name == "Fast":
            self.fast = self.game.ball.speed
            self.game.ball.speed *= 2
            
        elif self.name == "Triple":
            self.waiting = False
            self.game.balls.add(self.game.spawn_balls(True))
            self.game.balls.add(self.game.spawn_balls(False))
            
            for ball in self.game.balls:
                ball.speed = self.game.ball.speed
            
    def reset(self):
        self.moving = False
        self.waiting = False
        self.percent = 0
        self.game.ball.ball_img("Ball")
        self.game.player.image = pg.transform.scale(self.game.player.image, (80, 20))
        
        if self.name == "Fast":
            self.game.ball.speed = self.fast
            
    def load_bonus(self, total, color = (235, 235, 106), loading = True):
        if loading:
            if self.game.playing:
                    self.percent += 1
                    
        else:
            self.percent += 1
            
        percent = (self.percent * 6.28) / total
        pg.draw.arc(self.game.screen, color, [40, 100, 70, 80], 0, percent, 40)
        
        if self.percent == total:
            return True
        else:
            return False