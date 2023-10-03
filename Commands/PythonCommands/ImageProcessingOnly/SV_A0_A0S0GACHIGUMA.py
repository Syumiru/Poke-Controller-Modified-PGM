#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
import time
import cv2
from Commands.PythonCommands.ImageProcessingOnly import SyumiruSelectionModule
#from plyer import notification

# -----------------------------------------------------------------------------------------------------------------------------------------
# Windows通知を利用する場合は #notification.notifyのコメントアウトを削除してください． ※利用するにはPlyerモジュールのインポートが必要です．
# -----------------------------------------------------------------------------------------------------------------------------------------

class ScarletViolet2(ImageProcPythonCommand):
	NAME = '[SV]A0S0赫月ガチグマ厳選'
 
	def __init__(self, cam):
		super().__init__(cam)
		self.cam = cam

	def do(self):
		print("\n\n--------------------------------------------------")
		print("\nDeveloped By Syumiru (@PokeSyumiru)")
		print("\nTested By @ASTRY")
		print("\nUpdated By アリス (@Alice_lonewolf)")
		print("\nSpecial Thanks to お修羅 (@_Oshura_)")
		print("\nSpecial Thanks to こちゃてす (@kochatece12)") 
		print("\nSpecial Thanks to PokeconDeveloppers") 
		print("\n--------------------------------------------------")
		print("\n・サザレの目の前に立ったらレポートを書きましょう")
		print("\n・A0~1かつS0~1赫月ガチグマを厳選する場合は")
		print("\n・S78or79かつワンパンできるポケモンがおすすめです")
		print("\n--------------------------------------------------")
		print("\n以上の項目をしっかり確認したらスタートしましょう")
		print("\n--------------------------------------------------\n\n")
		# マイコンをSwitchに認識させる
		self.pressRep(Button.ZL, repeat=3, duration=0.05, interval=0.8, wait=0.5)
		# ----------------------------------------------------------------------------------------------------------------------
		#iniファイルを参照する
		SyumiruSelectionModule.Config_Read(self)
		#LINE通知機能のテスト
		SyumiruSelectionModule.LINE_TEST(self)
		# ----------------------------------------------------------------------------------------------------------------------
		# 海外言語で厳選する方は以下をご確認ください ---------------------------------------------------------------------------------
		# 日本語以外のガチグマを厳選する場合、画像認識に使用するキャプチャの書き換えが必須となります．
		# 戦闘画面で技選択後，画面下部に表示される「野生のガチグマの～」の「ガチグマ」に該当する部分をPoke-Controllerでキャプチャしてください．
		# 余白を入れないように文字だけを切り取ったら，SV_A0_A0S0GACHIGUMAフォルダにGACHIGUMA_ATTACK.pngの名称で保存してください．
		# -----------------------------------------------------------------------------------------------------------------------
		# 周回数を記録します
		self.LOOP_COUNT = 0
		# リセット時のエラー回数を記録します
		self.ERROR_COUNT = 0
		# プログラム開始時から時間を計測
		Program_start = time.time()
		# メイン処理
		while True:
			self.LOOP_COUNT += 1
			# プログラム稼働時間を算出する
			Time_Clock = time.time()
			Time_Clock = Time_Clock - Program_start
			print("\n---------------------------------------")
			print("\n★赫月ガチグマとの戦闘まで進行します★")
			print("\n---------------------------------------")
			print(f"\n周回数：{self.LOOP_COUNT} エラー: {self.ERROR_COUNT} / {(int(Time_Clock / 3600))}時間 {(int(Time_Clock / 60) % 60)}分 {(int(Time_Clock % 60))}秒")
			print("\n---------------------------------------\n")
			# 赫月ガチグマとの戦闘画面になるまでAボタン連打
			while not self.isContainTemplate('Syumiru/SV_A0_A0S0GACHIGUMA/!!!!.png', self.Battle_Scene, use_gray=False, show_value=False):
				self.press(Button.A,0.05,0.05)
			self.wait(0.5)
			print("\n---------------------------------------")
			print("\n★赫月ガチグマとエンカウント 戦闘開始★")
			print("\n---------------------------------------")
			# コマンド出現まで待機
			while not self.isContainTemplate('Syumiru/SV_A0_A0S0GACHIGUMA/BATTLE_COMMANDS.png', self.Battle_Command, use_gray=True, show_value=False):
				self.wait(0.5)
			self.wait(1.0)
			# 攻撃コマンドを選択
			self.pressRep(Button.A, repeat=2, duration=0.05, interval=0.8, wait=1.7)
			# 実数値判定テストがオフかつA0~1S0~1赫月ガチグマを厳選する場合は判定を行う
            # 赫月ガチグマに先制を取られた場合はS0ではないためソフトリセットを行う
			if self.Test_Check_Status == 1 and self.Check_Speed == 1 and SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/GACHIGUMA_ATTACK.png', [530,562,185,495], self.Gachiguma_Attack, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\n★赫月ガチグマがS0である可能性: なし★")
				print("\nソフトリセットします")
				print("\n---------------------------------------")
			# 手持ちのポケモンが先制を取った場合はS0かも
			else:
				# A0~1S0~1赫月ガチグマを厳選する場合のみ出力
				if self.Check_Speed == 1:
					print("\n---------------------------------------")
					print("\n★赫月ガチグマがS0である可能性: あり★")
					print("\n---------------------------------------")
     				# オリーヴァによる攻撃で超低確率なる事象へ対応。再度攻撃が必要になる場合を考慮しリードタイムを設ける
					self.wait(26.5)
				# 演出待機
				self.wait(16.5)
				# 判定
				# 捕まえるを選択
				self.press(Button.A,0.05,0.05)
				self.wait(0.6)
				# ボールカウント初期化
				self.Ball_Count = 0
				# ボール選択
				while self.Ball_Count < self.Choice_Ball:
					# 左を押下
					self.press(Direction.LEFT, wait=0.3)
					self.Ball_Count += 1
				# ボール決定
				self.press(Button.A,0.05,0.05)
				self.wait(20.0)
				if self.Pokedex == 1:
					# 図鑑登録でテキスト送り
					self.press(Button.A,0.05,0.05)
					self.wait(1.0)
				# ステータス確認
				# 下を押下
				self.press(Direction.DOWN, wait=0.5)
				# ガチグマのステータス確認を選択
				self.press(Button.A,0.05,0.05)
				self.wait(1.0)
				# ガチグマのステータス画面へ移行bbbb
				self.press(Direction.RIGHT, wait=1.0)
				# 攻撃判定（103判定）
				if SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/103.png', [248,272,1088,1139], self.A103, use_gray=True, show_value=False):
					print("\n---------------------------------------")
					print("\n★A0-1です★")
					print("\n---------------------------------------")
					# A0を厳選する場合
					if self.Check_Speed == 0:
						#notification.notify(title='★S0赫月ガチグマ厳選',message='S0出現の可能性あり',app_name='Poke-Controller')
						print("\n---------------------------------------")
						print("\n★A0-1赫月ガチグマを捕獲しました★")
						print("\n---------------------------------------")
						# LINE通知機能
						if self.Line_Notify_Switch:
							# 厳選完了報告をLINEに送信します
							SyumiruSelectionModule.LINE_Message(self,"🖋LINE通知\n"
								f"赫月ガチグマを捕獲しました\n"
								f"確認お願いします。", True)
						# HOMEボタンを長押ししてスリープ
						self.press(Button.HOME,2,2)
						self.press(Button.A,0.05,0.05)
						# プログラムを終了する
						self.finish()
					# A0かつS0を厳選する場合
					else:
					# 素早さ判定（77判定）
						if SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/77.png', [449,472,957,991], self.S77, use_gray=True, show_value=False):
							print("\n---------------------------------------")
							print("\n★A0-1かつS0の可能性がある赫月ガチグマを捕獲しました★")
							print("\n---------------------------------------")
							# LINE通知機能
							if self.Line_Notify_Switch:
								# 厳選完了報告をLINEに送信します
								SyumiruSelectionModule.LINE_Message(self,"🖋LINE通知\n"
									f"A0-1かつS0の\n"
									f"赫月ガチグマを捕獲しました", True)
		
							# HOMEボタンを長押ししてスリープ
							self.press(Button.HOME,2,2)
							self.press(Button.A,0.05,0.05)
							# プログラムを終了する
							self.finish()
						# 素早さ判定（78判定）
						elif SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/78.png', [449,472,957,991], self.S78, use_gray=True, show_value=False):
							print("\n---------------------------------------")
							print("\n★A0-1かつS1の可能性がある赫月ガチグマを捕獲しました★")
							print("\n---------------------------------------")
							if self.Line_Notify_Switch:
								# LINE通知機能
								# 厳選完了報告をLINEに送信します
								SyumiruSelectionModule.LINE_Message(self,"🖋LINE通知\n"
									f"A0-1かつS1の\n"
									f"赫月ガチグマを捕獲しました", True)
							# HOMEボタンを長押ししてスリープ
							self.press(Button.HOME,2,2)
							self.press(Button.A,0.05,0.05)
							# プログラムを終了する
							self.finish()
				# 実数値判定テスト機能
				if self.Test_Check_Status == 0:
				# 攻撃判定（124判定）※テスト
					if SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/124.png', [248,272,1088,1139],  self.A124, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\nA31です")
						print("\n---------------------------------------")	
					# 攻撃判定（103判定）※テスト
					elif SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/103.png', [248,272,1088,1139], self.A103, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\nA0-1です")
						print("\n---------------------------------------")
					# 素早さ判定（99判定）※テスト
					if SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/99.png', [449,472,957,991], self.S99, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\nS31です")
						print("\n---------------------------------------")
					# 素早さ判定（77判定）※テスト
					elif SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/77.png', [449,472,957,991], self.S77, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\nS0です")
						print("\n---------------------------------------")
					# 素早さ判定（78判定）※テスト
					elif SyumiruSelectionModule.isContainTemplateSuper(self,'Syumiru/SV_A0_A0S0GACHIGUMA/78.png', [449,472,957,991], self.S78, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\nS1です")
						print("\n---------------------------------------")
					print("\n---------------------------------------")
					print("\n5秒後にソフトリセットします")
					print("\n---------------------------------------")
					self.wait(5.0)	
				# スクショ保存
				if self.ScreenShot == 1:
					self.camera.saveCapture()
			# ソフトリセット
			SyumiruSelectionModule.SOFT_RESET(self)
			# プログラムの先頭に戻る
			self.wait(0.5)