# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.animation import Animation

from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ObjectProperty,NumericProperty

from kivy.uix.spinner import Spinner



#!/usr/bin/kivy
__version__ = '1.0'

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''

<TurnBattle>:
    # 전체 공간
    BoxLayout:
        pos: root.pos
        size: root.size
        padding: '10dp'
        spacing: '10dp'
        orientation: 'vertical' if self.height > self.width else 'horizontal'
        canvas:
            Color:
                rgb: 0xfa / 255., 0xf8 / 255., 0xef / 255.
            # BackGroundColor
            Rectangle:
                pos: self.pos
                size: self.size
        # 앵커 1 - 메인 전투화면
        AnchorLayout:
            id: anchor
            BattleScreen:
                id: game
                size_hint: None, None
                size: [min(anchor.width, anchor.height)] * 2
                on_size: self.reposition()
                on_pos: self.reposition()
            Label:
                text: 'Main'
                color: 0xee / 255., 0xe4 / 255., 0xda / 255., 1.
                bold: True

        # 박스 2
        BoxLayout:
            orientation: 'vertical' if root.height > root.width else 'horizontal'
            size_hint_y: .25 if root.height > root.width else 1
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'

                # 박스 2 - 정보표시 1
                BoxLayout:
                    orientation: 'vertical' if root.height > root.width else 'horizontal'
                    canvas.before:
                        Color:
                            rgb: 0xbb / 255., 0xad / 255., 0xa0 / 255.
                        BorderImage:
                            pos: self.pos
                            size: self.size
                            source: 'data/round.png'
                    Label:
                        text: 'Status'
                        color: 0xee / 255., 0xe4 / 255., 0xda / 255., 1.
                        bold: True

                # 박스 2 - 정보표시 2
                BoxLayout:
                    orientation: 'vertical'
                    canvas.before:
                        Color:
                            rgb: 0xbb / 255., 0xad / 255., 0xa0 / 255.
                        BorderImage:
                            pos: self.pos
                            size: self.size
                            source: 'data/round.png'

                    Label:
                        text: 'Status2'
                        color: 0xee / 255., 0xe4 / 255., 0xda / 255., 1.
                        bold: True
# <BattleScreen>:
    # BoxLayout:
    #     orientation: 'vertical'
    #     canvas.before:
    #         Color:
    #             rgb: 0xbb / 255., 0xad / 255., 0xa0 / 255.
    #         BorderImage:
    #             pos: self.pos
    #             size: self.size
    #             source: 'data/round.png'
    # Label:
    #     text: 'HP'
    #     color: 0xee / 255., 0xe4 / 255., 0xda / 255., 1.
    #     font_size: self.height / 1.5
    #     size_hint_y: .5
    #     bold: True
    # Label:
    #     text: str("BattleScreen")
    #     font_size: self.height / 1.5
    #     bold: True

# Game2048:
# id: game
# on_size: self.reposition()
# on_pos: self.reposition()

    # player: player_line
    # enermy: enermy_right


        # Player
        # Player:
        #     id: player_line
        # Label:
        #     font_size: 70
        #     center_x: self.width / 4
        #     top: root.top - 270
        #     text: "HP: "+ str(root.player.hp)
        # Label:
        #     font_size: 30
        #     center_x: root.width / 4
        #     top: root.top - 210
        #     text: "AP: "+ str(root.player.ap)
        # Label:
        #     font_size: 20
        #     center_x: root.width / 4
        #     top: root.top - 180
        #     text: root.player.status
        # Label:
        #     font_size: 20
        #     center_x: root.width * 3 / 16
        #     top: root.top - 330
        #     text: "exp: " + str(root.player.exp)
        # Label:
        #     font_size: 20
        #     center_x: root.width * 5 / 16
        #     top: root.top - 330
        #     text: "gold: " + str(root.player.gold)
        # Image:
        #     center_x: root.width / 4
        #     top: root.top - 100
        #     source: 'f074.png'


    # # Enermy
    # Enermy:
    #     id: enermy_right
    # Label:
    #     font_size: 70
    #     center_x: root.width * 3 / 4
    #     top: root.top - 270
    #     text: "HP: " + str(root.enermy.hp)
    # Label:
    #     font_size: 30
    #     center_x: root.width * 3 / 4
    #     top: root.top - 210
    #     text: "AP: " + str(root.enermy.ap)
    # Label:
    #     font_size: 20
    #     center_x: root.width * 3 / 4
    #     top: root.top - 180
    #     text: root.enermy.status
    # Image:
    #     center_x: root.width * 3 / 4
    #     top: root.top - 100
    #     source: 'data/Ghost_Light_2.png'

    # # Healing Spinner
    # Spinner:
    #     text: "auto heal"
    #     values: ['10%','20%','30%']
    #     center_x: root.width / 4
    #     top: root.top - 400
    #     size: [100, 50]


    # # UI
    # TurnButton:
    #     id: button
    #     text: "Turn"
    #     center_x: root.width * 3 / 4
    #     top: root.top - 400
    #     on_press: root.on_main_button(self)

    # NextButton:
    #     id: button
    #     text: "Next"
    #     center_x: root.width * 1 / 4
    #     top: root.top - 400
    #     on_press: root.load("orc")

    # debug for size
    # Label:
    #     font_size: 10
    #     center_x: root.width * 1 / 4
    #     top: root.top - 400
    #     text: "dir:" + str(dir(root))
''')

from kivy.graphics import Color, BorderImage


class BattleScreen(Widget):

    cube_size = NumericProperty(10)
    cube_padding = NumericProperty(10)
    score = NumericProperty(0)

    def rebuild_background(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0xbb / 255., 0xad / 255., 0xa0 / 255.)
            BorderImage(pos=self.pos, size=self.size, source='data/round.png')
            Color(0xcc / 255., 0xc0 / 255., 0xb3 / 255.)
            csize = self.cube_size, self.cube_size
            # for ix, iy in self.iterate_pos():
            #     BorderImage(pos=self.index_to_pos(ix, iy), size=csize,
            #     source='data/round.png')


    def reposition(self, *args):
        self.rebuild_background()
        # calculate the size of a number
        l = min(self.width, self.height)
        padding = (l / 4.) / 8.
        cube_size = (l - (padding * 5)) / 4.
        self.cube_size = cube_size
        self.cube_padding = padding

        # for ix, iy, number in self.iterate():
        #     number.size = cube_size, cube_size
        #     number.pos = self.index_to_pos(ix, iy)




STATUS_ALIVE = "ALIVE"
STATUS_DEAD = "DEAD"

class TurnButton(Button):
    pass

class User(object):
    hp = NumericProperty(0)
    ap = NumericProperty(0)
    status = StringProperty(STATUS_ALIVE)

    def up_score(self, number):
        self.hp += 1

    def fight(self, ap):
        self.hp -= ap

        if self.hp <= 0:
            self.hp = 0
            self.status = STATUS_DEAD
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
        self.status = STATUS_ALIVE


class Player(User, Widget):
    exp = NumericProperty(0)
    gold = NumericProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def get_reward(self, enemy):
        self.exp += enemy.exp
        self.gold += enemy.gold


player_data = [20, 2000]
enemy_data = {"orc":
              {"hp":200,
               "ap":10,
               "exp":10,
               "gold":100,},
}

GAME_STATUS_SEARCH = 0
GAME_STATUS_BATTLE = 1
GAME_STATUS_TURN = 2
GAME_STATUS_REWARD = 3

def status_name(status):
    if status == GAME_STATUS_SEARCH:
        return "SEARCH"
    if status == GAME_STATUS_BATTLE:
        return "BATTLE"
    if status == GAME_STATUS_TURN:
        return "TURN"
    if status == GAME_STATUS_REWARD:
        return "REWARD"


class TurnBattle(Widget):
    player = Player()
    enermy = Enermy()
    status = GAME_STATUS_SEARCH

    # for animation
    def update(self, dt):
        pass

    def init(self):
        self.player.ap = player_data[0]
        self.player.hp = player_data[1]

    def load(self, enemy_name):
        self.enermy.load(enemy_data[enemy_name])

    def _status_change(self, status):
        self.status = status

    def on_main_button(self, button):
        """ on_main_button turn """
        # button animation (but not good)
        # print self.player.hp
        # ratio = self.player.hp / 10
        # animation = Animation(size=(100 + 2 * ratio, 100 + 2 * ratio),
        #                       center_x = self.width * 3 / 4,
        #                       t='out_bounce')
        # animation.start(button)


        # Turn
        if self.status == GAME_STATUS_SEARCH:
            self.load("orc")
            self._status_change(GAME_STATUS_BATTLE)
        elif self.status == GAME_STATUS_BATTLE:
            self._status_change(GAME_STATUS_TURN)
        elif self.status == GAME_STATUS_TURN:
            # check for fight
            if self.player.hp == 0 or self.enermy.hp == 0:
                return
            # take dmg each other
            if self.player.fight(self.enermy.ap):
                # if dead
                pass
            if self.enermy.fight(self.player.ap):
                # if dead
                self._status_change(GAME_STATUS_REWARD)
        elif self.status == GAME_STATUS_REWARD:
            self.player.get_reward(self.enermy)
            self._status_change(GAME_STATUS_SEARCH)
        else:
            raise

        # Text button name change
        button.text = status_name(self.status)

# 컨트롤 부분을 밖으로 빼기 위함
from kivy.app import App
app = None

class TurnApp(App):
    def build(self):
        global app
        app = self

        # 빌드시 아이콘 타이틀 지정
        # self.icon = 'memoIcon.png'
        self.title = 'Kivy Test'
        game = TurnBattle()
        game.init()
        game.load("orc")
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ in ('__main__', '__android__'):
    TurnApp().run()

