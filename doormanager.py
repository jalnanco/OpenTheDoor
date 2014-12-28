# -*- coding: utf-8 -*-
from randomdict import RandomDict
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


GHOST = {
    "maxhp":20,
    "hp":20,
    "ap":1,
    "exp":1,
    "gold":1,
    "name":"의문의 유령",
    "png":['data/ghost_normal.png','data/ghost.png', 'data/ghost_dead.png']
}
FLYFLY = {
    "maxhp":15,
    "hp":15,
    "ap":1,
    "exp":1,
    "gold":1,
    "name":"날파리",
    "png":['data/flyFly1.png','data/flyFly2.png', 'data/flyDead.png']
}
MOUSE = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"찍찍이",
    "png":['data/mouse.png','data/mouse_walk.png', 'data/mouse_dead.png']
}
BAT = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"박쥐",
    "png":['data/bat.png','data/bat_fly.png', 'data/bat_dead.png']
}
BEE = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"벌",
    "png":['data/bee.png','data/bee_fly.png', 'data/bee_dead.png']
}
FLY = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"파리",
    "png":['data/fly.png','data/fly_fly.png', 'data/fly_dead.png']
}
FROG = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"개굴이",
    "png":['data/frog.png','data/frog_leap.png', 'data/frog_dead.png']
}
SLIME_GREEN = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"초록 슬라임",
    "png":['data/slimeGreen.png','data/slimeGreen_walk.png', 'data/slimeGreen_dead.png']
}
SLIME_PINK = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"핑크 슬라임",
    "png":['data/slime.png','data/slime_walk.png', 'data/slime_dead.png']
}
SLIME_BLUE = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"블루 슬라임",
    "png":['data/slimeBlue.png','data/slimeBlue_blue.png', 'data/slimeBlue_dead.png']
}
SNAIL = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"달팽이 병정",
    "png":['data/snail.png','data/snail_walk.png', 'data/snail_shell.png']
}
SNAKELAVA = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"당근 벌레",
    "png":['data/snakeLava.png','data/snakeLava_ani.png', 'data/snakeLava_dead.png']
}
SNAKESLIME = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"초록 벌레",
    "png":['data/snakeSlime.png','data/snakeSlime_ani.png', 'data/snakeSlime_dead.png']
}
SNAKE = {
    "maxhp":10,
    "hp":10,
    "ap":2,
    "exp":1,
    "gold":1,
    "name":"뱀",
    "png":['data/snake.png','data/snake_walk.png', 'data/snake_dead.png']
}


class DoorManager(Widget):
    doordata = {
        "1F":{
            "Enemies":{
                "Ghost":GHOST,
                "FlyFly":FLYFLY,
                "Mouse":MOUSE,
            },
        },
        "2F":{
            "Enemies":{
                "Bet":BAT,
                "Bee":BEE,
                "Fly":FLY,
            },
        },
        "3F":{
            "Enemies":{
                "Frog":FROG,
            },
        },
        "4F":{
            "Enemies":{
                "GreenSlime":SLIME_GREEN,
                "PinkSlime":SLIME_PINK,
                "BlueSlime":SLIME_BLUE,
           },
        },
        "5F":{
            "Enemies":{
                "Snail":SNAIL,
                "Snake":SNAKE,
                "SnakeLava":SNAKELAVA,
            },
        },
    }
    enemies_rdd = {}
    current_door = StringProperty("1F")
    def __init__(self):
        for key in self.doordata:
            self.enemies_rdd[key] = RandomDict(self.doordata[key]["Enemies"])

    def door_up(self):
        """ 문자열로처리"""
        num = int(self.current_door[:-1])
        if num == 5:
            return

        self.current_door = str(num+1) + "F"

    def door_down(self):
        """ 문자열로처리"""

        num = int(self.current_door[:-1])
        if num == 1:
            return

        self.current_door = str(num-1) + "F"

    def get_enermy_info(self):
        """
        이 중 랜덤으로 뽑아냄 // 합의 퍼센트로 뽑기
        """
        rd = self.enemies_rdd[self.current_door]
        return rd[rd.choice()]
