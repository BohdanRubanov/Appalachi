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
                    "game2/images/exit.png", "game2/images/background/bg_red.png", "game2/images/background/bg.png", "game2/images/background/smoke1.png",
                    "game2/images/background/smoke2.png", "game2/images/background/smoke3.png", "game2/images/background/smoke4.png", "game2/images/background/smoke5.png",
                    "game2/images/background/smoke6.png", "game2/images/background/smoke7.png", "game2/images/background/smoke8.png", "game2/images/background/smoke9.png", 
                    "game2/images/fire/fire1.png", "game2/images/fire/fire2.png", "game2/images/fire/fire3.png", "game2/images/fire/fire4.png",
                    "game2/images/background/bg_with_fire1.png", "game2/images/background/bg_with_fire2.png", "game2/images/background/bg_with_fire3.png", "game2/images/background/bg_with_fire4.png",
                    "game2/images/background/bg_with_smoke1_red.png", "game2/images/background/bg_with_smoke2_red.png", "game2/images/background/bg_with_smoke3_red.png",
                    "game2/images/background/bg_with_smoke4_red.png", "game2/images/background/bg_with_smoke5_red.png", "game2/images/background/bg_with_smoke6_red.png",
                    "game2/images/background/bg_with_smoke7_red.png", "game2/images/background/bg_with_smoke8_red.png", "game2/images/background/bg_with_smoke9_red.png",
                    "game2/images/background/bg_gray.png", "game2/images/background/bg_with_fire5.png", "game2/images/background/bg_with_fire6.png",
                    "game2/images/background/bg_with_fire7.png", "game2/images/background/bg_with_fire8.png", "game2/images/background/bg_with_fire9.png",]
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
name_bg = load_name_image("background/bg")
name_bg_red = load_name_image("background/bg_red")
smoke1 = load_name_image("background/smoke1")
smoke2 = load_name_image("background/smoke2")
smoke3 = load_name_image("background/smoke3")
smoke4 = load_name_image("background/smoke4")
smoke5 = load_name_image("background/smoke5")
smoke6 = load_name_image("background/smoke6")
smoke7 = load_name_image("background/smoke7")
smoke8 = load_name_image("background/smoke8")
smoke9 = load_name_image("background/smoke9")
bg_red_with_smoke1 = load_name_image("background/bg_with_smoke1_red")
bg_red_with_smoke2 = load_name_image("background/bg_with_smoke2_red")
bg_red_with_smoke3 = load_name_image("background/bg_with_smoke3_red")
bg_red_with_smoke4 = load_name_image("background/bg_with_smoke4_red")
bg_red_with_smoke5 = load_name_image("background/bg_with_smoke5_red")
bg_red_with_smoke6 = load_name_image("background/bg_with_smoke6_red")
bg_red_with_smoke7 = load_name_image("background/bg_with_smoke7_red")
bg_red_with_smoke8 = load_name_image("background/bg_with_smoke8_red")
bg_red_with_smoke9 = load_name_image("background/bg_with_smoke9_red")
bg_gray = load_name_image("background/bg_gray")
bg_with_fire_1 = load_name_image("background/bg_with_fire1")
bg_with_fire_2 = load_name_image("background/bg_with_fire2")
bg_with_fire_3 = load_name_image("background/bg_with_fire3")
bg_with_fire_4 = load_name_image("background/bg_with_fire4")
bg_with_fire_5 = load_name_image("background/bg_with_fire5")
bg_with_fire_6 = load_name_image("background/bg_with_fire6")
bg_with_fire_7 = load_name_image("background/bg_with_fire7")
bg_with_fire_8 = load_name_image("background/bg_with_fire8")
bg_with_fire_9 = load_name_image("background/bg_with_fire9")

fire_img1 = load_name_image("fire/fire1")
fire_img1 = pygame.transform.scale(fire_img1, (80, 50))
fire_img2 = load_name_image("fire/fire2")
fire_img2 = pygame.transform.scale(fire_img2, (80, 50))
fire_img3 = load_name_image("fire/fire3")
fire_img3 = pygame.transform.scale(fire_img3, (80, 50))
fire_img4 = load_name_image("fire/fire4")
fire_img4 = pygame.transform.scale(fire_img4, (80, 50))

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
scene1 = True #Меню
backstory = False #Початкова предисторія
level1 = False#1 рівень
comix_2 = False
comix_3 = False
comix_4 = False
level2 = False #2 рівень
level3 = False #3 рівень
scene3 = False #Розробники
scene4 = False #Чорний экран
level4 =   False #Мініігра надування лодки
death_scene1 = False
death_scene2 = False
death_scene3 = False
death_scene4 = False
win_1 = False
#Лічильник диму за допомогою якого змінюються розміри диму
smoke_count = 0 
#Заданий ФПС гри
fps = 60
#тимчасова музика для 3 рівня
music.menu_background_sound.load()
music.menu_background_sound.play(repeat=-1)
#Создавання об'єкту вікна гри
win = pygame.display.set_mode((dicts.SETTINGS_WIN["WIDTH"], dicts.SETTINGS_WIN["HEIGHT"]))
#Задання назви вікну гри
pygame.display.set_caption("Appalachi")
pygame_icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(pygame_icon)
list_pipes = []
list_rect_pipes = []
#Все те що відноситься до матриці
list_create_world = []
list_rect = []
list_pipes, list_rect_pipes = tubings.create_world(tubings.list_pipe_matrix)
list_create_world, list_rect = area.create_world(area.list_world_3)
#Головна функція гри у якій міститься майже все
smoke_width = 50
smoke_height = 50
smoke_y = 800
smoke_x = 0
smoke = sprite.Sprite(x = smoke_x, y = smoke_y, width = smoke_width, height = smoke_height, name_image = "game2/images/smoke.png")
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
    global death_scene1
    global death_scene2
    global death_scene3
    global death_scene4
    global backstory
    global comix_2, comix_3, comix_4
    global win_1
    #Лічильники
    menu_count = 0 #Лічильник для анімацій у меню
    fire_flag = True
    move_medic_count = 0
    medic_left_count_1 = 0
    medic_right_count_1 = 0
    medic_right_count_2 = 0
    medic_right_count_3 = 0
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
    fire_count = 0 
    blit_count = 0
    bg_fire_count = 0
    #Головний цикл гри у якому міститься майже все
    global smoke_count
    global level2
    global level3, level4
    global scene4
    fire_anim_count = 0
    while game:
        
        if sprite.sprite_3.SCENE5:
            level3 = False
            comix_4 = True
        #Медик починає рух
        last_medic_time_move += 1
        #Лічильнік починає лічити до того значення на якому медик зупиниться
        move_medic_count += 1
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
                    #print(click) #Виведення координат натиснення ігрока
                    #Умова відкриття 1 рівня при натисненні на кнопку play
                    if settings.play.RECT.collidepoint(click):
                        page_num = 1
                        sprite.page.NAME_IMAGE = "game2/images/comix/page_1.png" 
                        backstory = True #Создавання матриці 1 рівня                      
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
            #Цикл всіх івентів у предісторії гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False 
                #Умова дій при натисненні на якусь частину екрану предісторії гри
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    #print(click) #Виведення координат натиснення ігрока
                    #Умова відкриття наступної сторінк  при натисненні на кнопку стрілки вправо
                    if sprite.arrow1.RECT.collidepoint(click):
                        pages_time_black_time = 0
                        #Умова перегортання сторінки на наступну
                        if page_num <= 11:
                            page_num += 1
                            flag_black_pages = True
                    #Умова відкриття наступної сторінк  при натисненні на кнопку стрілки вліво
                    if sprite.arrow2.RECT.collidepoint(click):
                        pages_time_black_time = 0
                        #Умова перегортання сторінки на минулу
                        if page_num >= 2:
                            page_num -= 1
                            flag_black_pages = True
                    if sprite.button_skip.RECT.collidepoint(click):
                        page_num = 12
                        sprite.page.NAME_IMAGE = "game2/images/comix/page_12.png" 
                    if sprite.button_start.RECT.collidepoint(click):
                        level1 = True #Змінна яка робить level1 дійсним за допомогою чого запускається 1 рівень
                        music.menu_background_sound.stop() #Зупинення музику у меню
                        music.menu_background_sound.unload() #Видалення музику у меню з гри на тей час поки в неї нема потреби
                        music.level1_background_sound.load() #Загрузка музики 1 рівня
                        music.level1_background_sound.play(repeat=-1) #Початок гри музики 1 рівня
                        list_create_world, list_rect = area.create_world(area.list_world_1)
                        backstory = False
            settings.bg_menu.blit_sprite(win)
            #Відрисовка об'єктів предісторії
            sprite.page.blit_sprite(win) 
             
            if page_num == 12: 
                sprite.button_start.blit_sprite(win)
                sprite.arrow2.blit_sprite(win)
            elif page_num == 1:
                sprite.arrow1.blit_sprite(win) 
                sprite.button_skip.blit_sprite(win)
            else:
                sprite.button_skip.blit_sprite(win) 
                sprite.arrow1.blit_sprite(win) 
                sprite.arrow2.blit_sprite(win)
            #Умова переходу з сторінки на сторінку
            if flag_black_pages:
                pages_time_black_time += 1 #Лічильник часу переходу з сторінки на сторінку починає працювати
                #Умова відрисовки чорної картинки під час переходу коли лічильник pages_time_black_time буде мати значення менше за 50
                if pages_time_black_time < 25:    
                    sprite.black.blit_sprite(win)   
                    sprite.page.NAME_IMAGE = "game2/images/comix/black.png"  
                    sprite.page.load_image() 
                #Умова відрисовки сторінки під час переходу коли лічильник pages_time_black_time буде мати значення більше за 50
                if pages_time_black_time >= 25:       
                    sprite.page.NAME_IMAGE = f"game2/images/comix/page_{page_num}.png" 
            sprite.page.load_image()
         
        #Умова за якою відкривається 1 рівень гри
        if level1:
            #Цикл всіх івентів у 1 рівні гри
            for event in pygame.event.get():
                #Умова дій при натисненні на якусь частину екрану 1 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    #print(click) #Виведення координат натиснення ігрока
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
            
            smoke_count += 1 #Лічильник диму починає працю
            if smoke_count < 100:
                settings.bg.IMAGE = name_bg
            if smoke_count > 100 and smoke_count < 200:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke1
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke1
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 200 and smoke_count < 300:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke2
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke2
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 300 and smoke_count < 400:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke3
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke3
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 400 and smoke_count < 500:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke4
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke4
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 500 and smoke_count < 600:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke5
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke5
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 600 and smoke_count < 700:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke6
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke6
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 700 and smoke_count < 800:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke7
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke7
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 800 and smoke_count < 900:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke8
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke8
                if blit_count == 60:
                    blit_count = 0
            if smoke_count > 900:
                blit_count += 1
                if blit_count == 20:
                    settings.bg.IMAGE = smoke9
                if blit_count == 40:
                    settings.bg.IMAGE = bg_red_with_smoke9
                if blit_count == 60:
                    blit_count = 0
            settings.bg.blit_sprite(win)
            for el in list_create_world:
                el.blit_sprite(win)
            sprite.sprite.can_move_right(list_rect)
            sprite.sprite.can_move_left(list_rect)
            sprite.sprite.move_sprite()
            sprite.sprite.jump(list_rect)
            sprite.sprite.blit_sprite(win)
            sprite.sprite.gravity(list_rect= list_rect, sprite=1)
            #Умова відрисовки противогазу
            sprite.mask.gravity(list_rect= list_rect)
            settings.lever.blit_sprite(win)
            if settings.injured.IMAGE != None:
                settings.injured.blit_sprite(win)
            sprite.sprite.lever_collide(win)
            sprite.sprite.mask_collide(win)
            if sprite.mask.IMAGE != None:
                sprite.mask.blit_sprite(win)
            sprite.sprite.injured_collide()
            #Умова відрисовки одної з дверей
            if sprite.door.IMAGE != None:
                sprite.door.blit_sprite(win)
            sprite.sprite.door_collide(sprite.door)
            sprite.door_exit.blit_sprite(win)
            sprite.sprite.door_exit_collide()
            #Умова відрисовки блоків на мапі першого рівня
            
            
            #Умова змінення позиції об'єкту диму
            if smoke_count ==  101 or smoke_count ==  201 or smoke_count ==  301 or smoke_count ==  401 or smoke_count ==  501 or smoke_count ==  601 or smoke_count ==  701 or smoke_count ==  801 or smoke_count ==  901:
                # Змінення розмірів та позиції об'єкту диму
                smoke_width += 80
                smoke_height += 80
                smoke_y -= 80
                smoke.RECT.y = smoke_y           
                smoke.RECT.height = smoke_height
                smoke.RECT.width = smoke_width
            #Умова програшу від диму
            if sprite.sprite.X + sprite.sprite.WIDTH <= smoke_x + smoke_width + 20 and sprite.sprite.X + 20 >= smoke_x:
                if sprite.sprite.Y + 21 >= smoke_y and sprite.sprite.Y + sprite.sprite.HEIGHT <= smoke_y + smoke_height + 20:
                    if sprite.sprite.MASK_ON == True:
                        pass
                    else:
                        sprite.sprite.X = 330
                        sprite.sprite.Y = 600
                        #Змінення параметрів диму на стандартні після програшу ігрока
                        smoke = sprite.Sprite(x = 0, y = 750, width = 50, height = 50, name_image = "game2/images/smoke.png")
                        smoke_width = 50
                        smoke_height = 50
                        smoke_x = 0
                        smoke_y = 750
                        #Змінення сцен
                        level1 = False
                        death_scene1 = True
                        #Змінення музики
                        music.level1_background_sound.stop()
                        music.level1_background_sound.unload()
                        music.die_smoke_version.play()
                        #Обнуляємо лічильник диму
                        smoke_count = 0
    
            #Робимо змінну яка у себе записує яка клавіша була натиснена
            event = pygame.key.get_pressed()
            #Умова проходження та закінчення 1 рівня та переходу до 2
            if sprite.sprite.EXIT_DOOR:
                level1 = False
                comix_2 = True

        #Умова за якою відкривається 2 рівень гри
        if level2: 
            #Умова початку відигрування музики 2 рівня
            if not pygame.mixer.music.get_busy():
                music.level2_background_sound.load()
                music.level2_background_sound.play(repeat=-1)
            #Цикл всіх івентів у 2 рівні гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
                #Умова дій при натисненні на якусь частину екрану 2 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    #print(click) #Виведення координат натиснення ігрока
            blit_count += 1
            if blit_count < 20:
                settings.bg.IMAGE = bg_gray
            if blit_count > 20:
                settings.bg.IMAGE = name_bg_red
            if blit_count == 40:
                blit_count = 0
            settings.bg.blit_sprite(win)
            for el in list_create_world:
                el.blit_sprite(win)
            
            
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
                death_scene2 = True #Роблення сцени меню гри дійсною тим самим відкривається меню
                level2 = False #Роблення сцени другого рівня не дійсною тим самим відбувається закінчення 2 рівня
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
                level2 = False
                comix_3 = True
                
        
        #Умова за якою відкривається 3 рівень гри  
        if level3:
            music.level3.play()
            music.menu_background_sound.stop()
            #Цикл всіх івентів у 3 рівні гри
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  
                #Умова дій при натисненні на якусь частину екрану 3 рівня
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                   click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                   #print(click) #Виведення координат натиснення ігрока
   
            #Відрисовка фону 3 рівня
            bg_fire_count += 1
            fire_count += 1
            fire_anim_count += 1
            settings.bg.blit_sprite(win)
            if fire_flag:
                if bg_fire_count < 150:
                    settings.bg.IMAGE = name_bg
                if bg_fire_count > 150 and fire_anim_count < 800:
                    if sprite.sprite_3.Y >= 565:
                        music.level3.stop()
                        death_scene3 = True
                        level3 = False
                    if bg_fire_count > 150 and bg_fire_count < 155:
                        settings.bg.IMAGE = bg_with_fire_1
                    if bg_fire_count > 155 and bg_fire_count < 160:
                        settings.bg.IMAGE = bg_with_fire_2
                    if bg_fire_count > 160 and bg_fire_count < 165:
                        settings.bg.IMAGE = bg_with_fire_3
                    if bg_fire_count > 165 and bg_fire_count < 170:
                        settings.bg.IMAGE = bg_with_fire_4
                    if bg_fire_count == 170:
                        bg_fire_count = 150
                if bg_fire_count > 150 and fire_anim_count < 1600 and fire_anim_count > 800:
                    if sprite.sprite_3.Y >= 315:
                        music.level3.stop()
                        death_scene3 = True
                        level3 = False
                    if bg_fire_count > 150 and bg_fire_count < 155:
                        settings.bg.IMAGE = bg_with_fire_5
                    if bg_fire_count > 155 and bg_fire_count < 160:
                        settings.bg.IMAGE = bg_with_fire_6
                    if bg_fire_count > 160 and bg_fire_count < 165:
                        settings.bg.IMAGE = bg_with_fire_7
                    if bg_fire_count == 170:
                        bg_fire_count = 150  
                if bg_fire_count > 150 and fire_anim_count > 1600:
                    if sprite.sprite_3.Y >= 180:
                            music.level3.stop()
                            death_scene3 = True
                            level3 = False
                    if bg_fire_count > 150 and bg_fire_count < 155:
                        settings.bg.IMAGE = bg_with_fire_8
                    if bg_fire_count > 155 and bg_fire_count < 160:
                        settings.bg.IMAGE = bg_with_fire_9
                    if bg_fire_count == 170:
                        bg_fire_count = 150   
            else:
                settings.bg.IMAGE = name_bg
            #Створення блоків на мапі 3 рівня
            for el in list_create_world:
                el.blit_sprite(win)
            if fire_count < 5:
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 350:
                    if not sprite.fire1.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_1 = True
                        sprite.fire1.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 700:
                    if not sprite.fire2.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_2 = True
                        sprite.fire2.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1050:
                    if not sprite.fire3.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_3 = True
                        sprite.fire3.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1400:
                    if not sprite.fire4.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_4 = True
                        sprite.fire4.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1750:
                    if not sprite.fire5.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_5 = True
                        sprite.fire5.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2100:
                    if not sprite.fire6.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_6 = True
                        sprite.fire6.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2450:
                    if not sprite.fire7.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_7 = True
                        sprite.fire7.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2800:
                    if not sprite.fire8.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_8 = True
                        sprite.fire8.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3150:
                    if not sprite.fire9.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_9 = True
                        sprite.fire9.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3500:
                    if not sprite.fire10.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_10 = True
                        sprite.fire10.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3850:
                    if not sprite.fire11.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_11 = True
                        sprite.fire11.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4200:
                    if not sprite.fire12.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_12 = True
                        sprite.fire12.IMAGE = fire_img1
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4550:
                    if not sprite.fire13.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_13 = True
                        sprite.fire13.IMAGE = fire_img1
            if fire_count > 5 and fire_count < 10:
                if not sprite.fire1.NO_FIRE:
                    sprite.fire1.BLIT_FIRE_1 = True
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 350:
                    if not sprite.fire1.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_1 = True
                        sprite.fire1.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 700:
                    if not sprite.fire2.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_2 = True
                        sprite.fire2.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1050:
                    if not sprite.fire3.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_3 = True
                        sprite.fire3.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1400:
                    if not sprite.fire4.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_4 = True
                        sprite.fire4.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1750:
                    if not sprite.fire5.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_5 = True
                        sprite.fire5.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2100:
                    if not sprite.fire6.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_6 = True
                        sprite.fire6.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2450:
                    if not sprite.fire7.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_7 = True
                        sprite.fire7.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2800:
                    if not sprite.fire8.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_8 = True
                        sprite.fire8.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3150:
                    if not sprite.fire9.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_9 = True
                        sprite.fire9.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3500:
                    if not sprite.fire10.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_10 = True
                        sprite.fire10.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3850:
                    if not sprite.fire11.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_11 = True
                        sprite.fire11.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4200:
                    if not sprite.fire12.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_12 = True
                        sprite.fire12.IMAGE = fire_img2
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4550:
                    if not sprite.fire13.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_13 = True
                        sprite.fire13.IMAGE = fire_img2
            if fire_count > 10 and fire_count < 15:
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 350:
                    if not sprite.fire1.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_1 = True
                        sprite.fire1.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 700:
                    if not sprite.fire2.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_2 = True
                        sprite.fire2.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1050:
                    if not sprite.fire3.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_3 = True
                        sprite.fire3.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1400:
                    if not sprite.fire4.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_4 = True
                        sprite.fire4.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1750:
                    if not sprite.fire5.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_5 = True
                        sprite.fire5.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2100:
                    if not sprite.fire6.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_6 = True
                        sprite.fire6.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2450:
                    if not sprite.fire7.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_7 = True
                        sprite.fire7.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2800:
                    if not sprite.fire8.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_8 = True
                        sprite.fire8.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3150:
                    if not sprite.fire9.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_9 = True
                        sprite.fire9.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3500:
                    if not sprite.fire10.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_10 = True
                        sprite.fire10.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3850:
                    if not sprite.fire11.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_11 = True
                        sprite.fire11.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4200:
                    if not sprite.fire12.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_12 = True
                        sprite.fire12.IMAGE = fire_img3
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4550:
                    if not sprite.fire13.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_13 = True
                        sprite.fire13.IMAGE = fire_img3
            if fire_count > 15 and fire_count < 20:
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 350:
                    if not sprite.fire1.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_1 = True
                        sprite.fire1.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 700:
                    if not sprite.fire2.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_2 = True
                        sprite.fire2.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1050:
                    if not sprite.fire3.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_3 = True
                        sprite.fire3.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1400:
                    if not sprite.fire4.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_4 = True
                        sprite.fire4.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 1750:
                    if not sprite.fire5.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_5 = True
                        sprite.fire5.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2100:
                    if not sprite.fire6.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_6 = True
                        sprite.fire6.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2450:
                    if not sprite.fire7.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_7 = True
                        sprite.fire7.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 2800:
                    if not sprite.fire8.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_8 = True
                        sprite.fire8.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3150:
                    if not sprite.fire9.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_9 = True
                        sprite.fire9.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3500:
                    if not sprite.fire10.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_10 = True
                        sprite.fire10.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 3850:
                    if not sprite.fire11.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_11 = True
                        sprite.fire11.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4200:
                    if not sprite.fire12.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_12 = True
                        sprite.fire12.IMAGE = fire_img4
                if sprite.sprite_3.COUNT_FIRE_POSITION >= 4550:
                    if not sprite.fire13.NO_FIRE:
                        sprite.sprite_3.BLIT_FIRE_13 = True
                        sprite.fire13.IMAGE = fire_img4
            if fire_count == 20:
                fire_count = 0
            if fire_flag:
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
                if sprite.sprite_3.BLIT_FIRE_8:
                    sprite.fire8.blit_sprite(win)
                if sprite.sprite_3.BLIT_FIRE_9:
                    sprite.fire9.blit_sprite(win)
                if sprite.sprite_3.BLIT_FIRE_10:
                    sprite.fire10.blit_sprite(win)
                if sprite.sprite_3.BLIT_FIRE_11:
                    sprite.fire11.blit_sprite(win)
                if sprite.sprite_3.BLIT_FIRE_12:
                    sprite.fire12.blit_sprite(win)
                if sprite.sprite_3.BLIT_FIRE_13:
                    sprite.fire13.blit_sprite(win)
            #Умови відрисовки вогню на мапі 3 рівня
            sprite.sprite_3.fire(sprite.fire1, 1)
            sprite.sprite_3.fire(sprite.fire2, 2)
            sprite.sprite_3.fire(sprite.fire3, 3)
            sprite.sprite_3.fire(sprite.fire4, 4)
            sprite.sprite_3.fire(sprite.fire5, 5)
            sprite.sprite_3.fire(sprite.fire6, 6)
            sprite.sprite_3.fire(sprite.fire7, 7)
            sprite.sprite_3.fire(sprite.fire8, 8)
            sprite.sprite_3.fire(sprite.fire9, 9)
            sprite.sprite_3.fire(sprite.fire10, 10)
            sprite.sprite_3.fire(sprite.fire11, 11)
            sprite.sprite_3.fire(sprite.fire12, 12)
            sprite.sprite_3.fire(sprite.fire13, 13)
            sprite.door_3.blit_sprite(win)
            if not sprite.sprite_3.EXTING_ON:
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
            if sprite.blue.BLUE:
                try:
                    sprite.blue.blit_sprite(win)
                    sprite.blue.blit_blue()
                    sprite.blue.load_image()
                except:
                    sprite.fire1.FLAG_DEATH_FIRE = False
                    sprite.fire2.FLAG_DEATH_FIRE = False
                    sprite.fire3.FLAG_DEATH_FIRE = False
                    sprite.fire4.FLAG_DEATH_FIRE = False
                    sprite.fire5.FLAG_DEATH_FIRE = False
                    sprite.fire6.FLAG_DEATH_FIRE = False
                    sprite.fire7.FLAG_DEATH_FIRE = False
                    sprite.fire8.FLAG_DEATH_FIRE = False
                    sprite.fire9.FLAG_DEATH_FIRE = False
                    sprite.fire10.FLAG_DEATH_FIRE = False
                    sprite.fire11.FLAG_DEATH_FIRE = False
                    sprite.fire12.FLAG_DEATH_FIRE = False
                    sprite.fire13.FLAG_DEATH_FIRE = False
                    sprite.blue.BLUE = False
                    fire_flag = False
            sprite.sprite_3.door_collide(sprite.door_3)
            if sprite.sprite_3.DEATH_FIRE:
                music.level3.stop()
                death_scene3 = True
                level3 = False
        if scene4:
            music.pipes_minigame.play()
            for event in pygame.event.get():
                
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False  

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                   click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                   #print(click) #Виведення координат натиснення ігрока
                   
                   for pipe in list_pipes:
                       if pipe.RECT.collidepoint(event.pos):
                           pipe.IMAGE = pygame.transform.rotate(pipe.IMAGE, 90)
                           pipe.DIRECTION += 1
                           if pipe.DIRECTION > 4:
                               pipe.DIRECTION = 1
                           if pipe.NAME_IMAGE == "game2/images/pipes/pipe2.png" and pipe.DIRECTION > 2:
                               pipe.DIRECTION = 1
            settings.bg_pipes.blit_sprite(win)  
            for el in list_pipes:
                el.blit_sprite(win)  
            pipes_flag = True
            for key in tubings.dict_right_directions.keys():
                if list_pipes[int(key)].DIRECTION == tubings.dict_right_directions[key]:
                    pass
                else:
                    pipes_flag = False
                    break
            if pipes_flag:
                sprite.blue.BLUE = True
                sprite.sprite_3.ENTER_DOOR = True
                scene4 = False
                sprite.sprite_3.SCENE4 = False
        #Умова за якою відкривається розділ розробників 
        if level4:
            music.inflation_minigame.play()
            try:
                for event in pygame.event.get():

                    #Умова виходу з гри при натисненні хрестику
                    if event.type == pygame.QUIT:
                        game = False  
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        click = event.pos 
                        if sprite.pump.RECT.collidepoint(click):

                            sprite.pump_scale.HEIGHT += 7
                            sprite.pump_scale.Y -= 7
                            sprite.pump_scale.load_image()
                settings.bg_minigame.blit_sprite(win)
                sprite.pump.blit_sprite(win)    
                sprite.pump_scale.blit_sprite(win)  
                sprite.boat.blit_sprite(win) 
                if not sprite.hole1.HOLE_COUNT:
                    sprite.hole1.blit_sprite(win)
                    sprite.pump_scale.HEIGHT -= 1
                    sprite.pump_scale.Y += 1
                    sprite.pump_scale.load_image()
                sprite.hole1.hole()
                
            except:
                music.inflation_minigame.stop()
                death_scene4 = True
                level4 = False
            if sprite.pump_scale.HEIGHT >= 175:
                    music.inflation_minigame.stop()
                    level4 = False
                    win_1 = True
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
        if death_scene1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if sprite.button_menu.RECT.collidepoint(click):
                        scene1 = True
                        death_scene1 = False
                    if sprite.button_one_more.RECT.collidepoint(click):
                        level1 = True
                        death_scene1 = False
            sprite.death.blit_sprite(win)
            sprite.button_menu.blit_sprite(win)
            sprite.button_one_more.blit_sprite(win)
        if death_scene2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if sprite.button_menu.RECT.collidepoint(click):
                        scene1 = True
                        death_scene2 = False
                    if sprite.button_one_more.RECT.collidepoint(click):
                        music.level2_background_sound.load()
                        music.level2_background_sound.play(repeat=-1)
                        sprite.medic_bot.MEDIC_MOVE_RIGHT = False
                        sprite.medic_bot.MEDIC_MOVE_LEFT = False
                        sprite.sprite_2.X = 400
                        sprite.sprite_2.Y = 500
                        sprite.medic_bot.X = 20
                        sprite.medic_bot.Y = 660
                        move_medic_count = 0
                        medic_left_count_1 = 0
                        medic_right_count_1 = 0
                        medic_right_count_2 = 0
                        medic_right_count_3 = 0
                        medic_right = 0
                        medic_left = 0
                        last_medic_time_move_count = 0
                        bullet.flag_bullet_die = False
                        level2 = True
                        death_scene2 = False
            sprite.death.blit_sprite(win)
            sprite.button_menu.blit_sprite(win)
            sprite.button_one_more.blit_sprite(win)
        if death_scene3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if sprite.button_menu.RECT.collidepoint(click):
                        scene1 = True
                        death_scene3 = False
                    if sprite.button_one_more.RECT.collidepoint(click):
                        sprite.fire1 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire2 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire3 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire4 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire5 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire6 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire7 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire8 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire9 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire10 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire11 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire12 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        sprite.fire13 = sprite.Sprite(x = 1500, y = 1500, width = 80, height = 50, name_image = "game2/images/fire/fire1.png")
                        fire_anim_count = 0
                        bg_fire_count = 0
                        sprite.sprite_3.X = 300
                        sprite.sprite_3.Y = 650
                        sprite.sprite_3.EXTING_ON = False
                        sprite.sprite_3.COUNT_FIRE_POSITION = 0
                        fire_count = 0
                        sprite.sprite_3.DEATH_FIRE = False
                        level3 = True
                        death_scene3 = False
            sprite.death.blit_sprite(win)
            sprite.button_menu.blit_sprite(win)
            sprite.button_one_more.blit_sprite(win)
        if death_scene4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click = event.pos
                    if sprite.button_menu.RECT.collidepoint(click):
                        scene1 = True
                        death_scene1 = False
                    if sprite.button_one_more.RECT.collidepoint(click):
                        sprite.pump_scale.HEIGHT = 100
                        sprite.pump_scale.Y = 250
                        sprite.pump_scale.load_image()
                        music.menu_background_sound.stop()
                        level4 = True
                        death_scene4 = False
            sprite.death.blit_sprite(win)
            sprite.button_menu.blit_sprite(win)
            sprite.button_one_more.blit_sprite(win)
        if comix_2:
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False 
                #Умова дій при натисненні на якусь частину екрану предісторії гри
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    if sprite.button_start.RECT.collidepoint(click):
                        
                            sprite.sprite.X = 330
                            sprite.sprite.Y = 600
                            sprite.sprite.MASK_ON = False
                            sprite.sprite.INJURED = False
                            sprite.mask.NAME_IMAGE = "game2/images/mask.png"
                            sprite.mask.load_image()
                            sprite.door.NAME_IMAGE = "game2/images/door.png"
                            sprite.door.load_image()
                            settings.injured.NAME_IMAGE = "game2/images/injured.png"
                            settings.injured.load_image()
                            level2 = True #Робимо level2 дійсним тим самим починаємо 2 рівень
                            list_create_world, list_rect = area.create_world(area.list_world_2)
                            #Змінення музики
                            music.level1_background_sound.stop()
                            music.level1_background_sound.unload()
                             #Робимо level1 не дійсним тим самим закінчуємо 1 рівень
                            sprite.sprite.EXIT_DOOR = False
                            comix_2 = False
            sprite.page_level_2.blit_sprite(win)
            sprite.button_start.blit_sprite(win)
                
        if comix_3:
            
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False 
                #Умова дій при натисненні на якусь частину екрану предісторії гри
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    #print(click)
                    if sprite.button_start.RECT.collidepoint(click):
                        level3 = True #Умова яка робить змінну яка відповідає за 3 рівень дійсною
                        list_create_world, list_rect = area.create_world(area.list_world_3) 
                        #Змінення музики
                        music.level2_background_sound.stop()
                        music.level2_background_sound.unload()
                        comix_3 = False
            sprite.page_level_3.blit_sprite(win)
            sprite.button_start.blit_sprite(win)
        if comix_4:
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False 
                #Умова дій при натисненні на якусь частину екрану предісторії гри
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    click = event.pos #Змінна яка записує у себе координати натиснення ігрока
                    #print(click)
                    if sprite.button_start.RECT.collidepoint(click):
                        level4 = True
                        sprite.sprite_3.SCENE5 = False
                        comix_4 = False
                        music.menu_background_sound.stop()
                        sprite.blue.BLUE = False
                        sprite.blue.FLAG_BLUE = False
            sprite.page_level_4.blit_sprite(win)
            sprite.button_start.blit_sprite(win)
        if win_1:
            for event in pygame.event.get():
                #Умова виходу з гри при натисненні хрестику
                if event.type == pygame.QUIT:
                    game = False 
            level4 = False
            music.inflation_minigame.stop()
            music.menu_background_sound.stop()
            music.pipes_minigame.stop()
            music.level3.stop()
            music.win_1.play()
            sprite.win_1.blit_sprite(win)
        #Оновлення екрану гри
        pygame.display.flip()
        #Задання ФПС гри
        clock.tick(fps)
#Визов головної функції гри у якій є майже все  
run_game()