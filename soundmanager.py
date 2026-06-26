import pygame as pg
from imgloader import resource_path


class SoundManager:
    
    def __init__(self):
        self.sounds = {
            'break' : pg.mixer.Sound(resource_path("assets/Sounds/break.mp3")),
            'bound' : pg.mixer.Sound(resource_path("assets/Sounds/bound.mp3")),
            'die' : pg.mixer.Sound(resource_path("assets/Sounds/die.mp3")),
            'game' : pg.mixer.Sound(resource_path("assets/Sounds/font.mp3"))
        }
        
        
    def play(self, name):
        self.sounds[name].play()