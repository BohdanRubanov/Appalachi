import pygame
import os
class Sound:
    def __init__(self, sound_path = None, volume = None):
        self.SOUND = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + '/..'), sound_path))
        self.SOUND.set_volume(volume)
    def play(self):
        self.SOUND.play()
    def stop(self):
        self.SOUND.stop()
class Music:
    def __init__(self, music_path = None, volume = None):
        self.VOLUME = volume
        self.MUSIC_PATH = music_path
    def load(self):
        pygame.mixer.music.load(self.MUSIC_PATH)
        pygame.mixer.music.set_volume(self.VOLUME)
    def unload(self):
        pygame.mixer.music.unload()
    def play(self, repeat):
        pygame.mixer.music.play(loops = repeat)
    def stop(self):
        pygame.mixer.music.stop()
die_bullet_version = Sound('sounds/die_bullet_version.wav', 0.5)
pistol_shoot = Sound('sounds/pistol_shoot.wav', 0.5)
die_smoke_version = Sound('sounds/die_smoke_version.wav', 0.5)
menu_background_sound = Music('sounds/menu_background_song.wav', 0.5)
level1_background_sound = Music('sounds/level1_background_song.wav', 0.5)
level2_background_sound = Music('sounds/level2_background_song.wav', 0.5)





























#би па па парапум, па па парапум пара бара пиииии па па пара бу




