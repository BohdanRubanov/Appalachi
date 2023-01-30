import settings
import area 
import music
move_bullet = 0
flag_bullet_die = False
flag_bullet_shoot = False
class Bullet(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.STEP = 2
        self.MOVE_BULLET = False







    def bullet(self, sprite,medic, list_rect, derection = 1):
            global flag_bullet_die
            # global flag_pistol_shoot
            global flag_blit_bullet
            global move_bullet
            global flag_bullet_shoot

            if medic.X > 400:
                derection = -1
            else:
                derection = 1
            for block in list_rect:
                if block.X <= self.X + self.WIDTH and block.X + block.WIDTH > self.X + self.WIDTH:
                    if self.Y >= block.Y and self.Y + self.HEIGHT <= block.Y + block.HEIGHT:
                        self.MOVE_BULLET = False
                        music.pistol_shoot.stop()
                        break
                    else:
                        self.MOVE_BULLET = True
                        music.pistol_shoot.play()
                else:
                    self.MOVE_BULLET = True
            if self.MOVE_BULLET:
                if sprite.X <= self.X + self.WIDTH and sprite.X + sprite.WIDTH >= self.X:
                    if sprite.Y + 30 >= self.Y and sprite.Y + sprite.HEIGHT <= self.Y + self.HEIGHT + 30:
                        music.die_bullet_version.play()
                        self.MOVE_BULLET = False
                        flag_bullet_die = True
                        music.pistol_shoot.stop()
            if self.X <= 0:
                self.MOVE_BULLET = False
                music.pistol_shoot.stop()
            if self.X >= 800:
                self.MOVE_BULLET = False
                music.pistol_shoot.stop()

            
            if self.MOVE_BULLET:
                flag_bullet_shoot = True
                if move_bullet == 0:
                    move_bullet += 1
                if self.X >= 800 or self.X <= 0:
                    move_bullet = 0
                self.X += (5 + self.STEP)  * derection 