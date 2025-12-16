#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand
import time

class res_auto_to_720p_for_switch2(PythonCommand):
    NAME = '自動→720p(高速解像度変更) For Switch2 ver.1.0.0'

    def __init__(self):
        super().__init__()

    def do(self):
        print("-------------------------------------")
        print("自動→720p(高速解像度変更) For Switch2 ver.1.0.0")
        print("Developed by しゅみる(XID:@PokeSyumiru)")
        print("本プログラムのライセンスは引用元のプログラムに準ずるものとします")
        print("Special Thanks to フウ(XID:@dragonite303)")
        print("quotation from https://drive.google.com/file/d/1XEylLiM8jDNyX_f_abcgZTeHeDh65F7q/view?usp=drive_link")
        print("-------------------------------------")
        
        self.res_auto_to_720p_for_switch2()

    def sendCommand(self, row: str, wait: float = 0.04):
        self.keys.ser.ser.write((row + '\r\n').encode('utf-8'))
        time.sleep(wait)
        self.checkIfAlive()

    def res_auto_to_720p_for_switch2(self):
        Neutral      = "0x0003 8 80 80 80 80"   # NEUTRAL
        Button_A     = "0x0013 8 80 80 80 80"   # A
        Home         = "0x4000 8 80 80 80 80"   # HOME
        Lstick_down  = "0x0003 8 80 ff 80 80"   # LSTICK-DOWN
        Rstick_down  = "0x0003 8 80 80 80 ff"   # RSTICK-DOWN
        Lstick_right = "0x0003 8 ff 80 80 80"   # LSTICK-RIGHT
        Rstick_right = "0x0003 8 80 80 ff 80"   # RSTICK-RIGHT
        Lstick_left  = "0x0003 8 00 80 80 80"   # LSTICK-LEFT
        Lstick_up    = "0x0003 8 80 00 80 80"   # LSTICK-UP

        # ホーム画面に戻る
        self.sendCommand(Home,         wait=0.20)
        self.sendCommand(Neutral,      wait=1.00)

        # ゲーム選択画面⇒設定
        self.sendCommand(Lstick_left,  wait=0.04) 
        self.sendCommand(Neutral,      wait=0.16) # 設定画面に移動できない場合は要調整。
        self.sendCommand(Lstick_down,  wait=0.04)
        self.sendCommand(Lstick_left,  wait=0.04)
        self.sendCommand(Button_A,     wait=0.80)

        # ディスプレイまで移動
        self.sendCommand(Lstick_down,  wait=0.15)
        self.sendCommand(Rstick_down,  wait=0.15)
        self.sendCommand(Lstick_down,  wait=0.15)
        self.sendCommand(Rstick_down,  wait=0.15)
        self.sendCommand(Lstick_down,  wait=0.15)
        self.sendCommand(Rstick_down,  wait=0.15)
        self.sendCommand(Lstick_down,  wait=0.15)
        self.sendCommand(Rstick_down,  wait=0.15)
        self.sendCommand(Lstick_down,  wait=0.15)
        self.sendCommand(Rstick_down,  wait=0.15)
        self.sendCommand(Lstick_down,  wait=0.15)
        self.sendCommand(Button_A,     wait=0.30)

        # 720p→自動
        self.sendCommand(Lstick_down,  wait=0.04)
        self.sendCommand(Button_A,     wait=0.04) 
        self.sendCommand(Neutral,      wait=0.16)
        self.sendCommand(Lstick_down,  wait=0.04)
        self.sendCommand(Button_A,     wait=0.10) 

        # ゲーム画面に戻る
        self.sendCommand(Home,         wait=0.08)
        self.sendCommand(Neutral,      wait=1.00)
        self.sendCommand(Button_A,     wait=0.30)
