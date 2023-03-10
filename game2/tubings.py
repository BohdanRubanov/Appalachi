import settings

win_height = 800
win_width = 800

pipe_w = 60
pipe_h = 60
list_pipe_matrix = [
    "00000000000",
    "20000000000",
    "12100000000",
    "12100000000",
    "20000000000",
    "20000000000",
    "20000000000",
    "12210000000",
    "00020000000", 
    "00012100000",
    "00000200000",
    "00000110000",
    "00122210000",
    "00000000000"
]

dict_right_directions= {
    "0": 2,
    "1": 2,
    "2": 1, 
    "3": 4,
    "4": 1,
    "5": 1,
    "6": 3,
    "7": 2,
    "8": 2,
    "9": 2,
    "10": 2,
    "11": 1,
    "12": 1,
    "13": 4,
    "14": 2,
    "15": 2,
    "16": 1,
    "17": 4,
    "18": 2,
    "19": 2,
    "20": 4,
    "21": 1,
    "22": 1,
    "23": 1,
    "24": 1,
    "25": 3
                    }

    
list_pipes = []
list_rect_pipe = []
class Pipes(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DIRECTION = 1

def create_world(level):
    list_pipes = []
    list_rect_pipe = []
    x = 0
    y = 0
    for string in level:
        for el in string:
            if el == "1":
                pipe = Pipes(
                    x= x,
                    y= y,
                    width= pipe_w,
                    height= pipe_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/pipes/pipe1.png")
                )
                list_pipes.append(pipe)
                list_rect_pipe.append(pipe)
            if el == "2":
                pipe = Pipes(
                    x= x,
                    y= y,
                    width= pipe_w,
                    height= pipe_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/pipes/pipe2.png")
                )
                list_pipes.append(pipe)
                list_rect_pipe.append(pipe)
            x += pipe_w
        x = 0
        y += pipe_h
    return list_pipes, list_rect_pipe