# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ObjectProperty,NumericProperty

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''

<TurnBattle>:
    player: player_line
    enermy: enermy_right
    Label:
        font_size: 70
        center_x: root.width / 4
        top: root.top - 270
        text: "HP: "+ str(root.player.hp)
    Label:
        font_size: 70
        center_x: root.width * 3 / 4
        top: root.top - 270
        text: "HP: " + str(root.enermy.hp)
    Label:
        font_size: 30
        center_x: root.width / 4
        top: root.top - 210
        text: "AP: "+ str(root.player.ap)
    Label:
        font_size: 30
        center_x: root.width * 3 / 4
        top: root.top - 210
        text: "AP: " + str(root.enermy.ap)
    Label:
        font_size: 20
        center_x: root.width / 4
        top: root.top - 180
        text: root.player.status
    Label:
        font_size: 20
        center_x: root.width * 3 / 4
        top: root.top - 180
        text: root.enermy.status
    Image:
        center_x: root.width * 3 / 4
        center_y: root.center_y + 150
        source: 'f074.png'
    Image:
        center_x: root.width / 4
        center_y: root.center_y + 150
        source: 'f074.png'
    Player:
        id: player_line
    Enermy:
        id: enermy_right
    TurnButton:
        id: button
        text: "Turn"
        center_x: root.width * 3 / 4
        top: root.top - 400
        on_press: root.battle()
    # debug for size
    # Label:
    #     font_size: 10
    #     center_x: root.width * 1 / 4
    #     top: root.top - 400
    #     text: "width:" + str(root.width) + "height:" + str(root.height) + "center_xy:" + str(root.center_x) + " " + str(root.center_y)

''')

class TurnButton(Button):
    pass

class User(object):
    hp = NumericProperty(0)
    ap = NumericProperty(0)
    status = StringProperty("alive")

    def up_score(self, number):
        self.hp += 1

    def fight(self, ap):
        self.hp -= ap

        if self.hp <= 0:
            self.hp = 0
            self.status = "dead"
            return 1
        return 0


class Enermy(User, Widget):
    exp = NumericProperty(0)
    gold = NumericProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def load(self, enemy_info):

        self.ap = enemy_info["ap"]
        self.hp = enemy_info["hp"]
        self.exp = enemy_info["exp"]
        self.gold = enemy_info["gold"]


class Player(User, Widget):
    exp = NumericProperty(0)
    gold = NumericProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def get_reward(self, enemy):
        self.exp += enemy.exp
        self.gold += enemy.gold




player_data = [20, 200]
enemy_data = {"orc":
              {"hp":200,
               "ap":10,
               "exp":10,
               "gold":100,},
}

def battle(player, enermy):
    """ battle turn """

    # check for fight
    if player.hp == 0 or enermy.hp == 0:
        return

    # take dmg each other
    if player.fight(enermy.ap):
        # if dead
        pass
    if enermy.fight(player.ap):
        # if dead
        player.get_reward(enermy)


class TurnBattle(Widget):
    player = Player()
    enermy = Enermy()

    # for animation
    def update(self, dt):
        pass

    def battle(self):
        """ dmg swap """
        battle(self.player, self.enermy)

    def load(self, enemy_name):
        self.player.ap = player_data[0]
        self.player.hp = player_data[1]
        self.enermy.load(enemy_data[enemy_name])


class TurnApp(App):
    def build(self):
        # 빌드시 아이콘 타이틀 지정
        # self.icon = 'memoIcon.png'
        self.title = 'Kivy Test'
        game = TurnBattle()
        game.load("orc")
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ in ('__main__', '__android__'):
    TurnApp().run()

