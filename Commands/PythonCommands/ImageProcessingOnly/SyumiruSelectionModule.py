#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button
import cv2
import configparser
from typing import Any
from Commands.PythonCommandBase import ImageProcPythonCommand

# iniファイルを参照する
def Config_Read(self):
    
	config = configparser.ConfigParser()
	config.read('./Template/Syumiru/setting.ini', encoding='utf-8')
 
	SV = 'SV'
	Game_Start_Wait_Time = 'Game_Start_Wait_Time'
 
	self.Game_Start_Wait_Time = config.getfloat(SV,Game_Start_Wait_Time)

	SV_A0_A0S0GACHIGUMA = 'SV_A0_A0S0GACHIGUMA'
	Check_Speed ='Check_Speed'
	Choice_Ball ='Choice_Ball'
	Pokedex ='Pokedex'
	Test_Check_Status = 'Test_Check_Status'
	A103 = 'A103'
	S77 = 'S77'
	S78 = 'S78'
	A124 = 'A124'
	S99 = 'S99'
	Battle_Scene = 'Battle_Scene'
	Battle_Command = 'Battle_Command'
	Gachiguma_Attack = 'Gachiguma_Attack'
	ScreenShot = 'ScreenShot'
	self.Check_Speed = config.getint(SV_A0_A0S0GACHIGUMA,Check_Speed)
	self.Choice_Ball = config.getint(SV_A0_A0S0GACHIGUMA,Choice_Ball)
	self.Pokedex = config.getint(SV_A0_A0S0GACHIGUMA,Pokedex)
	self.Test_Check_Status = config.getint(SV_A0_A0S0GACHIGUMA,Test_Check_Status)
	self.A103 = config.getfloat(SV_A0_A0S0GACHIGUMA,A103)
	self.S77 = config.getfloat(SV_A0_A0S0GACHIGUMA,S77)
	self.S78 = config.getfloat(SV_A0_A0S0GACHIGUMA,S78)
	self.A124 = config.getfloat(SV_A0_A0S0GACHIGUMA,A124)
	self.S99 = config.getfloat(SV_A0_A0S0GACHIGUMA,S99)
	self.Battle_Scene = config.getfloat(SV_A0_A0S0GACHIGUMA,Battle_Scene)
	self.Battle_Command = config.getfloat(SV_A0_A0S0GACHIGUMA,Battle_Command)
	self.Gachiguma_Attack = config.getfloat(SV_A0_A0S0GACHIGUMA,Gachiguma_Attack)
	self.ScreenShot = config.getint(SV_A0_A0S0GACHIGUMA,ScreenShot)
	SV_C0_Paojian = 'SV_C0_Paojian'
	No_Correction_Only = 'No_Correction_Only'
 
	self.No_Correction_Only = config.getint(SV_C0_Paojian,No_Correction_Only)
# 画面内の座標を指定して認識を行うための関数(こちゃてす@kochatece12さんのプログラムからお借りしています)
def isContainTemplateSuper(self, template_path, search_range, threshold=0.7, use_gray=True, show_value=False,print_value=0.5,Coordinate=False):
	TEMPLATE_PATH = "./Template/"
	src = self.camera.readFrame()
	# ↓座標を指定する場合は [y座標最小,y座標最大,x座標最小,x座標最大] で入力します
	src = src[search_range[0]:search_range[1],search_range[2]:search_range[3]]
	src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) if use_gray else src

	template = cv2.imread(TEMPLATE_PATH+template_path, cv2.IMREAD_GRAYSCALE if use_gray else cv2.IMREAD_COLOR)
	w, h = template.shape[1], template.shape[0]

	method = cv2.TM_CCOEFF_NORMED
	res = cv2.matchTemplate(src, template, method)
	_, max_val, _, max_loc = cv2.minMaxLoc(res)

	if show_value:
		if max_val > print_value:
			print(template_path + ' value: ' + str(round(max_val,3)))
	
	top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	if max_val > threshold:
		if use_gray:
			src = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
		if Coordinate:
			return True, bottom_right
		else:
			return True
	else:
		if Coordinate:
			return False, bottom_right
		else:
			return False

# ソフトリセット用の関数(元関数作成：お修羅さん(@_Oshura_))
def SOFT_RESET(self):
	self.SOFT_ERROR = False
	while True:
		if self.SOFT_ERROR == False:
			# リセット初回はここを通る
			self.press(Button.HOME,0.05,1.5)
			# ソフトの終了
			self.press(Button.X,0.05,0.5)
		# リセット時にソフトエラーが起きていた場合はここを通る
		else:
			pass
		self.press(Button.A,0.05,3.0)
		# ソフトを開く
		self.pressRep(Button.A, repeat=5, duration=0.05, interval=0.5)
		# ゲーフリロゴを認識したら7.0秒後にAボタンを入力
		while not (self.isContainTemplate('Syumiru/SV_A0_A0S0GACHIGUMA/OPENING.png',0.8, use_gray=True, show_value=False)):
			self.wait(0.1)
		self.wait(7.0)
		self.pressRep(Button.A, repeat=5, duration=0.05, interval=0.5)
		# フィールド画面に移行するまで待機する
		self.wait(self.Game_Start_Wait_Time)
		# 起動直後にソフトエラー表示が出ることがあるためチェックを行う
		if self.isContainTemplate('Syumiru/SV_A0_A0S0GACHIGUMA/ERROR.png',0.8, use_gray=True, show_value=False):
			print("\n---------------------------------------")
			print("\n★ソフトリセット中にエラーが発生しました★")
			print("\n---------------------------------------")
			self.discord_text("★ソフトリセット中にエラーが発生しました★")
			# SOFT_RESET()の先頭の処理に戻る
			self.SOFT_ERROR = True
			self.ERROR_COUNT += 1
		# 本体の再起動が必要なエラーが出ている場合は直ちにプログラムを停止する
		elif self.isContainTemplate('Syumiru/SV_A0_A0S0GACHIGUMA/ERROR_2.png',0.8, use_gray=True, show_value=False):
			#notification.notify(title='★S0赫月ガチグマ厳選',message='危険なエラーが発生したため動作を停止します',app_name='Poke-Controller')
			self.discord_text("危険なエラーが発生しているためプログラムの動作を停止しました")
			print("\n---------------------------------------")
			print("\n危険なエラーが発生しているためプログラムの動作を停止しました")
			print("\n---------------------------------------\n")
			self.finish()
		# 起動直後にソフトエラー表示が出ていない場合はここを通る
		else:
			# メインのプログラムに戻る
			return True