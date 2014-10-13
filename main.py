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
from kivy.properties import StringProperty, ObjectProperty,NumericProperty, ListProperty
from kivy.core.audio import SoundLoader
from kivy.uix.spinner import Spinner

from doormanager import DoorManager

#!/usr/bin/kivy
__version__ = '1.0'

# 여기에 kivy파일을 추가함 - 그림파일 불러오기용
Builder.load_string('''

<BackGroundScreen>:
    center_x: self.parent.center_x
    center_y: self.parent.center_y
    Image:
        center_x: self.parent.center_x - 32
        center_y: self.parent.center_y - 38
        source: 'data/slice03_03.png'
        # opacity: 0.5
    Image:
        center_x: self.parent.center_x + 32
        center_y: self.parent.center_y - 38
        source: 'data/slice03_03.png'
        # opacity: 0.5
    Image:
        center_x: self.parent.center_x - 96
        center_y: self.parent.center_y - 38
        source: 'data/slice14_14.png'
        # opacity: 0.5
    Image:
        center_x: self.parent.center_x + 96
        center_y: self.parent.center_y - 38
        source: 'data/slice15_15.png'
        # opacity: 0.5
    Image:
        center_x: self.parent.center_x + 40
        center_y: self.parent.center_y + 55 + 31
        source: 'data/doorOpenTop.png'
    # opacity: 0.5
    Image:
        center_x: self.parent.center_x + 40
        center_y: self.parent.center_y + 31
        source: 'data/doorOpen.png'
        # opacity: 0.5


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

        # 메인 전투화면
        MainLayout:
            id: main_screen
            DoorScreen:
                backgroundscreen:backgroundscreen
                size_hint: None, None
                size: [min(main_screen.width, main_screen.height)] * 2
                on_size: self.reposition()
                on_pos: self.reposition()
                # background Image
                BackGroundScreen:
                    id:backgroundscreen

                # Floor
                Label:
                    font_size: 30
                    text: str(root.door.current_door)
                    bold: True
                    # top: self.parent.top
                    top: self.parent.top
                    center_x: self.parent.center_x
                    bold: True
                    font_name: 'data/kenpixel.ttf'
                    color: (0, 0, 0, 1)
                Label:
                    font_size: 30
                    text: str(root.enermy.name) if root.enermy.game_status != "DEAD" else ""
                    bold: True
                    center_y: self.parent.center_y + self.parent.height * 5 / 16
                    center_x: self.parent.center_x
                    font_name: 'data/kenpixel.ttf'
                    color: (0, 0, 0, 1)

                # Enermy
                EnermyImage:
                    id: enermy_screen
                    center_x: self.parent.center_x
                    center_y: self.parent.center_y + 35
                    source: self.get_enermy_image(root.game_status, root.enermy, turnbutton.state, root.door)

                # Enermy Heart Image
                Image:
                    center_y: self.parent.center_y - self.parent.height * 3 / 16
                    center_x: self.parent.center_x - 36
                    source: 'data/hud_heartEmpty.png' if root.enermy.hp < 1 else 'data/hud_heartHalf.png' if root.enermy.hp <  root.enermy.maxhp/6 else 'data/hud_heartFull.png'
                    size: 40, 40
                Image:
                    center_y: self.parent.center_y - self.parent.height * 3 / 16
                    center_x: self.parent.center_x
                    source: 'data/hud_heartEmpty.png' if root.enermy.hp <  root.enermy.maxhp * 3/6 else 'data/hud_heartHalf.png' if root.enermy.hp <  root.enermy.maxhp* 4/6 else 'data/hud_heartFull.png'
                    size: 40, 40
                Image:
                    center_y: self.parent.center_y - self.parent.height * 3 / 16
                    center_x: self.parent.center_x + 36
                    source: 'data/hud_heartEmpty.png' if root.enermy.hp <  root.enermy.maxhp * 5/6 else 'data/hud_heartHalf.png' if root.enermy.hp <  root.enermy.maxhp* 6/6 else 'data/hud_heartFull.png'
                    size: 40, 40

                Image:
                    id: reward
                    opacity: 0
                #     center_x: self.parent.center_x
                #     center_y: self.parent.center_y
                #     source: 'data/coinGold.png'

                Image:
                    center_x: self.parent.center_x - 70
                    center_y: self.parent.center_y + 20
                    source: 'data/Gall_5.png' if turnbutton.state == "down" else 'data/Gall_1.png'


                # Damage
                Label:
                    id: dmg
                    font_size: 15
                    center_y: self.parent.center_y - self.parent.height
                    center_x: self.parent.center_x
                    text: "-" + str(root.player.ap)
                    font_name: 'data/kenpixel.ttf'
                    color: (1, 0, 0, 1)
                    bold: True


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
                            # Image:
                            #     center_x: self.parent.center_x - 64
                            #     center_y: self.parent.center_y
                            #     source: 'data/rpgTile056.png'
                            # Image:
                            #     center_x: self.parent.center_x - 64
                            #     center_y: self.parent.center_y
                            #     source: 'data/rpgTile056.png'
                            # Image:
                            #     center_x: self.parent.center_x - 32
                            #     center_y: self.parent.center_y
                            #     source: 'data/rpgTile075.png'
                            # Image:
                            #     center_x: self.parent.center_x + 32
                            #     center_y: self.parent.center_y
                            #     source: 'data/rpgTile077.png'

                        # Player Status
                        BoxLayout:
                            id: player_status
                            orientation: 'horizontal' if root.height > root.width else 'vertical'
                            Label:
                                font_size: 20
                                pos: self.pos
                                text: root.player.game_status if root.player.game_status != 'DEAD' else "game over!"
                                font_name: 'data/kenpixel.ttf'

                            # 가능 하면 이미지 편집을 할껄..
                            HeartScreen:
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
                            on_press: root.on_main_button(self, main_screen, enermy_screen, dmg, reward, floor_spinner.text)
                            background_color: (0, 0, 0, 0)
                            Image:
                                center_x: self.parent.center_x
                                center_y: self.parent.center_y
                                source: root.get_main_button_image(self.parent.state)
                            Label:
                                center_x: self.parent.center_x
                                center_y:  self.parent.center_y - self.parent.height * 3/8 if root.height > root.width else self.parent.center_y - self.parent.height * 1/8
                                text: self.parent.name
                                bold: True
                                font_size: 30
                                font_name: 'data/kenpixel.ttf'

    # Healing Spinner
    Spinner:
        id: floor_spinner
        text: '1F'
        values: ['1F','2F','3F','4F','5F']
        # center_x: root.width / 4
        # top: root.top - 400
        size: [100, 50]

''')

from kivy.graphics import Color, BorderImage
from kivy.uix.anchorlayout import AnchorLayout

class Repositon(object):
    def rebuild_background(self):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0xd0 / 255., 0xf4 / 255., 0xf7 / 255.)
            BorderImage(pos=self.pos, size=self.size)
            Color(0xcc / 255., 0xc0 / 255., 0xb3 / 255.)

    def reposition(self, *args):
        self.rebuild_background()

    def repostion_with_size(self, screen):
        self.rebuild_background()
        self.size = [min(screen.width, screen.height)] * 2

class DoorScreen(Widget, Repositon):
    backgroundscreen = ObjectProperty(None)
    tpos = [0, 0]

    def on_touch_down(self, touch):
        super(DoorScreen, self).on_touch_down(touch)
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.tpos = touch.pos

    def on_touch_move(self, touch):
        if touch.grab_current is not self:
            return
        if self.collide_point(*touch.pos):
            x, y  = self.tpos
            diff_x = touch.x - x
            diff_y = touch.y - y
            print diff_x, diff_y
            print self.backgroundscreen.x, self.backgroundscreen.y
            space = 20
            if self.backgroundscreen:
                if (diff_x  > space):
                    self.backgroundscreen.center_x = touch.x
                elif (diff_x < -space):
                    self.backgroundscreen.center_x = touch.x
                elif (diff_y > space):
                    self.backgroundscreen.y = touch.y
                elif (diff_y < -space):
                    self.backgroundscreen.y = touch.y

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.backgroundscreen.center_x = self.center_x
            self.backgroundscreen.center_y = self.center_y
            touch.ungrab(self)


class BackGroundScreen(Widget):
    pass



class HeartScreen(Widget, Repositon):
    pass

GAME_STATUS_OPEN = 0
GAME_STATUS_BATTLE = 1
GAME_STATUS_TURN = 2
GAME_STATUS_REWARD = 3

# DoorImage
class DoorImage(Image):
    def get_door_image(self, game_status, state, door):
        if game_status == GAME_STATUS_OPEN:
            return 'data/rpgTile228.png' if state=="down" else 'data/rpgTile194.png'
        return 'data/rpgTile228.png'

# EnermyImage
class EnermyImage(Image):
    def get_enermy_image(self, game_status, enermy, state, door):
        """
        문을 선택하고 거기서 몬스터가 나오는 거 까지 관리 할 수 있을까?
        """
        if game_status == GAME_STATUS_OPEN:
            return "data/tapTick.png"
        elif game_status == GAME_STATUS_REWARD:
            return enermy.png[2]
        elif state == "down":
            return enermy.png[0]
        else:
            return enermy.png[1]

# User Screen
class UserScreen(Widget, Repositon):
    score = NumericProperty(0)

# Turn Button
class TurnButton(Button):
    name = StringProperty("OPEN")

class MainLayout(AnchorLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__()

STATUS_ALIVE = "ALIVE"
STATUS_DEAD = "DEAD"


class User(object):
    hp = NumericProperty(0)
    maxhp = NumericProperty(0)
    ap = NumericProperty(0)
    game_status = StringProperty(STATUS_ALIVE)
    lv = NumericProperty(0)

    def up_score(self, number):
        self.hp += 1

    def fight(self, ap):
        self.hp -= ap

        if self.hp <= 0:
            self.hp = 0
            self.game_status = STATUS_DEAD
            return 1
        return 0

class Enermy(User, Widget):
    exp = NumericProperty(0)
    gold = NumericProperty(0)
    name = StringProperty("")
    png = ListProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def load(self, enermy_info):
        self.ap = enermy_info["ap"]
        self.hp = enermy_info["hp"]
        self.exp = enermy_info["exp"]
        self.gold = enermy_info["gold"]
        self.game_status = STATUS_ALIVE
        self.name = enermy_info["name"]
        self.maxhp = enermy_info["maxhp"]
        self.png = enermy_info["png"]

class Player(User, Widget):
    exp = NumericProperty(0)
    gold = NumericProperty(0)

    def __init__(self, **kwargs):
        super(User, self).__init__()

    def get_reward(self, enermy):
        self.exp += enermy.exp

        if self.exp >= 5*(self.lv/2)*(1+self.lv):
            self.lv += 1
            self.exp = 0
            self.maxhp = self.lv * self.maxhp
            self.hp = self.maxhp
            self.ap = self.ap * 2
        self.gold += enermy.gold

    def save(self):
        return self.lv, self.ap, self.hp, self.maxhp

    def load(self, data):
        self.lv, self.ap, self.hp, self.maxhp = data



player_data = [1, 1, 1000, 1000]



def status_name(game_status):
    if game_status == GAME_STATUS_OPEN:
        return "OPEN"
    if game_status == GAME_STATUS_BATTLE:
        return "BATTLE"
    if game_status == GAME_STATUS_TURN:
        return "TURN"
    if game_status == GAME_STATUS_REWARD:
        return "REWARD"

# 컨트롤 부분을 밖으로 빼기 위함
from kivy.app import App
app = None

# root
class TurnBattle(Widget):
    player = Player()
    enermy = Enermy()
    door = DoorManager()

    game_status = GAME_STATUS_OPEN

    def update(self, dt):
        pass

    def init(self):
        self.player.lv = player_data[0]
        self.player.ap = player_data[1]
        self.player.hp = player_data[2]
        self.player.maxhp = player_data[3]

    def load_enermy(self):
        enermy_data = self.door.get_enermy_info()
        self.enermy.load(enermy_data)

    def _status_change(self, game_status):
        self.game_status = game_status

    def get_main_button_image(self, state):
        if self.game_status == GAME_STATUS_OPEN:
            return 'data/shadedDark26.png' if state == "down" else 'data/shadedLight26.png'
        elif self.game_status == GAME_STATUS_BATTLE:
            return 'data/shadedDark48.png' if state == "down" else 'data/shadedLight48.png'
        elif self.game_status == GAME_STATUS_TURN:
            return 'data/shadedDark49.png' if state == "down" else 'data/shadedLight49.png'
        elif self.game_status == GAME_STATUS_REWARD:
            return 'data/shadedDark28.png' if state == "down" else 'data/shadedLight28.png'
        else:
            raise



    def on_main_button(self, button, main_screen, enermy_screen, dmg, reward, floor):
        """ on_main_button turn """

        # Turn
        if self.game_status == GAME_STATUS_OPEN:
            # text code
            self.door.current_door = floor

            self.load_enermy()

            enermy_screen.center_x=enermy_screen.parent.center_x+35
            anim = Animation(center_x=enermy_screen.parent.center_x, duration=.2)
            if anim:
                anim.stop(self)
            anim.start(enermy_screen)

            self._status_change(GAME_STATUS_BATTLE)
        elif self.game_status == GAME_STATUS_BATTLE:
            self._status_change(GAME_STATUS_TURN)

        elif self.game_status == GAME_STATUS_TURN:
            # print dir(app.sound['swing'])
            app.sound['swing'].play()

            # enermy
            left = Animation(center_x=enermy_screen.parent.center_x-10, duration=.2)
            right = Animation(center_x=enermy_screen.parent.center_x, duration=.2)
            anim = left + right
            if anim:
                anim.stop(self)
            anim.start(enermy_screen)

            # player
            left = Animation(center_x=enermy_screen.parent.center_x-10, duration=.2)
            right = Animation(center_x=enermy_screen.parent.center_x, duration=.2)
            anim = left + right
            if anim:
                anim.stop(self)
            anim.start(enermy_screen)


            # damage
            dmg_anim = Animation(center_y=dmg.parent.center_y+80, duration=.2, t='out_circ')
            dmg_anim &= Animation(opacity=0, duration=.4)

            if dmg_anim:
                dmg.center_y = dmg.parent.center_y + 40
                dmg.opacity=1
                dmg_anim.stop(self)
            dmg_anim.start(dmg)


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
        elif self.game_status == GAME_STATUS_REWARD:
            app.sound['coin'].play()
            self.player.get_reward(self.enermy)


            # # reward
            # reward.center_y = reward.parent.center_y
            # reward.opacity=0
            # reward_anim = Animation(center_y=reward.parent.center_y+60, duration=1.0, t='out_circ')
            # reward_anim.bind(on_complete=self.wow)
            # # reward_anim &= Animation(opacity=1, duration=3.0)
            # reward_anim.start(reward)

            self._status_change(GAME_STATUS_OPEN)

        else:
            raise

        # Text button name change
        button.name = status_name(self.game_status)

class TurnApp(App):
    sound = {}
    music = None
    def build(self):
        global app
        app = self

        # background sound
        # start the background music:
        # self.music = SoundLoader.load('sound/8bitattempt.ogg')
        # self.music.bind(on_stop=self.sound_replay)
        # self.music.play()

        # sound
        self.sound['swing'] = SoundLoader.load('sound/battle/swing.ogg')
        self.sound['coin'] = SoundLoader.load('sound/inventory/chainmail1.ogg')


        self.title = 'One RPG'
        self.game = TurnBattle()
        self.game.init()
        # self.game.load_enermy()
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)
        return self.game

    def sound_replay(self, instance):
        if self.music.game_status != 'play':
            self.music.play()


    def on_pause(self):
        return True

if __name__ in ('__main__', '__android__'):
    TurnApp().run()

