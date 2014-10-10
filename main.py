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
from kivy.core.audio import SoundLoader
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
        MainLayout:
            id: main_screen
            # size: self.get_size(self.parent)
            # size: [min(self.parent.width, self.parent.height)] * 2
            # on_size: self.reposition()
            # on_pos: self.reposition()

            EnermyScreen:
                id: battle_screen
                size_hint: None, None
                size: [min(main_screen.width, main_screen.height)] * 2
                on_size: battle_screen.reposition()
                on_pos: battle_screen.reposition()
                Label:
                    font_size: 20
                    center_y: battle_screen.center_y - battle_screen.height * 5 / 16
                    center_x: battle_screen.center_x
                    text: root.enermy.status
                    font_name: 'data/kenpixel.ttf'
                EnermyImage:
                    center_x: battle_screen.center_x
                    center_y: battle_screen.center_y
                    source: self.get_enemy_image(root.status, root.enermy, turnbutton.state)
                Label:
                    font_size: 20
                    text: 'Monster Name'
                    color: 0xee / 255., 0xe4 / 255., 0xda / 255., 1.
                    bold: True
                    center_y: battle_screen.center_y + battle_screen.height * 3 / 16
                    center_x: battle_screen.center_x
                    font_name: 'data/kenpixel.ttf'

                # 가능 하면 이미지 편집을 할껄..
                Image:
                    center_y: battle_screen.center_y - battle_screen.height * 3 / 16
                    center_x: battle_screen.center_x - 36
                    source: 'data/hud_heartEmpty.png' if root.enermy.hp < 1 else 'data/hud_heartHalf.png' if root.enermy.hp <  root.enermy.maxhp/6 else 'data/hud_heartFull.png'
                    size: 40, 40
                Image:
                    center_y: battle_screen.center_y - battle_screen.height * 3 / 16
                    center_x: battle_screen.center_x
                    source: 'data/hud_heartEmpty.png' if root.enermy.hp <  root.enermy.maxhp * 3/6 else 'data/hud_heartHalf.png' if root.enermy.hp <  root.enermy.maxhp* 4/6 else 'data/hud_heartFull.png'
                    size: 40, 40
                Image:
                    center_y: battle_screen.center_y - battle_screen.height * 3 / 16
                    center_x: battle_screen.center_x + 36
                    source: 'data/hud_heartEmpty.png' if root.enermy.hp <  root.enermy.maxhp * 5/6 else 'data/hud_heartHalf.png' if root.enermy.hp <  root.enermy.maxhp* 6/6 else 'data/hud_heartFull.png'
                    size: 40, 40
                Label:
                    font_size: 20
                    center_y: battle_screen.center_y - battle_screen.height * 4 / 16
                    center_x: battle_screen.center_x
                    text: "AP: " + str(root.enermy.ap)
                    font_name: 'data/kenpixel.ttf'

        # 박스 2
        BoxLayout:
            orientation: 'vertical' if root.height > root.width else 'horizontal'
            BoxLayout:
                orientation: 'vertical'
                spacing: '10dp'

                # 박스 2 - 정보표시 1
                BoxLayout:
                    padding: '10dp'
                    spacing: '10dp'
                    id: user_screen
                    orientation: 'vertical' if root.height > root.width else 'horizontal'
                    canvas.before:
                        Color:
                            rgb: 0x33 / 255., 0xad / 255., 0xa0 / 255.
                        BorderImage:
                            pos: self.pos
                            size: self.size
                    # 박스 2 - 정보표시 1 - 유저 얼굴 1
                    BoxLayout:
                        id: user_screen
                        padding: '10dp'
                        spacing: '10dp'

                        orientation: 'vertical'  # if root.height > root.width else 'horizontal'
                        canvas.before:
                            Color:
                                rgb: 0xaa / 255., 0xcc / 255., 0xa0 / 255.
                            BorderImage:
                                pos: self.pos
                                size: self.size

                        # 박스 2 - 정보표시 1 - 유저 정보 2
                        UserScreen:
                            id: battle_screen2
                            # size_hint: None, None
                            size: [min(user_screen.width, user_screen.height)] * 2
                            on_size: battle_screen2.reposition()
                            on_pos: battle_screen2.reposition()
                            Image:
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                                #  atlas test
                                # source: 'atlas://data/myatlas/dungeontile'
                                source: 'data/Gall_5.png' if turnbutton.state == "down" else 'data/Gall_1.png'
                                # allow_stretch: True
                                # width: 100
                                # height: 100
                        # Player Status
                        BoxLayout:
                            id: player_status
                            orientation: 'horizontal' if root.height > root.width else 'vertical'
                            # canvas.before:
                            #     Color:
                            #         rgb: 0xbb / 255., 0xdd / 255., 0xa0 / 255.
                            #     BorderImage:
                            #         pos: self.pos
                            #         size: self.size
                            Label:
                                font_size: 20
                                pos: self.pos
                                text: root.player.status
                                font_name: 'data/kenpixel.ttf'

                            # 가능 하면 이미지 편집을 할껄..
                            HeartScreen:
                                # orientation: 'horizontal'
                                # size_hint: 1, 1
                                # center_y: self.parent.center_y
                                # center_x: self.parent.center_x
                                Image:
                                    center_y: self.parent.center_y
                                    center_x: self.parent.center_x - 36
                                    source: 'data/hud_heartEmpty.png' if root.player.hp < 1 else 'data/hud_heartHalf.png' if root.player.hp <  root.player.maxhp/6 else 'data/hud_heartFull.png'
                                    size: 40, 40
                                Image:
                                    center_y: self.parent.center_y
                                    center_x: self.parent.center_x
                                    source: 'data/hud_heartEmpty.png' if root.player.hp <  root.player.maxhp * 3/6 else 'data/hud_heartHalf.png' if root.player.hp <  root.player.maxhp* 4/6 else 'data/hud_heartFull.png'
                                    size: 40, 40
                                Image:
                                    center_y: self.parent.center_y
                                    center_x: self.parent.center_x + 36
                                    source: 'data/hud_heartEmpty.png' if root.player.hp <  root.player.maxhp * 5/6 else 'data/hud_heartHalf.png' if root.player.hp <  root.player.maxhp* 6/6 else 'data/hud_heartFull.png'
                                    size: 40, 40
                            Label:
                                font_size: 20
                                pos: self.pos
                                # center_y: player_status.center_y
                                # center_x: player_status.center_x
                                text: "LV: "+ str(root.player.lv)
                                font_name: 'data/kenpixel.ttf'
                            Label:
                                font_size: 20
                                pos: self.pos
                                text: "AP: "+ str(root.player.ap)
                                font_name: 'data/kenpixel.ttf'
                            Label:
                                font_size: 20
                                pos: self.pos
                                text: "exp: " + str(root.player.exp)
                                font_name: 'data/kenpixel.ttf'
                            Label:
                                font_size: 20
                                pos: self.pos
                                text: "gold: " + str(root.player.gold)
                                font_name: 'data/kenpixel.ttf'

                    # 박스 2 - 정보표시 2
                    BoxLayout:
                        padding: '10dp'
                        spacing: '10dp'
                        orientation: 'horizontal'
                        canvas.before:
                            Color:
                                rgb: 0xdd / 255., 0xad / 255., 0xa0 / 255.
                            BorderImage:
                                pos: self.pos
                                size: self.size
                        # UI
                        TurnButton:
                            # text: "Turn"
                            id: turnbutton
                            center_x: root.width * 3 / 4
                            top: root.top - 400
                            on_press: root.on_main_button(self, main_screen)
                            background_color: (0, 0, 0, 0)
                            Image:
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                                source: root.get_main_button_image(turnbutton.state)
                            Label:
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y - self.parent.height * 1/8
                                text: self.parent.name
                                bold: True
                                font_size: 30
                                font_name: 'data/kenpixel.ttf'
                            # background_normal: 'data/Gall_1.png'
                            # background_down: 'data/Gall_5.png'

    # # Healing Spinner
    # Spinner:
    #     text: "auto heal"
    #     values: ['10%','20%','30%']
    #     center_x: root.width / 4
    #     top: root.top - 400
    #     size: [100, 50]
''')

from kivy.graphics import Color, BorderImage
from kivy.uix.anchorlayout import AnchorLayout


class Repositon(object):
    def rebuild_background(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0xbb / 255., 0xad / 255., 0xa0 / 255.)
            BorderImage(pos=self.pos, size=self.size)
            Color(0xcc / 255., 0xc0 / 255., 0xb3 / 255.)

    def reposition(self, *args):
        self.rebuild_background()

    def repostion_with_size(self, screen):
        self.rebuild_background()
        self.size = [min(screen.width, screen.height)] * 2

# Main Screen
class EnermyScreen(Widget, Repositon):
    pass

class HeartScreen(Widget, Repositon):
    pass

GAME_STATUS_SEARCH = 0
GAME_STATUS_BATTLE = 1
GAME_STATUS_TURN = 2
GAME_STATUS_REWARD = 3


# EnermyImage
class EnermyImage(Image):
    def get_enemy_image(self, status, enermy, state):
        if status == GAME_STATUS_SEARCH:
            return 'data/rpgTile220.png'  if state=="down" else 'data/rpgTile205.png'
        elif status == GAME_STATUS_REWARD:
            return 'data/coinGold.png'
        elif enermy.name == "orc":
            return  'data/spider_dead.png' if enermy.status == "DEAD" else 'data/spider_walk1.png' if state=="down" else 'data/spider.png'

# EnermyHpImage
# class EnermyHpImage(Image):
#     def get_enemy_hp(self, hp):
#         return 

        # if status == GAME_STATUS_SEARCH:
        #     return 'data/rpgTile220.png'  if state=="down" else 'data/rpgTile205.png'
        # elif status == GAME_STATUS_REWARD:
        #     return 'data/coinGold.png'
        # elif enermy.name == "orc":
        #     return  'data/spider_dead.png' if enermy.status == "DEAD" else 'data/spider_walk1.png' if state=="down" else 'data/spider.png'
# User Screen
class UserScreen(Widget, Repositon):
    score = NumericProperty(0)

# Turn Button
class TurnButton(Button):
    name = StringProperty("START")


class MainLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__()


STATUS_ALIVE = "ALIVE"
STATUS_DEAD = "DEAD"


class User(object):
    hp = NumericProperty(0)
    maxhp = NumericProperty(0)
    ap = NumericProperty(0)
    status = StringProperty(STATUS_ALIVE)
    lv = NumericProperty(0)

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
    name = StringProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def load(self, enemy_info):
        self.ap = enemy_info["ap"]
        self.hp = enemy_info["hp"]
        self.exp = enemy_info["exp"]
        self.gold = enemy_info["gold"]
        self.status = STATUS_ALIVE
        self.name = enemy_info["name"]
        self.maxhp = enemy_info["maxhp"]

class Player(User, Widget):
    exp = NumericProperty(0)
    gold = NumericProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def get_reward(self, enemy):
        self.exp += enemy.exp
        self.gold += enemy.gold


player_data = [1, 1, 100, 100]
enemy_data = {"orc":{
    "maxhp":20,
    "hp":20,
    "ap":1,
    "exp":1,
    "gold":1,
    "name":"orc"},
}


def status_name(status):
    if status == GAME_STATUS_SEARCH:
        return "SEARCH"
    if status == GAME_STATUS_BATTLE:
        return "BATTLE"
    if status == GAME_STATUS_TURN:
        return "TURN"
    if status == GAME_STATUS_REWARD:
        return "REWARD"

# 컨트롤 부분을 밖으로 빼기 위함
from kivy.app import App
app = None

class TurnBattle(Widget):
    player = Player()
    enermy = Enermy()
    status = GAME_STATUS_SEARCH

    # for animation
    def update(self, dt):
        pass

    def init(self):
        self.player.lv = player_data[0]
        self.player.ap = player_data[1]
        self.player.hp = player_data[2]
        self.player.maxhp = player_data[3]

    def load(self, enemy_name):
        self.enermy.load(enemy_data[enemy_name])

    def _status_change(self, status):
        self.status = status

    def get_main_button_image(self, state):
        if self.status == GAME_STATUS_SEARCH:
            return 'data/shadedDark26.png' if state == "down" else 'data/shadedLight26.png'
        elif self.status == GAME_STATUS_BATTLE:
            return 'data/shadedDark48.png' if state == "down" else 'data/shadedLight48.png'
        elif self.status == GAME_STATUS_TURN:
            return 'data/shadedDark49.png' if state == "down" else 'data/shadedLight49.png'
        elif self.status == GAME_STATUS_REWARD:
            return 'data/shadedDark28.png' if state == "down" else 'data/shadedLight28.png'
        else:
            raise



    def on_main_button(self, button, main_screen):
        """ on_main_button turn """

        # Turn
        if self.status == GAME_STATUS_SEARCH:
            self.load("orc")
            self._status_change(GAME_STATUS_BATTLE)
        elif self.status == GAME_STATUS_BATTLE:
            self._status_change(GAME_STATUS_TURN)
        elif self.status == GAME_STATUS_TURN:
            # print dir(app.sound['swing'])
            app.sound['swing'].play()
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
            app.sound['coin'].play()
            self.player.get_reward(self.enermy)
            self._status_change(GAME_STATUS_SEARCH)
        else:
            raise

        # Text button name change
        button.name = status_name(self.status)

class TurnApp(App):
    sound = {}
    music = None

    def build(self):
        global app
        app = self

        # 빌드시 아이콘 타이틀 지정
        # self.icon = 'memoIcon.png'

        # start the background music:
        self.music = SoundLoader.load('sound/8bitattempt.ogg')
        self.music.bind(on_stop=self.sound_replay)
        self.music.play()

        # sound
        self.sound['swing'] = SoundLoader.load('sound/battle/swing.ogg')
        self.sound['coin'] = SoundLoader.load('sound/inventory/chainmail1.ogg')


        self.title = 'One RPG'
        game = TurnBattle()
        game.init()
        game.load("orc")
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

    def sound_replay(self, instance):
        if self.music.status != 'play':
            self.music.play()

if __name__ in ('__main__', '__android__'):
    TurnApp().run()
