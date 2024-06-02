import pygame as pg



class SoundManager:
    
    def __init__(self):
        self.sounds = {
            'break' : pg.mixer.Sound("assets/Sounds/break.mp3"),
            'bound' : pg.mixer.Sound("assets/Sounds/bound.mp3"),
            'die' : pg.mixer.Sound("assets/Sounds/die.mp3"),
            'game' : pg.mixer.Sound("assets/Sounds/font.mp3")
        }
        
        
    def play(self, name):
        self.sounds[name].play()