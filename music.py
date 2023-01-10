import pygame
import os
class Sounds:
    def __init__(self, sound = None):
        self.DIE_BULLET_VERSION = sound
        self.DIE_BULLET_VERSION = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), 'sounds/die_bullet_version.wav'))
        self.PISTOL_SHOOT = sound
        self.PISTOL_SHOOT = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), 'sounds/pistol_shoot.wav'))
        self.DIE_SMOKE_VERSION = sound
        self.DIE_SMOKE_VERSION = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), 'sounds/die_smoke_version.wav'))
die_bullet_version = Sounds('sounds/die_bullet_version.wav')
pistol_shoot = Sounds('sounds/pistol_shoot.wav')
die_smoke_version = Sounds('sounds/die_smoke_version.wav')