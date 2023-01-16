# from profilehooks import profile
import pygame 
import os
import dicts 
import settings
import area
import sprite
import music
import bullet
import tubings
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
level1 = False#1 рівень
level2 = False #2 рівень
level3 = False #3 рівень
scene3 = False #Розробники
scene4 = False#черный экран
level4 = True
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

list_pipes = []
list_rect_pipes = []
#Все те що відноситься до матриці
list_create_world = []
list_rect = []
list_pipes, list_rect_pipes = tubings.create_world(tubings.list_pipe_matrix)
list_create_world, list_rect = area.create_world(area.list_world_1)
# area.create_world(area.list_world_2)
# @profile
#Головна функція гри у якій міститься майже все
smoke_width = 50
smoke_height = 50
smoke_y = 800
smoke_x = 0
smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
print(smoke.X)
smoke.IMAGE = pygame.transform.rotate(smoke.IMAGE, 180)
smoke.load_image()

def run_game():
    global smoke_width, smoke_height, smoke_y, smoke_x, smoke
    #Робимо потрібні функції локальні змінні глобальними
    global list_create_world
    global list_rect
    global smoke
    global scene1
    global level1
    global scene3
    
    #Лічильники
    menu_count = 0 #Лічильник для анімацій у меню
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
    # black = pygame.image.load("images/comix/black.png")
    #Головний цикл гри у якому міститься майже все
    global smoke_count
    global level2
    global level3, level4
    global scene4
    while game:
        #Медик починає рух
        last_medic_time_move += 1
        #Лічильнік починає лічити до того значення на якому медик зупиниться
        move_medic_count += 1
        #Робимо потрібні циклу локальні змінні глобальними
        #global smoke_x
        #global smoke_y
        #global smoke_height
        #global smoke_width
        if sprite.sprite_3.SCENE4:
            scene4 = True
        
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
            #Цикл всіх івентів у меню гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
                #Умова дій при натисненні на якусь частину екрану меню гри
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
                        scene1 = False #Робимо сцену меню не дійсно завдяки чому меню закривається
                    #Умова натиснення на кнопку exit та вихід з гри завдяки робленню змінної game не дійсною
                    if settings.exit.RECT.collidepoint(click):
                        game = False 
                    #Умова натиснення на кнопку developers та вихід з меню гри і перехід до сцени з розробниками
                    if settings.developers.RECT.collidepoint(click):
                        scene3 = True #Робимо сцену розробників дійсною
                        scene1 = False #Робимо сцену меню не дійсною
                
            #Умова зміни картинки кнопки при наведені на неї курсором
            if flag_menu_light:
                #Умова наведення курсором на кнопку play
                if settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play_1 #Зміна картинки кнопки play на ту яка є під час наведення на неї курсору
                if not settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play_light #Зміна другої картинки кнопки play на ту яка є під час НЕ наведення на неї курсору
                
                #Умова наведення курсором на кнопку developers
                if settings.developers.RECT.collidepoint(mouse_pos):   
                    settings.developers.IMAGE =  image_developers_1 #Зміна картинки кнопки developers на ту яка є під час наведення на неї курсору
                if not settings.developers.RECT.collidepoint(mouse_pos):
                    settings.developers.IMAGE =  image_developers_light #Зміна другої картинки кнопки developers на ту яка є під час НЕ наведення на неї курсору
                    
                #Умова наведення курсором на кнопку exit
                if settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit_1 #Зміна картинки кнопки exit на ту яка є під час наведення на неї курсору
                if not settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit_light #Зміна другої картинки кнопки exit на ту яка є під час наведення на неї курсору     
            else:
                #Умова НЕ наведення курсором на кнопку play
                if settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play_1 #Зміна картинки кнопки play на ту яка є під час НЕ наведення на неї курсору
                if not settings.play.RECT.collidepoint(mouse_pos):
                    settings.play.IMAGE = image_play #Зміна другої картинки кнопки play на ту яка є під час НЕ наведення на неї курсору

                #Умова НЕ наведення курсором на кнопку developers
                if settings.developers.RECT.collidepoint(mouse_pos):  
                    settings.developers.IMAGE =  image_developers_1 #Зміна картинки кнопки developers на ту яка є під час НЕ наведення на неї курсору   
                if not settings.developers.RECT.collidepoint(mouse_pos):
                    settings.developers.IMAGE =  image_developers #Зміна другої картинки кнопки developers на ту яка є під час НЕ наведення на неї курсору
                    
                #Умова НЕ наведення курсором на кнопку exit
                if settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit_1 #Зміна картинки кнопки exit на ту яка є під час НЕ наведення на неї курсору
                if not settings.exit.RECT.collidepoint(mouse_pos):
                    settings.exit.IMAGE = image_exit #Зміна другої картинки кнопки exit на ту яка є під час НЕ наведення на неї курсору    
            #Відрисовка об'єктів меню
            settings.bg_menu.blit_sprite(win)
            settings.play.blit_sprite(win)
            settings.developers.blit_sprite(win)
            settings.exit.blit_sprite(win)                
        
        #Умова за якою відкривається предісторія гри
        if backstory:
            # print(flag_black_pages)
            #Цикл всіх івентів у предісторії гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False 
                #Умова дій при натисненні на якусь частину екрану предісторії гри
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    # print(click) #Виведення координат натиснення ігрока
                    #Умова відкриття наступної сторінк  при натисненні на кнопку стрілки вправо
                    if sprite.arrow1.RECT.collidepoint(click):
                        pages_time_black_time = 0
                        #Умова перегортання сторінки на наступну
                        if page_num <= 2:
                            page_num += 1
                            flag_black_pages = True
                    #Умова відкриття наступної сторінк  при натисненні на кнопку стрілки вліво
                    if sprite.arrow2.RECT.collidepoint(click):
                        pages_time_black_time = 0
                        #Умова перегортання сторінки на минулу
                        if page_num >= 2:
                            page_num -= 1
                            flag_black_pages = True
            #Відрисовка об'єктів предісторії
            sprite.page.blit_sprite(win) 
            sprite.arrow1.blit_sprite(win) 
            sprite.arrow2.blit_sprite(win)  
            #Умова переходу з сторінки на сторінку
            if flag_black_pages:
                pages_time_black_time += 1 #Лічильник часу переходу з сторінки на сторінку починає працювати
                # sprite.black.blit_sprite(win)if sprite.arrow1.RECT.collidepoint(click):
                #Умова відрисовки чорної картинки під час переходу коли лічильник pages_time_black_time буде мати значення менше за 50
                if pages_time_black_time < 50:       
                    sprite.page.NAME_IMAGE = "game2/images/comix/black.png"  
                    sprite.page.load_image() 
                #Умова відрисовки сторінки під час переходу коли лічильник pages_time_black_time буде мати значення більше за 50
                if pages_time_black_time >= 50:       
                    sprite.page.NAME_IMAGE = f"game2/images/comix/page_{page_num}.png"  
                    sprite.page.load_image()
                # sprite.page.blit_sprite(win)  
         
        #Умова за якою відкривається 1 рівень гри
        if level1:
            # music.level1_background_sound.load()
            # music.level1_background_sound.play(repeat = -1) 
            #Цикл всіх івентів у 1 рівні гри
            for event in pygame.event.get():
                #Умова дій при натисненні на якусь частину екрану 1 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    print(click) #Виведення координат натиснення ігрока
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
            # print(clock.get_fps())
            smoke_count += 1 #Лічильник диму починає працю
            settings.bg.blit_sprite(win)
            sprite.sprite.can_move_right(list_rect)
            sprite.sprite.can_move_left(list_rect)
            # sprite.sprite.can_move_down(area.list_rect)
            sprite.sprite.move_sprite()
            sprite.sprite.jump(list_rect)
            sprite.sprite.blit_sprite(win)
            sprite.sprite.gravity(list_rect= list_rect, sprite=1)
            # sprite.smoke.blit_sprite(win)
            #Умова відрисовки противогазу
            if sprite.mask.IMAGE != None:
                sprite.mask.blit_sprite(win)
            sprite.mask.gravity(list_rect= list_rect)
            settings.lever.blit_sprite(win)
            settings.injured.blit_sprite(win)
            sprite.sprite.lever_collide(win)
            sprite.sprite.mask_collide(win)
            sprite.sprite.injured_collide()
            #Умова відрисовки одної з дверей
            if sprite.door.IMAGE != None:
                sprite.door.blit_sprite(win)
            sprite.sprite.door_collide(sprite.door)
            sprite.door_exit.blit_sprite(win)
            sprite.sprite.door_exit_collide()
            #Умова відрисовки блоків на мапі першого рівня
            for el in list_create_world:
                el.blit_sprite(win)
            
            #Умова змінення позиції об'єкту диму
            if smoke_count == 50:
                ##Змінення розмірів та позиції об'єкту диму
                smoke_width += 100
                smoke_height += 100
                smoke_y -= 50
                # smoke_x += 5
                print(smoke_width)
                #smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
                #smoke_count = 0
                #smoke_sur = pygame.image.load(smoke.NAME_IMAGE)
                smoke.IMAGE = pygame.transform.scale(smoke.IMAGE, (smoke_width, smoke_height))
                smoke.Y = smoke_y
                # smoke.X = smoke_x
                smoke_count = 0
            smoke.blit_sprite(win)
            #smoke.blit_sprite(win) #Відрисовка диму
            sprite.sprite.position() 
            x = sprite.sprite.X
            y = sprite.sprite.Y
            sprite_cor = x,y
            #Умова програшу від диму
            if sprite.sprite.X + sprite.sprite.WIDTH <= smoke_x + smoke_width + 20 and sprite.sprite.X + 20 >= smoke_x:
                # print(3333333333)
                if sprite.sprite.Y + 21 >= smoke_y and sprite.sprite.Y + sprite.sprite.HEIGHT <= smoke_y + smoke_height + 20:
                    # print(22222222222)
                    if sprite.sprite.MASK_ON == True:
                        # print(22222222222)
                        pass
                    else:
                        # print(111111)
                        #Змінення параметрів диму на стандартні після програшу ігрока
                        smoke = sprite.Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
                        smoke_width = 50
                        smoke_height = 50
                        smoke_x = 0
                        smoke_y = 750
                        #Змінення сцен
                        level1 = False
                        scene1 = True
                        #Змінення музики
                        music.level1_background_sound.stop()
                        music.level1_background_sound.unload()
                        music.die_smoke_version.play()
                        music.menu_background_sound.load()
                        music.menu_background_sound.play(repeat=-1)
                        #Обнуляємо лічильник диму
                        smoke_count = 0
            #Робимо змінну яка у себе записує яка клавіша була натиснена
            event = pygame.key.get_pressed()
            #Умова проходження та закінчення 1 рівня та переходу до 2
            if sprite.sprite.EXIT_DOOR:
                level2 = True #Робимо level2 дійсним тим самим починаємо 2 рівень
                list_create_world, list_rect = area.create_world(area.list_world_2)
                #Змінення музики
                music.level1_background_sound.stop()
                music.level1_background_sound.unload()
                # print(pygame.mixer.music.get_busy())
                # music.level2_background_sound.load()
                # music.level2_background_sound.play(repeat=-1)
                level1 = False #Робимо level1 не дійсним тим самим закінчуємо 1 рівень

        #Умова за якою відкривається 2 рівень гри
        if level2: 
            #Умова початку відигрування музики 2 рівня
            if not pygame.mixer.music.get_busy():
                music.level2_background_sound.load()
                music.level2_background_sound.play(repeat=-1)
            # music.level2_background_sound.play()
            # print(sprite.sprite_2.X)
            #Цикл всіх івентів у 2 рівні гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
                #Умова дій при натисненні на якусь частину екрану 2 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    print(click) #Виведення координат натиснення ігрока
            #Відрисовка фону 2 рівня
            settings.bg.blit_sprite(win)
            #Створення блоків на мапі 2 рівня
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
            #Здійснення гравітації медику
            sprite.medic_bot.gravity(list_rect= list_rect)
            #Умова програгу від пулі
            if bullet.flag_bullet_die == True:
                level2 = False #Роблення сцени другого рівня не дійсною тим самим відбувається закінчення 2 рівня
                scene1 = True #Роблення сцени меню гри дійсною тим самим відкривається меню
                #Змінення музики
                music.level2_background_sound.stop()
                music.level2_background_sound.unload()
                music.menu_background_sound.load()
                music.menu_background_sound.play(repeat=-1)
            #Умова переміщення медику вліво
            if move_medic_count == 150 and medic_left != 5 and move_medic_left == True:
                sprite.medic_bot.MEDIC_MOVE_LEFT = True
                move_medic_count = -100
                medic_left += 1
            #Умова змінення позиції медику за межою екрана
            if medic_left == 2:
                sprite.medic_bot.MEDIC_MOVE_LEFT = False
                sprite.medic_bot.X = 0
                sprite.medic_bot.Y = 190
            #Умова зміни напрямку переміщення медику
            if medic_left == 4:
                #Умова за якою медик змінює напрямок руху зліва на право
                if medic_left_count_1 != 1:
                    sprite.medic_bot.MEDIC_MOVE_LEFT = False
                    sprite.medic_bot.X = 0
                    sprite.medic_bot.Y = 0
                    medic_left_count_1 += 1
                    move_medic_right = True
                    medic_left = 0
                    move_medic_left = False
            #Умова у якій дається наказ переміщення медику вправ
            if move_medic_count == 150 and medic_right != 6 and move_medic_right == True:
                medic_left_count_1 = 0
                sprite.medic_bot.MEDIC_MOVE_LEFT = False
                sprite.medic_bot.MEDIC_MOVE_RIGHT = True
                move_medic_count = -100
                medic_right += 1
            #Переміщення медику вправо
            if medic_right == 1:
                if medic_right_count_1 != 1:
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 70
            #Умова змінення позиції медику на мапі
            if medic_right == 3:
                if medic_right_count_2 != 1:
                    sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                    sprite.medic_bot.X = 750
                    sprite.medic_bot.Y = 630
                    medic_right_count_2 += 1
            #Умова змінення позиції медику на мапі
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
            #Умова змінення позиції медику на мапі
            if last_medic_time_move > 2250 and last_medic_time_move_count < 3:
                sprite.medic_bot.X = 0
                sprite.medic_bot.Y = 660
                last_medic_time_move = 0
                last_medic_time_move_count += 1
                if last_medic_time_move_count == 2:
                    last_medic_time_move += 1800
            #Відрисовка картинки побігу медика у випадку його побігу
            if last_medic_time_move_count >= 3:
                sprite.medic_escape.blit_sprite(win)
            #Умова зупинення руху медика та зупинення його лічильнику
            if move_medic_count > 151:
                move_medic_count = 0
            #Умова закінчення 2 рівня та початку 3
            if sprite.flag_level_3:
                level3 = True #Умова яка робить змінну яка відповідає за 3 рівень дійсною
                list_create_world, list_rect = area.create_world(area.list_world_3)
                level2 = False #Умова яка робить змінну яка відповідає за 2 рівень НЕ дійсною
                #Змінення музики
                music.level2_background_sound.stop()
                music.level2_background_sound.unload()
        
        #Умова за якою відкривається 3 рівень гри  
        if level3:
            #Цикл всіх івентів у 3 рівні гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
                #Умова дій при натисненні на якусь частину екрану 3 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                   click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                   print(click) #Виведення координат натиснення ігрока
   
            # sprite.sprite.can_move_down(area.list_rect)
            #Відрисовка фону 3 рівня
            settings.bg.blit_sprite(win)
            #Створення блоків на мапі 3 рівня
            for el in list_create_world:
                el.blit_sprite(win)
            #Умови зникнення вогню на мапі 3 рівня
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
            #Умови відрисовки вогню на мапі 3 рівня
            sprite.sprite_3.fire(sprite.fire1, 1)
            sprite.sprite_3.fire(sprite.fire2, 2)
            sprite.sprite_3.fire(sprite.fire3, 3)
            sprite.sprite_3.fire(sprite.fire4, 4)
            sprite.sprite_3.fire(sprite.fire5, 5)
            sprite.sprite_3.fire(sprite.fire6, 6)
            sprite.sprite_3.fire(sprite.fire7, 7)
            sprite.door_3.blit_sprite(win)
            sprite.extinguisher.blit_sprite(win) #Відрисовка вогнегасника
            sprite.panel.blit_sprite(win)
            sprite.sprite_3.move_sprite()
            sprite.sprite_3.can_move_right(list_rect)
            sprite.sprite_3.can_move_left(list_rect)
            sprite.sprite_3.jump(list_rect)
            sprite.sprite_3.blit_sprite(win)
            sprite.sprite_3.gravity(list_rect= list_rect, sprite=1) 
            sprite.sprite_3.panel_collide()
            sprite.sprite_3.extinguisher_collide() #Взяття вогнегасника
            sprite.sprite_3.door_collide(sprite.door_3)
        if scene4:
            
            for event in pygame.event.get():
                
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
            # print(list_pipes)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                   click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                   print(click) #Виведення координат натиснення ігрока
                   
                   for pipe in list_pipes:
                    #    print(pipe.DIRECTION)
                       if pipe.RECT.collidepoint(event.pos):
                           pipe.IMAGE = pygame.transform.rotate(pipe.IMAGE, 90)
                           pipe.DIRECTION += 1
                           print(pipe.DIRECTION)
                           if pipe.DIRECTION > 4:
                               pipe.DIRECTION = 1
            settings.bg_pipes.blit_sprite(win)  
            for el in list_pipes:
                # print(el)
                el.blit_sprite(win)  
            # print(len(list_pipes))
            for i in range(21):
                # print(list_pipes[i])
                # pass
                if list_pipes[i].DIRECTION == tubings.dict_right_directions[str(i + 1)]:
                    print(111111)
            # sprite.pipe_1.blit_sprite(win)
            # sprite.pipe_2.blit_sprite(win)
            # sprite.pipe_3.blit_sprite(win)
            # sprite.pipe_4.blit_sprite(win)
        #Умова за якою відкривається розділ розробників 
        if level4:
            
            for event in pygame.event.get():
                
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
            settings.bg.blit_sprite(win)
        if scene3:
            #Відрисовка об'єктів у розділі розробників
            settings.bg_developers.blit_sprite(win)
            settings.back.blit_sprite(win)
            #Цикл всіх івентів у розділі розробників
            for event in pygame.event.get():
                #Умова дій при натисненні на якусь частину екрану 3 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    #Умова відкриття 1 рівня при натисненні на кнопку play
                    if settings.back.RECT.collidepoint(click):
                        scene1 = True #Робимо сцену меню дійсною завдяки чому відкривається меню
                        scene3 = False #Робимо сцену розділу розробників не дійсною завдяки чому розділ розробників закривається
                #Умова змінення розмірів кнопок при наведенні на них курсором
                if event.type == pygame.MOUSEMOTION:
                    #Умова зменшення кнопки при наведенні на неї курсором
                    if settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 715,y = 0, width = 75, height = 45,name_image = "game2/images/back.png")
                    #Умова НЕ зменшення кнопки коли курсор не наведен на неї
                    if not settings.back.RECT.collidepoint(event.pos):
                        settings.back = settings.Settings(x = 700,y = 0, width = 100, height = 50,name_image = "game2/images/back.png")
        #Оновлення екрану гри
        pygame.display.flip()
        #Задання ФПС гри
        #print(clock)
        clock.tick(fps)
#Визов головної функції гри у якій є майже все  
run_game()