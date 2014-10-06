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
        top: root.top - 200
        text: "AP: "+ str(root.player.ap)
    Label:
        font_size: 30
        center_x: root.width * 3 / 4
        top: root.top - 200
        text: "AP: " + str(root.enermy.ap)
    Image:
        center_x: root.width * 3 / 4
        center_y: root.center_y + 150
        source: 'f074.png'
    Image:
        center_x: root.width / 4
        center_y: root.center_y + 150
        source: 'f074.png'
    User:
        id: player_line
    User:
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

class User(Widget):
    hp = NumericProperty(0)
    ap = NumericProperty(0)

    def up_score(self, number):
        self.hp += 1

    def fight(self, ap):
        self.hp -= ap


player_data = [20, 200]
enemy_data = {"orc": [10, 200],}


def battle(player, enermy):
    """ for battle a vs b """
    player.fight(enermy.ap)
    enermy.fight(player.ap)

class TurnBattle(Widget):
    player = ObjectProperty(None)
    enermy = ObjectProperty(None)

    # for animation
    def update(self, dt):
        pass

    def battle(self):
        """ dmg swap """
        battle(self.player, self.enermy)

    def load(self, enemy_name):
        self.player.ap = player_data[0]
        self.player.hp = player_data[1]
        self.enermy.ap, self.enermy.hp = enemy_data[enemy_name]


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

