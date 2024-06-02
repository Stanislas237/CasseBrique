import pygame as pg


class Player(pg.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pg.image.load("assets/Player.png")
        self.image = pg.transform.scale(self.image, (80, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = game.screen.get_width() / 2
        self.rect.centery = game.screen.get_height() - 30
        
    def move(self):
        mouse_pos = pg.mouse.get_pos()
        self.diff = self.rect.width / 2
        
        if 140 + self.diff <= mouse_pos[0] and mouse_pos[0] + self.diff <= 940:
            self.rect.centerx = mouse_pos[0]