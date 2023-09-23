#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick, Hat
import time

class paojian_c0(ImageProcPythonCommand):
    NAME = 'paojian_c0'

    def __init__(self, cam):
        super().__init__(cam)
        
    def do(self):
        print("プログラム開始")
        bt_count = 0
        tm_count = 0
        hp383_count = 0
        hp350_count = 0
        hp367_count = 0
        hp367_k_count = 0
        k_count = 0
        hu_g_count = 0
        pao_count = 0
        pao_life_count = 0
        c0_count = 0
        ikiti = False

        time_sta = time.time()
        while True:
            self.wait(0.5)
            print("---------------------------------------------")
            print("パオジアンC0厳選_ver1")      
            print("Developed     by.ひびき")
            print("戦闘回数 : ",bt_count,"回")
            print("時間リセット : ",tm_count,"回")
            print("H383のパオジアン : ",hp383_count,"回")
            print("H350のパオジアン : ",hp350_count,"回")
            print("H367のパオジアン : ",hp367_count,"回")
            print("H367かつ混乱したパオジアン : ",hp367_k_count,"回")
            print("H367以外の混乱したパオジアン : ",k_count,"回")
            print("フワライド回復 : ",hu_g_count,"回")
            print("パオジアン討伐 : ",pao_count,"回")            
            print("パオジアンＨＰ確認 : ",pao_life_count,"回")
            print("C0のパオジアン : ",c0_count,"回")

            print("---------------------------------------------")            

            bt_count += 1
            while not self.isContainTemplate('paojian/paojian.png', threshold=0.7, use_gray=True, show_value=ikiti):      
                self.press(Button.A, wait=0.3)
            print("わざわいのつるぎを確認しました")     
            while not self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti):      
                self.wait(0.1)
            print("戦闘を確認しました") 
            #戦う
            self.press(Button.A, wait=1.0)
            #ちからをすいとる
            self.press(Button.A, wait=1.0)           
            #HP確認
            resetflag = False
            while True:    
                if self.isContainTemplate('paojian/HP383.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    count = 1
                    hp383_count += 1
                    print("HP383のパオジアンです") 
                    print(count)
                    break                             
                if self.isContainTemplate('paojian/HP350.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    count = 2
                    hp350_count += 1
                    print("HP350のパオジアンです")
                    print(count)
                    break
                if self.isContainTemplate('paojian/HP367.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    count = 3
                    hp367_count += 1
                    print("HP367のパオジアンです")
                    print(count) 
                    break          
                if self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti): 
                    print("HPが規定外のため、リセットします")
                    resetflag = True
                    break
            self.wait(0.1)
            if resetflag:
                self.softreset()
                continue

            print("待機しています")
            self.wait(5.0)    
            while not self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                self.wait(0.1)
            print("戦闘画面確認しました") 
            #戦う
            self.press(Button.A, wait=1.0)
            #投げつける（ウイのみ）
            self.press(Direction.DOWN, wait=0.6)
            self.press(Button.A, wait=1.0)

            g_resetflag = False  
            while True:
                if self.isContainTemplate('paojian/paogain.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    print("パオジアン回復")
                    break
                if self.isContainTemplate('paojian/gain.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                    print("フワライド回復")
                    print("リセットします")
                    g_resetflag = True
                    hu_g_count += 1 
                    break
            self.wait(0.1)
            if g_resetflag:
                self.softreset()            
                continue

            
            resetflag2 = False
            while True:
                if self.isContainTemplate('paojian/konran_2.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    print("混乱しました") 
                    if count == 3:
                        count = 4
                        print(count)
                        hp367_k_count += 1
                        break     
                    else:
                        print("HP367以外かつ混乱のため、リセットします")
                        resetflag2 = True
                        k_count += 1                
                        break
                if self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                    print("戦闘画面確認しました2")
                    break
            self.wait(0.1)
            if resetflag2:
                self.softreset()            
                continue

            print("待機しています")
            self.wait(1.0)
            while not self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                self.wait(0.1)
            print("戦闘画面確認しました3")               
            #戦う
            self.press(Button.A, wait=1.0)
            #おきみやげ
            self.press(Direction.DOWN, wait=0.6)
            self.press(Button.A, wait=1.0)

            print("待機しています")
            self.wait(1.0)    
            while not self.isContainTemplate('paojian/hinshi.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                self.wait(0.1)

            #いれかえ
            print("いれかえを行います")
            for i in range(count):
                self.press(Direction.DOWN, wait=0.6)
            #ポケモン決定
            self.press(Button.A, wait=1.0)
            #入れ替え
            self.press(Button.A, wait=1.0)
            
            #アメタマ
            print("待機しています")
            self.wait(5.0)    
            while not self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                self.wait(0.1)
            print("戦闘画面確認しました4") 
            #戦う
            self.press(Button.A, wait=1.0)
            #パワーシャア
            self.press(Button.A, wait=1.0)

            print("待機しています")
            self.wait(5.0)
            while not self.isContainTemplate('paojian/fight.png', threshold=0.7, use_gray=True, show_value=ikiti):            
                self.wait(0.1)
            print("戦闘画面確認しました5") 
            #戦う
            self.press(Button.A, wait=1.0)
            #水テラバースト
            self.press(Button.R, wait=1.0)
            self.press(Direction.DOWN, wait=0.6)
            if self.isContainTemplate('paojian/waterteraba.png', threshold=0.9, use_gray=True, show_value=ikiti):
                print("テラバースト") 
                self.press(Button.A, wait=1.0)



            resetflag3 = False
            while True:    
                if self.isContainTemplate('paojian/fight.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    print("戦闘画面確認しました6")
                    break                             
                if self.isContainTemplate('paojian/paohinshi.png', threshold=0.9, use_gray=True, show_value=ikiti):
                    print("パオジアン討伐")
                    print("リセットします")
                    resetflag3 = True
                    pao_count += 1
                    break
            if resetflag3: 
                self.softreset()
                continue

            #パオジアン体力確認        
            if self.isContainTemplate('paojian/paolife.png', threshold=0.9, use_gray=True, show_value=ikiti):
                print("C0,1です")
                c0_count += 1 
                self.finish()
            else:
                print("C0以外のためリセットします")
                pao_life_count += 1
                self.softreset()

            #経過時間でリセット
            time_elp = time.time() - time_sta
            if time_elp > 470:
                print("とりあえずリセットします")
                tm_count += 1
                self.softreset()          

    

    
            

    #ゲームリセット
    def softreset(self):
        self.wait(0.5)
        self.press(Button.HOME, wait=0.5)
        self.wait(0.5)
        self.press(Button.X, wait=0.5)
        self.wait(0.5)
        self.press(Button.A, wait=2.0) 
        self.press(Button.A, wait=2.0) 
        self.press(Button.A, wait=2.0) 
        while not self.isContainTemplate('paojian/S_TOP.png', threshold=0.8, use_gray=True, show_value=False):
            self.wait(0.5)
            self.press(Button.A, wait=1.0)
        print("TOP画面を認識しました。")
        self.wait(3.0)
        self.press(Button.A, wait=1.0)





