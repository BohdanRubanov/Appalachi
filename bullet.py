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
                    # print(1111111111)
                    if self.Y >= block.Y and self.Y + self.HEIGHT <= block.Y + block.HEIGHT:
                        print(33333333333333333)
                        self.MOVE_BULLET = False
                        music.pistol_shoot.PISTOL_SHOOT.stop()
                        # flag_blit_bullet = False
                        break
                    else:
                        self.MOVE_BULLET = True
                        music.pistol_shoot.PISTOL_SHOOT.play()
                else:
                    self.MOVE_BULLET = True
                    # music.pistol_shoot.PISTOL_SHOOT.play()
            if self.MOVE_BULLET:
                # print("erhbhUIWRHOIQHOUE")
                if sprite.X <= self.X + self.WIDTH and sprite.X + sprite.WIDTH >= self.X:
                # print(222222222222222)
                    if sprite.Y + 30 >= self.Y and sprite.Y + sprite.HEIGHT <= self.Y + self.HEIGHT + 30:
                        # print("ulygiguoviuo")
                        music.die_bullet_version.DIE_BULLET_VERSION.play()
                        
                        # print(6666666666666)
                        self.MOVE_BULLET = False
                        flag_bullet_die = True
                        music.pistol_shoot.PISTOL_SHOOT.stop()
            if self.X <= 0:
                self.MOVE_BULLET = False
                music.pistol_shoot.PISTOL_SHOOT.stop()
                # print(4444444444444)
            if self.X >= 800:
                self.MOVE_BULLET = False
                music.pistol_shoot.PISTOL_SHOOT.stop()
    
                # print(55555555555)

            
            if self.MOVE_BULLET:
                flag_bullet_shoot = True
                # for i in range(1):
                if move_bullet == 0:
                    move_bullet += 1
                if self.X >= 800 or self.X <= 0:
                    move_bullet = 0
                # print(111111)
                self.X += (5 + self.STEP)  * derection 
    # def blit_sprite(self,win):
    #     win.blit(self.IMAGE, (self.X,self.Y))