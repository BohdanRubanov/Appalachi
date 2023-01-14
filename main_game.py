# from profilehooks import profile
import pygame 
import os
import dicts 
import settings
import area
import sprite
import music
import bullet

pygame.init()

#Списики з шляхами до об'єктів меню
images_list1 = []
images_list = ["game2/images/play_1.png", "game2/images/play_light.png",
                    "game2/images/developer_light.png",
                    "game2/images/exit_1.png", "game2/images/exit_light.png",
                    "game2/images/play.png", "game2/images/developers_1.png", "game2/images/developers.png",
                    "game2/images/exit.png"]
#Функція яка загружає картинки до об'єктів меню
def load_name_image(name):
    for image in images_list:
        if image == f"game2/images/{name}.png":
            path_image = settings.create_path()
            path_image = os.path.join(path_image, image)
            image = pygame.image.load(path_image)
            image = pygame.transform.scale(image, (800,800))
            return image
#Картинки кнопки play (грати) у меню
image_play = load_name_image("play")
image_play_1 = load_name_image("play_1")
image_play_light = load_name_image("play_light")
#Картинки кнопки developers (розробники) у меню
image_developers = load_name_image("developers")
image_developers_1 = load_name_image("developers_1")
image_developers_light = load_name_image("developer_light")
#Картинки кнопки exit (вийти) у меню
image_exit = load_name_image("exit")
image_exit_1 = load_name_image("exit_1")
image_exit_light = load_name_image("exit_light")
#Змінні щ параметрами  об'єкту диму
smoke_width = 50
smoke_height = 50
smoke_x = 0
smoke_y = 750
#Создання об'єкт диму
smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
#Змінні які відповідають за те, яка сцена або рівень на екрані
scene1 = False #Меню
backstory = False #Початкова предисторія
level1 = False #1 рівень
level2 = False #2 рівень
level3 = True #3 рівень
scene3 = False #Розробники
#Лічильник диму за допомогою якого змінюються розміри диму
smoke_count = 0 
#Заданий ФПС гри
fps = 60
#тимчасова музика для 3 рівня
# music.menu_background_sound.load()
# music.menu_background_sound.play(repeat=-1)
#Создавання об'єкту вікна гри
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
#Задання назви вікну гри
pygame.display.set_caption("game")
#Все те що відноситься до матриці
list_create_world = []
list_rect = []
list_create_world, list_rect = area.create_world(area.list_world_3)
# area.create_world(area.list_world_2)
# @profile
#Головна функція гри у якій міститься майже все
def run_game():
    #Робимо потрібні функції локальні змінні глобальними
    global list_create_world
    global list_rect
    global smoke
    global scene1
    global level1
    global scene3
    
    #Лічильники
    menu_count = 0#Лічильник для анімацій у меню
    move_medic_count = 0
    medic_left_count_1 = 0
    medic_right_count_1 = 0
    medic_right_count_2 = 0
    medic_right_count_3 = 0
    # name_image_count = 0
    last_medic_time_move_count = 0
    #Флаги
    flag_menu_light = True
    flag_black_pages = False
    #Змінна відповідальна за ФПС у грі
    clock = pygame.time.Clock()
    #Головна змінна гри
    game = True
    #Змінні які відповідальні за переміщення медика по мапі 2 рівня
    medic_left = 0
    medic_right = 0
    move_medic_right = False
    move_medic_left = True
    last_medic_time_move = 0
    #Змінна відповідальна за переход зі сторінки на сторінку у предисторії
    pages_time_black_time = 0
    #Змінна яка говорить про те яка зараз відкрита сторінка
    page_num = 1

    #Головний цикл гри у якому міститься майже все
    while game:
        #Медик починає рух
        last_medic_time_move += 1
        #Лічильнік починає лічити до того значення на якому медик зупиниться
        move_medic_count += 1
        #Робимо потрібні циклу локальні змінні глобальними
        global smoke_x
        global smoke_y
        global smoke_height
        global smoke_width
        global smoke_count
        global level2
        global level3

        #Умова за якою відкривається меню гри
        if scene1:
            #Лічильник меню починає лічити за для того щоб почала роботу анімація
            menu_count += 1
            #Перша картинка в анімації фону меню
            if menu_count == 5:
                settings.bg_menu.NAME_IMAGE = "game2/images/bg_menu_1.png" #Зміна картинки нової свойства
                settings.bg_menu.load_image() #Завантаження картинки нової свойства
                flag_menu_light = True
            #Друга картинка в анімації фону меню
            if menu_count == 10:
                settings.bg_menu.NAME_IMAGE = "game2/images/bg_menu_2.png"
                settings.bg_menu.load_image() 
                flag_menu_light = True
            #Третя картинка в анімації фону меню
            if menu_count == 15:
                settings.bg_menu.NAME_IMAGE = "game2/images/bg_menu_3.png"
                settings.bg_menu.load_image() 
                flag_menu_light = True
            #Четверта картинка в анімації фону меню
            if menu_count == 20:
                settings.bg_menu.NAME_IMAGE = "game2/images/bg_menu_4.png"
                settings.bg_menu.load_image() 
                flag_menu_light = False
            #П'ята картинка в анімації фону меню
            if menu_count == 25:
                settings.bg_menu.NAME_IMAGE = "game2/images/bg_menu_5.png"
                settings.bg_menu.load_image()
                flag_menu_light = False
                menu_count = 0 #Змінення значення лічильника меню на 0, із-за чого анімація починається знову
                
            mouse_pos = pygame.mouse.get_pos() #Змінна яка записує у себе координати кліку ігрока
            #Цикл всіх івентів у меню
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
                #Умова дій при натисненні на якусь частину екрану меню
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    print(click) #Виведення координат натиснення ігрока
                    #Умова відкриття 1 рівня при натисненні на кнопку play 
                    if settings.play.RECT.collidepoint(click):
                        level1 = True #Змінна яка робить level1 дійсним за допомогою чого запускається 1 рівень
                        music.menu_background_sound.stop() #Зупинення музику у меню
                        music.menu_background_sound.unload() #Видалення музику у меню з гри на тей час поки в неї нема потреби
                        music.level1_background_sound.load() #Загрузка музики 1 рівня
                        music.level1_background_sound.play(repeat=-1) #Початок гри музики 1 рівня
                        list_create_world, list_rect = area.create_world(area.list_world_1) #Создавання матриці 1 рівня
                        
                        scene1 = False
                    if settings.exit.RECT.collidepoint(click):
                        # print(2)
                        game = False 
                    if settings.developers.RECT.collidepoint(click):
                        # print(3)
                        scene3 = True
                        scene1 = False
                
            if flag_menu_light:
                if settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play_1
                if not settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play_light
                    
                if settings.developers.RECT.collidepoint(mouse_pos):
                
                    settings.developers.IMAGE =  image_developers_1
                    
                if not settings.developers.RECT.collidepoint(mouse_pos):
                    settings.developers.IMAGE =  image_developers_light
                    
                if settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit_1
                    
                if not settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit_light
                    
            else:
                if settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play_1
                    
                if not settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play
                    
                if settings.developers.RECT.collidepoint(mouse_pos):
                
                    settings.developers.IMAGE =  image_developers_1
                    
                if not settings.developers.RECT.collidepoint(mouse_pos):
                    settings.developers.IMAGE =  image_developers
                    
                if settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit_1
                    
                if not settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit
            settings.bg_menu.blit_sprite(win)
            settings.play.blit_sprite(win)
            # settings.play.draw_rect(win)
            settings.developers.blit_sprite(win)
            # settings.developers.draw_rect(win)
            settings.exit.blit_sprite(win)                
            # print(list_create_world)   
            # print(settings.play.IMAGE)
        
        
        
        
        if backstory:
            # print(flag_black_pages)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False 
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = event.pos 
                    # print(click)
                    if sprite.arrow1.RECT.collidepoint(click):
                        pages_time_black_time = 0
                        if page_num <= 2:
                            page_num += 1
                            flag_black_pages = True
                    if sprite.arrow2.RECT.collidepoint(click):
                        pages_time_black_time = 0
                        if page_num >= 2:
                            page_num -= 1
                            flag_black_pages = True
            sprite.page.blit_sprite(win) 
            sprite.arrow1.blit_sprite(win) 
            sprite.arrow2.blit_sprite(win)  
            if flag_black_pages:
                # print(111111111)
                pages_time_black_time += 1
                # sprite.black.blit_sprite(win)if sprite.arrow1.RECT.collidepoint(click):
                if pages_time_black_time < 50:       
                    sprite.page.NAME_IMAGE = "game2/images/comix/black.png"  
                    sprite.page.load_image() 
                if pages_time_black_time >= 50:       
                    sprite.page.NAME_IMAGE = f"game2/images/comix/page_{page_num}.png"  
                    sprite.page.load_image()
                # sprite.page.blit_sprite(win)  
         
            
            
            
            
        if level1:
            # music.level1_background_sound.load()
            # music.level1_background_sound.play(repeat = -1) 
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    print(click)
                if event.type == pygame.QUIT:
                    game = False  
            # print(clock.get_fps())
            smoke_count += 1
            settings.bg.blit_sprite(win)
            sprite.sprite.can_move_right(list_rect)
            sprite.sprite.can_move_left(list_rect)
            # sprite.sprite.can_move_down(area.list_rect)
            sprite.sprite.move_sprite()
            sprite.sprite.jump(list_rect)
            sprite.sprite.blit_sprite(win)
            sprite.sprite.gravity(list_rect= list_rect, sprite=1)
            sprite.smoke.blit_sprite(win)
            if sprite.mask.IMAGE != None:
                sprite.mask.blit_sprite(win)
            sprite.mask.gravity(list_rect= list_rect)
            settings.lever.blit_sprite(win)
            settings.injured.blit_sprite(win)
                # settings.mask.NAME_IMAGE = None
            sprite.sprite.lever_collide(win)
            sprite.sprite.mask_collide(win)
            sprite.sprite.injured_collide()
            # sprite.sprite.draw_rect(win)
            if sprite.door.IMAGE != None:
                sprite.door.blit_sprite(win)
            sprite.sprite.door_collide(sprite.door)
            sprite.door_exit.blit_sprite(win)
            sprite.sprite.door_exit_collide()
            # sprite.door.open_door()
            # sprite.sprite.draw_text(win, )
            for el in list_create_world:
                # print(el)
                el.blit_sprite(win)

            if smoke_count == 50:
                # sprite.smoke.WIDTH += 50
                # sprite.smoke.HEIGHT += 50
                # print(1)
                smoke_width += 50
                smoke_height += 50
                # smoke_x += 20
                smoke_y -= 20
                smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
                # smoke.blit_sprite(win)
                smoke_count = 0

            smoke.blit_sprite(win)
            #условие смерти от дыма
            sprite.sprite.position()
            x = sprite.sprite.X
            y = sprite.sprite.Y
            sprite_cor = x,y
            if sprite.sprite.X + sprite.sprite.WIDTH <= smoke.X + smoke.WIDTH + 20 and sprite.sprite.X + 20 >= smoke.X:
                if sprite.sprite.Y + 21 >= smoke.Y and sprite.sprite.Y + sprite.sprite.HEIGHT <= smoke.Y + smoke.HEIGHT + 20:
                    if sprite.sprite.MASK_ON == True:
                        pass
                    else:
                        smoke = sprite.Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
                        smoke_width = 50
                        smoke_height = 50
                        smoke_x = 0
                        smoke_y = 750

                        # music.die_smoke_version.play()
                        level1 = False
                        scene1 = True
                        music.level1_background_sound.stop()
                        music.level1_background_sound.unload()
                        music.die_smoke_version.play()
                        music.menu_background_sound.load()
                        music.menu_background_sound.play(repeat=-1)
                        smoke_count = 0
                        print("touch")
            event = pygame.key.get_pressed()
            if sprite.sprite.EXIT_DOOR:
                level2 = True
                list_create_world, list_rect = area.create_world(area.list_world_2)
                music.level1_background_sound.stop()
                music.level1_background_sound.unload()
                # print(pygame.mixer.music.get_busy())
                # music.level2_background_sound.load()
                # music.level2_background_sound.play(repeat=-1)
                # print("edrdees")
                level1 = False
        if level2: 
            if not pygame.mixer.music.get_busy():
                music.level2_background_sound.load()
                music.level2_background_sound.play(repeat=-1)
            # music.level2_background_sound.play()
            # print(sprite.sprite_2.X)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False  
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos 
                    print(click)
            settings.bg.blit_sprite(win)
            # area.create_world(area.list_world_2)
            for el in list_create_world:
                el.blit_sprite(win)
            
            
            # sprite.sprite.can_move_down(area.list_rect)
            sprite.sprite_2.move_sprite()
            sprite.sprite_2.can_move_right(list_rect)
            sprite.sprite_2.can_move_left(list_rect)
            sprite.medic_bot.can_move_right(list_rect)
            sprite.medic_bot.can_move_left(list_rect)
            sprite.sprite_2.jump(list_rect)
            sprite.sprite_2.blit_sprite(win)
            sprite.sprite_2.gravity(list_rect= list_rect, sprite=1) 
            sprite.medic_bot.blit_sprite(win)
            sprite.medic_bot.medic_move()
            sprite.sprite_2.medic_bot_collide()
            sprite.medic_bot.shoot(win,50, sprite.sprite_2, list_rect = list_rect)
            
            # sprite.medic_bot.medic_move_screen()
            # sprite.medic_bot.can_move_left(list_rect= area.list_rect)
            # sprite.medic_bot.can_move_right(list_rect= area.list_rect)
            # print(sprite.medic_bot.X)
            sprite.medic_bot.gravity(list_rect= list_rect)
            # sprite.bullet.blit_sprite(win)
            # for i in range(1):
            #     sprite.pistol_shoot.PISTOL_SHOOT.play()
            # sprite.sprite_2.bullet()
            # if bullet.flag_bullet_shoot == True:
            #     music.pistol_shoot.PISTOL_SHOOT.play()
            if bullet.flag_bullet_die == True:
                level2 = False
                scene1 = True
                
                music.level2_background_sound.stop()
                music.level2_background_sound.unload()
                music.menu_background_sound.load()
                music.menu_background_sound.play(repeat=-1)
            # print(move_medic_count)
            if move_medic_count == 150 and medic_left != 5 and move_medic_left == True:
                # print(11111)
                sprite.medic_bot.MEDIC_MOVE_LEFT = True
                move_medic_count = -100
                medic_left += 1
            # else:
            #     sprite.medic_bot.MEDIC_MOVE_LEFT = False
            if medic_left == 2:
                    sprite.medic_bot.MEDIC_MOVE_LEFT = False
                    sprite.medic_bot.X = 0
                    sprite.medic_bot.Y = 190
                # print(sprite.medic_bot.X)
                # print(1)
            if medic_left == 4:
                if medic_left_count_1 != 1:
                    sprite.medic_bot.MEDIC_MOVE_LEFT = False
                    sprite.medic_bot.X = 0
                    sprite.medic_bot.Y = 0
                    medic_left_count_1 += 1
                    move_medic_right = True
                    medic_left = 0
                    move_medic_left = False
            if move_medic_count == 150 and medic_right != 6 and move_medic_right == True:
                medic_left_count_1 = 0
                sprite.medic_bot.MEDIC_MOVE_LEFT = False
                # print(11111)
                sprite.medic_bot.MEDIC_MOVE_RIGHT = True
                move_medic_count = -100
                medic_right += 1
            if medic_right == 1:
                if medic_right_count_1 != 1:
                    # print(22222)
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 70
                    # sprite.medic_bot.gravity(list_rect= area.list_rect)
                    # medic_right_count_1 += 1
                # print(sprite.medic_bot.X)
                # print(1)
            if medic_right == 3:
                if medic_right_count_2 != 1:
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 630
                    medic_right_count_2 += 1
            if medic_right == 5:
                if medic_right_count_3 != 1:
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 190
                    move_medic_left = True
                    move_medic_count = 0
                    medic_right = 0
                    move_medic_right = False
                    medic_right_count_3 += 1
            if last_medic_time_move > 2250 and last_medic_time_move_count < 3:
                sprite.medic_bot.X = 0
                sprite.medic_bot.Y = 660
                last_medic_time_move = 0
                last_medic_time_move_count += 1
                if last_medic_time_move_count == 2:
                    last_medic_time_move += 1800
            if last_medic_time_move_count >= 3:
                sprite.medic_escape.blit_sprite(win)
            if move_medic_count > 151:
                move_medic_count = 0
            if sprite.flag_level_3:
                # print(222222222222222)
                level3 = True
                list_create_world, list_rect = area.create_world(area.list_world_3)
                level2 = False
                music.level2_background_sound.stop()
                music.level2_background_sound.unload()
        
            
        if level3:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   game = False  
               if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                   click = event.pos 
                   print(click)
            # settings.bg.blit_sprite(win)
            # area.create_world(area.list_world_2)
            
            
            # sprite.sprite.can_move_down(area.list_rect)
            settings.bg.blit_sprite(win)
            for el in list_create_world:
                el.blit_sprite(win)
            # print(sprite.fire7.BLIT_FIRE_7)
            if sprite.sprite_3.BLIT_FIRE_1:
                sprite.fire1.blit_sprite(win)
            if sprite.sprite_3.BLIT_FIRE_2:
                sprite.fire2.blit_sprite(win)
            if sprite.sprite_3.BLIT_FIRE_3:
                sprite.fire3.blit_sprite(win)
            if sprite.sprite_3.BLIT_FIRE_4:
                sprite.fire4.blit_sprite(win)
            if sprite.sprite_3.BLIT_FIRE_5:
                sprite.fire5.blit_sprite(win)
            if sprite.sprite_3.BLIT_FIRE_6:
                sprite.fire6.blit_sprite(win)
            if sprite.sprite_3.BLIT_FIRE_7:
                sprite.fire7.blit_sprite(win)
            sprite.sprite_3.fire(sprite.fire1, 1)
            sprite.sprite_3.fire(sprite.fire2, 2)
            sprite.sprite_3.fire(sprite.fire3, 3)
            sprite.sprite_3.fire(sprite.fire4, 4)
            sprite.sprite_3.fire(sprite.fire5, 5)
            sprite.sprite_3.fire(sprite.fire6, 6)
            sprite.sprite_3.fire(sprite.fire7, 7)
            sprite.door_3.blit_sprite(win)
            sprite.extinguisher.blit_sprite(win)
            sprite.panel.blit_sprite(win)
            sprite.sprite_3.move_sprite()
            sprite.sprite_3.can_move_right(list_rect)
            sprite.sprite_3.can_move_left(list_rect)
            sprite.sprite_3.jump(list_rect)
            sprite.sprite_3.blit_sprite(win)
            sprite.sprite_3.gravity(list_rect= list_rect, sprite=1) 
            sprite.sprite_3.panel_collide()
            sprite.sprite_3.extinguisher_collide()
            sprite.sprite_3.door_collide(sprite.door_3)
            
        
            
        
            
        if scene3:
            settings.bg_developers.blit_sprite(win)
            settings.back.blit_sprite(win)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if settings.back.RECT.collidepoint(click):
                        scene1 = True
                        scene3 = False
                if event.type == pygame.MOUSEMOTION:
                    if settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 715,y = 0, width = 75, height = 45,name_image = "game2/images/back.png")
                    if not settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 700,y = 0, width = 100, height = 50,name_image = "game2/images/back.png")
        pygame.display.flip()
        clock.tick(fps)      
run_game() 