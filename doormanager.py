# -*- coding: utf-8 -*-
from randomdict import RandomDict
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class DoorManager(Widget):
    doordata = {
        "1F":{
            "Enemies":{
                "Ghost":{
                    "maxhp":20,
                    "hp":20,
                    "ap":1,
                    "exp":1,
                    "gold":1,
                    "name":"Ghost",
                    "png":['data/ghost_normal.png','data/ghost.png', 'data/ghost_dead.png']},
                "Fly":{
                    "maxhp":15,
                    "hp":15,
                    "ap":1,
                    "exp":1,
                    "gold":1,
                    "name":"Fly",
                    "png":['data/flyFly1.png','data/flyFly2.png', 'data/flyDead.png']},
                "Mouse":{
                    "maxhp":10,
                    "hp":10,
                    "ap":2,
                    "exp":1,
                    "gold":1,
                    "name":"Mouse",
                    "png":['data/mouse.png','data/mouse_walk.png', 'data/mouse_dead.png']},
            },
        },
        "2F":{
            "Enemies":{
                "Ghost":{
                    "maxhp":40,
                    "hp":40,
                    "ap":2,
                    "exp":2,
                    "gold":2,
                    "name":"Ghost",
                    "png":['data/ghost_normal.png','data/ghost.png', 'data/ghost_dead.png']},
                "Fly":{
                    "maxhp":30,
                    "hp":30,
                    "ap":2,
                    "exp":2,
                    "gold":2,
                    "name":"Fly",
                    "png":['data/flyFly1.png','data/flyFly2.png', 'data/flyDead.png']},
                "Mouse":{
                    "maxhp":20,
                    "hp":20,
                    "ap":4,
                    "exp":2,
                    "gold":2,
                    "name":"Mouse",
                    "png":['data/mouse.png','data/mouse_walk.png', 'data/mouse_dead.png']},
            },
        },
        "3F":{
            "Enemies":{
                "Ghost":{
                    "maxhp":100,
                    "hp":100,
                    "ap":5,
                    "exp":5,
                    "gold":5,
                    "name":"Ghost",
                    "png":['data/ghost_normal.png','data/ghost.png', 'data/ghost_dead.png']},
                "Fly":{
                    "maxhp":200,
                    "hp":200,
                    "ap":10,
                    "exp":10,
                    "gold":10,
                    "name":"Fly",
                    "png":['data/flyFly1.png','data/flyFly2.png', 'data/flyDead.png']},
                "Mouse":{
                    "maxhp":300,
                    "hp":300,
                    "ap":30,
                    "exp":30,
                    "gold":30,
                    "name":"Mouse",
                    "png":['data/mouse.png','data/mouse_walk.png', 'data/mouse_dead.png']},
            },
        },
        "4F":{
            "Enemies":{
                "Ghost":{
                    "maxhp":1000,
                    "hp":1000,
                    "ap":100,
                    "exp":100,
                    "gold":500,
                    "name":"Ghost",
                    "png":['data/ghost_normal.png','data/ghost.png', 'data/ghost_dead.png']},
           },
        },
        "5F":{
            "Enemies":{
                "Mouse":{
                    "maxhp":100000000,
                    "hp":100000,
                    "ap":100000,
                    "exp":100000,
                    "gold":100000,
                    "name":"Mouse",
                    "png":['data/mouse.png','data/mouse_walk.png', 'data/mouse_dead.png']},
            },
        },
    }
    enemies_rdd = {}
    current_door = StringProperty("1F")
    def __init__(self):
        for key in self.doordata:
            self.enemies_rdd[key] = RandomDict(self.doordata[key]["Enemies"])

    # def change_door(self, name):
    #     self.rdd[kley

    def get_enermy_info(self):
        """
        이 중 랜덤으로 뽑아냄 // 합의 퍼센트로 뽑기
        """
        rd = self.enemies_rdd[self.current_door]
        return rd[rd.choice()]
