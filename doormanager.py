# -*- coding: utf-8 -*-
from randomdict import RandomDict
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

GHOST = {
    "maxhp":10,
    "hp":10,
    "ap":1,
    "exp":1,
    "gold":1,
    "name":"유령",
    "png":['data/ghost_normal.png','data/ghost.png', 'data/ghost_dead.png']
}
FLYFLY = {
    "maxhp":20,
    "hp":20,
    "ap":1,
    "exp":2,
    "gold":2,
    "name":"날파리",
    "png":['data/flyFly1.png','data/flyFly2.png', 'data/flyDead.png']
}

MOUSE = {
    "maxhp":60,
    "hp":60,
    "ap":5,
    "exp":5,
    "gold":5,
    "name":"찍찍이",
    "png":['data/mouse.png','data/mouse_walk.png', 'data/mouse_dead.png']
}
BAT = {
    "maxhp":120,
    "hp":120,
    "ap":10,
    "exp":10,
    "gold":10,
    "name":"박쥐",
    "png":['data/bat.png','data/bat_fly.png', 'data/bat_dead.png']
}

BEE = {
    "maxhp":200,
    "hp":200,
    "ap":25,
    "exp":20,
    "gold":25,
    "name":"벌",
    "png":['data/bee.png','data/bee_fly.png', 'data/bee_dead.png']
}
FLY = {
    "maxhp":360,
    "hp":360,
    "ap":55,
    "exp":40,
    "gold":40,
    "name":"파리",
    "png":['data/fly.png','data/fly_fly.png', 'data/fly_dead.png']
}
FROG = {
    "maxhp":5000,
    "hp":5000,
    "ap":200,
    "exp":100,
    "gold":1000,
    "name":"(보스)개굴이",
    "png":['data/frog.png','data/frog_leap.png', 'data/frog_dead.png']
}

SLIME_GREEN = {
    "maxhp":10000,
    "hp":10000,
    "ap":10000,
    "exp":200,
    "gold":10000,
    "name":"초록 슬라임",
    "png":['data/slimeGreen.png','data/slimeGreen_walk.png', 'data/slimeGreen_dead.png']
}
SLIME_PINK = {
    "maxhp":500000,
    "hp":50000,
    "ap":50000,
    "exp":400,
    "gold":50000,
    "name":"핑크 슬라임",
    "png":['data/slime.png','data/slime_walk.png', 'data/slime_dead.png']
}
SLIME_BLUE = {
    "maxhp":10000000,
    "hp":10000000,
    "ap":100000,
    "exp":600,
    "gold":100000,
    "name":"블루 슬라임",
    "png":['data/slimeBlue.png','data/slimeBlue_blue.png', 'data/slimeBlue_dead.png']
}

SNAIL = {
    "maxhp":100000000,
    "hp":100000000,
    "ap":100000,
    "exp":1000,
    "gold":100000,
    "name":"달팽이 병정",
    "png":['data/snail.png','data/snail_walk.png', 'data/snail_shell.png']
}

SNAKELAVA = {
    "maxhp":100000000000,
    "hp":100000000000,
    "ap":2,
    "exp":2000,
    "gold":1,
    "name":"당근 벌레",
    "png":['data/snakeLava.png','data/snakeLava_ani.png', 'data/snakeLava_dead.png']
}
SNAKESLIME = {
    "maxhp":10000000000000,
    "hp":10000000000000,
    "ap":20000000,
    "exp":4000,
    "gold":20000000,
    "name":"초록 벌레",
    "png":['data/snakeSlime.png','data/snakeSlime_ani.png', 'data/snakeSlime_dead.png']
}

SNAKE = {
    "maxhp":9999999999999999,
    "hp":999999999,
    "ap":999999999,
    "exp":9999999999,
    "gold":9999999999,
    "name":"(보스)뱀",
    "png":['data/snake.png','data/snake_walk.png', 'data/snake_dead.png']
}


class DoorManager(Widget):
    doordata = {
        "1F":{
            "Enemies":{
                "Ghost":GHOST,
                "FlyFly":FLYFLY,
            },
        },
        "2F":{
            "Enemies":{
                "Mouse":MOUSE,
                "Bet":BAT,
            },
        },
        "3F":{
            "Enemies":{
                "Bee":BEE,
                "Fly":FLY,
            },
        },
        "4F":{
            "Enemies":{
                "Frog":FROG,
           },
        },
        "5F":{
            "Enemies":{
                "GreenSlime":SLIME_GREEN,
                "PinkSlime":SLIME_PINK,
                "BlueSlime":SLIME_BLUE,
            },
        },
        "6F":{
            "Enemies":{
                "Snail":SNAIL,
                "SnakeLava":SNAKELAVA,
            },
        },
        "7F":{
            "Enemies":{
                "Snake":SNAKE,
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
        if num == 7:
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
