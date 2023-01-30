import settings
import pygame
import area 
import dicts
import os 
import bullet
import music
import random
# from bullet import blit_bullet_count
list_letters = ["q", "w", "e", "r", "t", "y", "u","x", "c", "f"]
list_cor_x = [150, 200, 220, 300, 350, 370]
list_cor_y = [300, 350, 440, 580, 620, 700]
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
flag_bullet_die = False
flag_level_3 = False
letter = ""
bullet1 = bullet.Bullet(
                    x = 0,
                    y = 0,
                    width= 0,
                    height= 0,
                    name_image= None
                )
        
class Sprite(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.COUNT_BULLET = 0
        self.LIST_BULLET = []
        self.STEP = 2
        self.GRAVITY = 6
        self.ACTIVE_GRAVITY = True
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True
        self.COUNT_JUMP = 0
        self.JUMP = False
        self.KEY_PRESSED = False
        self.OPEN_DOOR = False
        self.MASK_ON = False
        self.INJURED = False
        self.EXIT_DOOR = False
        self.MEDIC_MOVE_RIGHT = False
        self.MEDIC_MOVE_LEFT = False
        self.MOVE_BULLET = False
        self.DIRECTION = "R"
        self.SPEED_ANIMATION = 0
        self.COUNT_IMG = 3
        self.COUNT_FIRE_POSITION = 0
        self.EXTING_ON = False
        self.BLIT_FIRE_1 = True
        self.BLIT_FIRE_2 = True
        self.BLIT_FIRE_3 = True
        self.BLIT_FIRE_4 = True
        self.BLIT_FIRE_5 = True
        self.BLIT_FIRE_6 = True
        self.BLIT_FIRE_7 = True
        self.BLIT_FIRE_8 = True
        self.BLIT_FIRE_9 = True
        self.BLIT_FIRE_10 = True
        self.BLIT_FIRE_11 = True
        self.BLIT_FIRE_12 = True
        self.BLIT_FIRE_13 = True
        self.BLIT_FIRE_14 = True
        self.SCENE4 = False
        self.COUNT_FIRE_POSITION = 0
        self.EXTING_ON = False
        self.BLIT_FIRE_1 = True
        self.BLIT_FIRE_2 = True
        self.BLIT_FIRE_3 = True
        self.BLIT_FIRE_4 = True
        self.BLIT_FIRE_5 = True
        self.BLIT_FIRE_6 = True
        self.BLIT_FIRE_7 = True
        self.HOLE_COUNT = True
        self.ENTER_DOOR = False
        self.TIME_HOLE_BLIT = 0
        self.SCENE5 = False
        self.BLUE = False
        self.FLAG_BLUE = True
        self.DEATH_FIRE = False
        self.FLAG_DEATH_FIRE = True
        self.NO_FIRE = False
    def move_sprite(self):
        if not self.MASK_ON and not self.INJURED and not self.EXTING_ON:
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                self.DIRECTION = 'R'
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player",count_while=5,last_img= 5, first_img=1) 
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
               
                self.DIRECTION = 'L'
                if self.CAN_MOVE_LEFT == True:      
                    self.X -= self.STEP      
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player",count_while=5,last_img= 5, first_img=1) 
            elif self.ACTIVE_GRAVITY == False:
                self.NAME_IMAGE = "game2/images/player/1.png"
                self.direction()
        if self.MASK_ON and not self.INJURED and not self.EXTING_ON:
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                self.DIRECTION = 'R'
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player_mask",count_while=5,last_img= 5, first_img=1) 
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
               
                self.DIRECTION = 'L'
                if self.CAN_MOVE_LEFT == True:      
                    self.X -= self.STEP      
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player_mask",count_while=5,last_img= 5, first_img=1)
            elif self.ACTIVE_GRAVITY == False:
                self.NAME_IMAGE = "game2/images/player_mask/1.png"
                self.direction()
        if self.INJURED and not self.EXTING_ON:
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                self.DIRECTION = 'R'
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player_with_injured",count_while=5,last_img= 5, first_img=1) 
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
                self.DIRECTION = 'L'
                if self.CAN_MOVE_LEFT == True:      
                    self.X -= self.STEP      
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player_with_injured",count_while=5,last_img= 5, first_img=1)
            elif self.ACTIVE_GRAVITY == False:
                self.NAME_IMAGE = "game2/images/player_with_injured/1.png"
                self.direction()
        if self.EXTING_ON:
            event = pygame.key.get_pressed()
            if event[pygame.K_RIGHT] and self.X + self.WIDTH <= dicts.SETTINGS_WIN["WIDTH"]:
                self.DIRECTION = 'R'
                if self.CAN_MOVE_RIGHT == True:
                    self.X += self.STEP
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player_with_exting",count_while=5,last_img= 5, first_img=1) 
            elif event[pygame.K_LEFT] and self.X + 1 >= 0:   
                self.DIRECTION = 'L'
                if self.CAN_MOVE_LEFT == True:      
                    self.X -= self.STEP      
                if self.ACTIVE_GRAVITY == False and self.JUMP == False:
                    self.animation(folder= "player_with_exting",count_while=5,last_img= 5, first_img=1)
            elif self.ACTIVE_GRAVITY == False:
                self.NAME_IMAGE = "game2/images/player_with_exting/1.png"
                self.direction()
     
    def jump(self, list_rect):
        if not self.MASK_ON and not self.INJURED and not self.EXTING_ON:
            event = pygame.key.get_pressed()
            #
            if event[pygame.K_UP] and self.KEY_PRESSED == False:
                self.KEY_PRESSED = True

            if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
                if self.COUNT_JUMP <= 25:
                    self.NAME_IMAGE = "game2/images/player/6.png"
                else: 
                    self.NAME_IMAGE = "game2/images/player/8.png"
                self.direction()
                self.JUMP = True
                self.COUNT_JUMP += 1
                self.Y -= 11
                self.can_move_up(list_rect)
            if self.COUNT_JUMP > 30 and self.COUNT_JUMP <= 35:
                self.COUNT_JUMP += 1
                self.JUMP = False 
                self.NAME_IMAGE = "game2/images/player/8.png"
                self.direction()
        if self.MASK_ON and not self.INJURED and not self.EXTING_ON:
            event = pygame.key.get_pressed()
            #
            if event[pygame.K_UP] and self.KEY_PRESSED == False:
                self.KEY_PRESSED = True

            if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
                if self.COUNT_JUMP <= 25:
                    self.NAME_IMAGE = "game2/images/player_mask/6.png"
                else: 
                    self.NAME_IMAGE = "game2/images/player_mask/8.png"
                self.direction()
                self.JUMP = True
                self.COUNT_JUMP += 1
                self.Y -= 11
                self.can_move_up(list_rect)
            if self.COUNT_JUMP > 30 and self.COUNT_JUMP <= 35:
                self.COUNT_JUMP += 1
                self.JUMP = False 
                self.NAME_IMAGE = "game2/images/player_mask/8.png"
                self.direction()

        if self.INJURED and not self.EXTING_ON:
            event = pygame.key.get_pressed()
            #
            if event[pygame.K_UP] and self.KEY_PRESSED == False:
                self.KEY_PRESSED = True

            if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
                if self.COUNT_JUMP <= 25:
                    self.NAME_IMAGE = "game2/images/player_with_injured/6.png"
                else: 
                    self.NAME_IMAGE = "game2/images/player_with_injured/8.png"
                self.direction()
                self.JUMP = True
                self.COUNT_JUMP += 1
                self.Y -= 11
                self.can_move_up(list_rect)
            if self.COUNT_JUMP > 30 and self.COUNT_JUMP <= 35:
                self.COUNT_JUMP += 1
                self.JUMP = False 
                self.NAME_IMAGE = "game2/images/player_with_injured/8.png"
                self.direction()
        if self.EXTING_ON:
            event = pygame.key.get_pressed()
            #
            if event[pygame.K_UP] and self.KEY_PRESSED == False:
                self.KEY_PRESSED = True

            if self.KEY_PRESSED and self.COUNT_JUMP <= 30:
                if self.COUNT_JUMP <= 25:
                    self.NAME_IMAGE = "game2/images/player_with_exting/6.png"
                else: 
                    self.NAME_IMAGE = "game2/images/player_with_exting/8.png"
                self.direction()
                self.JUMP = True
                self.COUNT_JUMP += 1
                self.Y -= 11
                self.can_move_up(list_rect)
            if self.COUNT_JUMP > 30 and self.COUNT_JUMP <= 35:
                self.COUNT_JUMP += 1
                self.JUMP = False 
                self.NAME_IMAGE = "game2/images/player_with_exting/8.png"
                self.direction()
    def medic_move(self):
        if self.MEDIC_MOVE_LEFT == True:
                self.DIRECTION = 'L'
                self.X -= 2
                self.DIRECTION = 'R'
                self.animation(folder= "medic",count_while=5,last_img= 5, first_img=1) 
        if self.MEDIC_MOVE_RIGHT == True:
                self.DIRECTION = 'R'
                self.X += 2
                self.DIRECTION = 'L'
                self.animation(folder= "medic",count_while=5,last_img= 5, first_img=1) 
        if self.X + self.WIDTH < 0:
            self.MEDIC_MOVE_LEFT = False
        if self.X > 800:
            self.MEDIC_MOVE_RIGHT = False
    def medic_move_screen(self):
        if self.X < 0:
            self.X += 5
            self.DIRECTION = 'L'
        if self.X > 800:
            self.MEDIC_MOVE_LEFT = True
            self.DIRECTION = 'R'
            
        

    def gravity(self, list_rect, sprite = None):
        if not self.MASK_ON and not self.INJURED and not self.EXTING_ON:

            self.can_move_down(list_rect, sprite)
            if self.ACTIVE_GRAVITY:
                self.Y += self.GRAVITY
                if sprite != None and self.JUMP == False and (self.COUNT_JUMP > 35 or self.COUNT_JUMP == 0):

                    self.NAME_IMAGE = "game2/images/player/6.png"
                    self.direction()
        if self.MASK_ON and not self.INJURED and not self.EXTING_ON:

            self.can_move_down(list_rect, sprite)
            if self.ACTIVE_GRAVITY:
                self.Y += self.GRAVITY
                if sprite != None and self.JUMP == False and (self.COUNT_JUMP > 35 or self.COUNT_JUMP == 0):

                    self.NAME_IMAGE = "game2/images/player_mask/6.png"
                    self.direction()
        if self.INJURED and not self.EXTING_ON:

            self.can_move_down(list_rect, sprite)
            if self.ACTIVE_GRAVITY:
                self.Y += self.GRAVITY
                if sprite != None and self.JUMP == False and (self.COUNT_JUMP > 35 or self.COUNT_JUMP == 0):

                    self.NAME_IMAGE = "game2/images/player_with_injured/6.png"
                    self.direction()
        if self.EXTING_ON:

            self.can_move_down(list_rect, sprite)
            if self.ACTIVE_GRAVITY:
                self.Y += self.GRAVITY
                if sprite != None and self.JUMP == False and (self.COUNT_JUMP > 35 or self.COUNT_JUMP == 0):

                    self.NAME_IMAGE = "game2/images/player_with_exting/6.png"
                    self.direction()
        
    def can_move_right(self, list_rect):
        for block in list_rect:
            if self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                if self.X + self.WIDTH <= block.X + self.STEP and self.X + self.WIDTH >= block.X:
                    self.CAN_MOVE_RIGHT = False
                    self.X -= self.STEP
                    break         
                else:
                    self.CAN_MOVE_RIGHT = True
            else:
                    self.CAN_MOVE_RIGHT = True
    def can_move_left(self, list_rect):
        for block in list_rect:
            if  self.Y + 10 <= block.Y + block.HEIGHT and self.Y + self.HEIGHT - 10 >= block.Y:
                if self.X >= block.X - self.STEP and self.X <= block.X + block.WIDTH:
                        self.CAN_MOVE_LEFT = False
                        self.X += self.STEP
                        break
                else:
                    self.CAN_MOVE_LEFT = True
            else:
                self.CAN_MOVE_LEFT = True
    def can_move_down(self, list_rect, sprite = None):
        
        for block in list_rect:
            if self.X <= block.X + block.WIDTH and self.X + self.WIDTH >= block.X:
                if self.Y + self.HEIGHT >= block.Y and self.Y + self.HEIGHT <= block.Y + self.GRAVITY:
                    self.ACTIVE_GRAVITY = False
                    self.COUNT_JUMP = 0
                    self.KEY_PRESSED = False
                    self.JUMP = False
                    self.Y = block.Y - self.HEIGHT
                      
                    break
                else:
                    self.ACTIVE_GRAVITY = True
            else:
                    self.ACTIVE_GRAVITY = True
                

    def can_move_up(self, list_rect):
        for block in list_rect:
            if self.Y <= block.Y + block.HEIGHT and self.Y + self.HEIGHT >= block.Y + block.HEIGHT:
                if self.X + 50>= block.X and self.X + self.WIDTH - 50 <= block.X + block.WIDTH:
                    self.COUNT_JUMP = 41
                    self.ACTIVE_GRAVITY = True
                    self.JUMP = False
    def draw_text(self, win, key):
        font = pygame.font.SysFont("kokila", 25)
        follow = font.render(f"Натисніть {key} щоб взаємодіяти з предметами!", 1, (255,255,255))
        win.blit(follow, (100, 200))

    def lever_collide(self, win):
        event = pygame.key.get_pressed()
        if (self.X + self.WIDTH <= settings.lever.X + self.STEP + 60 and self.X + self.WIDTH >= settings.lever.X - 60) or (self.X >= settings.lever.X - self.STEP - 60 and self.X <= settings.lever.X + settings.lever.WIDTH + 60):
            if (self.Y + 10 <= settings.lever.Y + settings.lever.HEIGHT and self.Y + self.HEIGHT - 10 >= settings.lever.Y) or (self.Y + 10 <= settings.lever.Y + settings.lever.HEIGHT and self.Y + self.HEIGHT - 10 >= settings.lever.Y):
               self.draw_text(win, "E")
               if event[pygame.K_e]:
                  self.OPEN_DOOR = True

    def mask_collide(self, win):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= mask.X + mask.WIDTH + 20 and self.X + 20 >= mask.X:
            if self.Y + 21 >= mask.Y and self.Y + self.HEIGHT <= mask.Y + mask.HEIGHT + 20:
                self.draw_text(win, "R")
                if event[pygame.K_r]:
                    self.MASK_ON = True
                    self.NAME_IMAGE = "game2/images/player_mask/1.png"
                    mask.NAME_IMAGE = None
                    mask.IMAGE = None
                    self.load_image()

    def injured_collide(self):
        event = pygame.key.get_pressed()
        if self.X + self.WIDTH <= settings.injured.X + settings.injured.WIDTH + 20 and self.X + 20 >= settings.injured.X:
            if self.Y + 21 >= settings.injured.Y and self.Y + self.HEIGHT <= settings.injured.Y + settings.injured.HEIGHT + 20:
                self.draw_text(win, "F")
                if event[pygame.K_f]:
                    self.NAME_IMAGE = "game2/images/player_with_injured/1.png"
                    self.load_image()
                    settings.injured.IMAGE = None
                    settings.injured.NAME_IMAGE = None
                    self.INJURED = TrueW
    def door_collide(self, door):
        event = pygame.key.get_pressed()
        if not self.OPEN_DOOR:
            if self.Y >= door.Y and self.Y + self.HEIGHT - 10 <= door.Y + door.HEIGHT:
                if self.X + self.WIDTH >= door.X:
                    if self.ENTER_DOOR:
                        self.draw_text(win, "F")
                        if event[pygame.K_f]:
                           self.SCENE5 = True 
                    else:
                        self.CAN_MOVE_RIGHT = False
                        self.X -= 3
                        self.X -= 3
        if self.OPEN_DOOR:
            door.NAME_IMAGE = None
            door.IMAGE = None

    def medic_bot_collide(self):
        global flag_level_3
        if self.X <= medic_bot.X + medic_bot.WIDTH and self.X + self.WIDTH >= medic_bot.X:
            if self.Y + 30 >= medic_bot.Y and self.Y + self.HEIGHT <= medic_bot.Y + medic_bot.HEIGHT + 30:
                flag_level_3 = True

    def door_exit_collide(self):
        if self.INJURED:
            if self.Y >= door_exit.Y and self.Y + self.HEIGHT - 10 <= door_exit.Y + door_exit.HEIGHT:
                if self.X + self.WIDTH >= door_exit.X:
                    event = pygame.key.get_pressed()
                    self.draw_text(win, "E")
                    if event[pygame.K_e]:
                        self.EXIT_DOOR = True
    def animation(self,folder= None, count_while= None, last_img= None, first_img= None):
        self.SPEED_ANIMATION += 1
        if self.SPEED_ANIMATION % count_while == 0:
            if self.COUNT_IMG == last_img:
                self.COUNT_IMG = first_img
            self.NAME_IMAGE = f"game2/images/{folder}/{self.COUNT_IMG}.png"
            self.direction() # задаємо напрямок по горизонталі зображення 
            self.COUNT_IMG += 1 # задаємо наступний номер зображення
    def direction(self):
        if self.DIRECTION == 'R':
            self.load_image()
        elif self.DIRECTION == 'L':
            self.load_image(direction=True)
    def fire(self, fire, num_fire):
        global fire1
        global fire2
        global fire3
        global fire4
        global fire5
        global fire6
        global fire7
        global fire8
        global fire9
        global fire10
        global fire11
        global fire12
        global fire13
        if fire.FLAG_DEATH_FIRE:
            self.COUNT_FIRE_POSITION += 1
            if self.X <= fire.X + fire.WIDTH and self.X + self.WIDTH >= fire.X:
                if self.Y + 30 >= fire.Y and self.Y + self.HEIGHT <= fire.Y + fire.HEIGHT + 30:
                    self.DEATH_FIRE = True
            if (self.Y + 10 <= fire.Y + fire.HEIGHT and self.Y + self.HEIGHT - 10 >= fire.Y) or (self.Y + 10 <= fire.Y + fire.HEIGHT and self.Y + self.HEIGHT - 10 >= fire.Y):
                if (self.X + self.WIDTH <= fire.X + self.STEP + 30 and self.X + self.WIDTH >= fire.X - 30) or (self.X >= fire.X - self.STEP - 30 and self.X <= fire.X + fire.WIDTH + 30):
                    if self.EXTING_ON:
                        event = pygame.key.get_pressed()
                        self.draw_text(win, "E")
                        if event[pygame.K_e]:
                            if num_fire == 1:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_1 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 2:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_2 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 3:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_3 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 4:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_4 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 5:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_5 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 6:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_6 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 7:
                                fire.NO_FIRE = True
                            
                                self.BLIT_FIRE_7 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 8:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_8 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 9:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_9 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 10:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_10 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 11:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_11 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 12:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_12 = False
                                fire.FLAG_DEATH_FIRE = False
                            if num_fire == 13:
                                fire.NO_FIRE = True
                                self.BLIT_FIRE_13 = False  
                                fire.FLAG_DEATH_FIRE = False 
            if self.COUNT_FIRE_POSITION == 350:
                fire1 = Sprite(x = 400, y = 70, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 700:
                fire2 = Sprite(x = 720, y = 670, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 1050:
                fire3 = Sprite(x = 0, y = 670, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 1400:
                fire4 = Sprite(x = 100, y = 490, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 1750:
                fire5 = Sprite(x = 100, y = 250, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 2100:
                fire6 = Sprite(x = 0, y = 0, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 2450:
                fire7 = Sprite(x = 400, y = 670, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 2800:
                fire8 = Sprite(x = 200, y = 670, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 3150:
                fire9 = Sprite(x = 0, y = 0, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 3500:
                fire10 = Sprite(x = 300, y = 370, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 3850:
                fire11 = Sprite(x = 270, y = 670, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 4200:
                fire12 = Sprite(x = 320, y = 190, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
            if self.COUNT_FIRE_POSITION == 4550:
                fire13 = Sprite(x = 550, y = 490, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
    def panel_collide(self):
        event = pygame.key.get_pressed()
        if (self.X + self.WIDTH <= panel.X + self.STEP + 60 and self.X + self.WIDTH >= panel.X - 60) or (self.X >= panel.X - self.STEP - 60 and self.X <= panel.X + panel.WIDTH + 60):
            if (self.Y + 10 <= panel.Y + panel.HEIGHT and self.Y + self.HEIGHT - 10 >= panel.Y) or (self.Y + 10 <= panel.Y + panel.HEIGHT and self.Y + self.HEIGHT - 10 >= panel.Y):
                self.draw_text(win, "E")
                if event[pygame.K_e]:
                   self.SCENE4 = True
    def extinguisher_collide(self):
        event = pygame.key.get_pressed()
        if not self.EXTING_ON:
            if self.X + self.WIDTH <= extinguisher.X + extinguisher.WIDTH + 20 and self.X + 20 >= extinguisher.X:
                if self.Y + 21 >= extinguisher.Y and self.Y + self.HEIGHT <= extinguisher.Y + extinguisher.HEIGHT + 20:
                    self.draw_text(win, "E")
                    if event[pygame.K_e]:
                      self.NAME_IMAGE = "game2/images/player_with_exting/1.png"
                      self.EXTING_ON = True
                      self.load_image()
    def shoot(self, win, count_while, sprite, list_rect):
            global bullet1
            self.COUNT_BULLET += 1
            if self.COUNT_BULLET % count_while == 2 and len(self.LIST_BULLET) < 1:
                if medic_bot.X < -2:
                    bullet1 = bullet.Bullet(
                        x = self.X - 20,
                        y = self.Y + 10,
                        width= 20,
                        height= 20,
                        name_image= "game2/images/bullet.png"
                    )
                
                    
                else:
                    if medic_bot.X > 400:          
                        bullet1 = bullet.Bullet(
                            x = self.X + 20,
                            y = self.Y + 10,
                            width= 20,
                            height= 20,
                            name_image= "game2/images/bullet_2.png"
                        )
                    else:
                        bullet1 = bullet.Bullet(
                            x = self.X + 20,
                            y = self.Y + 10,
                            width= 20,
                            height= 20,
                            name_image= "game2/images/bullet.png"
                        )

                bullet1.load_image()
                
                self.LIST_BULLET.append(bullet1)
            if self.LIST_BULLET:
                for bullet1 in self.LIST_BULLET:
                    bullet1.blit_sprite(win)
                    bullet1.bullet(sprite,list_rect = list_rect, medic = medic_bot)
                    if bullet1.MOVE_BULLET == False:
                        self.LIST_BULLET.remove(bullet1)   
    def hole(self):
        global letter
        if self.HOLE_COUNT:
            self.TIME_HOLE_BLIT += 1
            if self.TIME_HOLE_BLIT == 50:
                self.X = random.choice(list_cor_x) 
                self.Y = random.choice(list_cor_y)  
                letter = random.choice(list_letters)
                self.TIME_HOLE_BLIT = 0
                self.HOLE_COUNT = False
        event = pygame.key.get_pressed()
        font = pygame.font.SysFont("kokila", 23)
        follow = font.render(f"{letter}", 1, (0,0,0))
        if letter == "q":
            if event[pygame.K_q]:
                self.HOLE_COUNT = True
        if letter == "w":
            if event[pygame.K_w]:
                self.HOLE_COUNT = True
        if letter == "e":
            if event[pygame.K_e]:
                self.HOLE_COUNT = True
        if letter == "r":
            if event[pygame.K_r]:
                self.HOLE_COUNT = True
        if letter == "t":
            if event[pygame.K_t]:
                self.HOLE_COUNT = True
        if letter == "y":
            if event[pygame.K_y]:
                self.HOLE_COUNT = True
        if letter == "u":
            if event[pygame.K_u]:
                self.HOLE_COUNT = True
        if letter == "x":
            if event[pygame.K_x]:
                self.HOLE_COUNT = True
        if letter == "c":
            if event[pygame.K_c]:
                self.HOLE_COUNT = True
        if letter == "f":
            if event[pygame.K_f]:
                self.HOLE_COUNT = True
        if not self.HOLE_COUNT:
            win.blit(follow, (self.X, self.Y))
    def blit_blue(self):
        try:
            if self.BLUE and self.FLAG_BLUE:
                self.HEIGHT += 10
            if self.HEIGHT > 800:
                self.FLAG_BLUE = False   
            if self.BLUE and not self.FLAG_BLUE:
                self.HEIGHT -= 10
                
        except:
            self.BLUE = False
                


sprite = Sprite(color = (0,0,0), x = 330, y = 600, width = 50, height = 60, name_image = "game2/images/player/1.png")
smoke = Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
mask = Sprite(x = 5, y = 5, width = 30, height = 40, name_image = "game2/images/mask.png")
door = Sprite(x = 500, y = 600, width = 120, height = 120, name_image = "game2/images/door.png")
door_exit = Sprite(x = 700, y = 0, width = 120, height = 120, name_image = "game2/images/door.png")



medic_bot = Sprite(x = 20, y = 660, width = 50, height = 50, name_image = "game2/images/medic/1.png")


sprite_2 = Sprite(color = (0,0,0), x = 400, y = 500, width = 50, height = 60, name_image = "game2/images/sprite.png")
sprite_3 = Sprite(color = (0,0,0), x = 300, y = 660, width = 50, height = 60, name_image = "game2/images/sprite.png")



medic_escape = Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/medic_escape.png")



arrow1 = Sprite(x = 700, y = 650, width = 100, height = 150, name_image = "game2/images/comix/arrow_1.png")
arrow2 = Sprite(x = 0, y = 650, width = 100, height = 150, name_image = "game2/images/comix/arrow_2.png")
page = Sprite(x = 0, y = 0, width = 800, height = 750, name_image = "game2/images/comix/page_1.png")
page_level_2 = Sprite(x = 0, y = 0, width = 800, height = 750, name_image = "game2/images/comix/page_13.png")
page_level_3 = Sprite(x = 0, y = 0, width = 800, height = 750, name_image = "game2/images/comix/page_14.png")
page_level_4 = Sprite(x = 0, y = 0, width = 800, height = 750, name_image = "game2/images/comix/page_15.png")
black = Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/comix/black.png")
button_skip = Sprite(x = 300, y = 710, width = 220, height = 80, name_image = "game2/images/skip.png")
button_start = Sprite(x = 300, y = 710, width = 220, height = 80, name_image = "game2/images/start.png")
win_1 =  Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/win.png")

#3 лвл. Вогонь
fire1 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire2 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire3 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire4 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire5 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire6 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire7 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire8 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire9 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire10 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire11 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire12 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
fire13 = Sprite(x = 0, y = 0, width = 0, height = 0, name_image = "game2/images/fire/fire1.png")
blue = Sprite(x = 0, y = 0, width = 800, height = 0, name_image = "game2/images/blue.png")

door_3 = Sprite(x = 520, y = 600, width = 120, height = 120, name_image = "game2/images/door.png")
extinguisher = Sprite(x = 730, y = 490, width = 50, height = 50, name_image = "game2/images/extinguisher.png")
panel = Sprite(x = 525, y = 66, width = 50, height = 50, name_image = "game2/images/panel.png")
pump = Sprite(x = 550, y = 550, width = 200, height = 200, name_image = "game2/images/pump.png")
pump_scale = Sprite(x = 580, y = 250, width = 60, height = 100, name_image = "game2/images/scale.png")
boat = Sprite(x = 100, y = 250, width = 300, height = 500, name_image = "game2/images/boat.png")

hole1 = Sprite(x = 0, y = 0, width = 50, height = 50, name_image = "game2/images/hole1.png")


death = Sprite(x = 0, y = 0, width = 800, height = 800, name_image = "game2/images/death.png")
button_menu = Sprite(x = 130, y = 675, width = 250, height = 100, name_image = "game2/images/menu.png")
button_one_more = Sprite(x = 420, y = 675, width = 250, height = 100, name_image = "game2/images/one_more.png")