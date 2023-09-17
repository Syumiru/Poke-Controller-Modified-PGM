#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
import time
import cv2
#from plyer import notification

# -----------------------------------------------------------------------------------------------------------------------------------------
# Windows通知を利用する場合は 8行目/ 107行目のコメントアウトを削除してください． ※利用するにはPlyerモジュールのインポートが必要です．
# -----------------------------------------------------------------------------------------------------------------------------------------

class ScarletViolet2(ImageProcPythonCommand):
	NAME = '[SV]A0S0赫月ガチグマ厳選'
	def __init__(self, cam,Speed):
		super().__init__(cam)
		self.cam = cam

	def do(self):
		print("\n\n--------------------------------------------------")
		print("\nDeveloped By Syumiru (@PokeSyumiru)")
		print("\nSpecial Thanks to お修羅 (@_Oshura_)")
		print("\nSpecial Thanks to こちゃてす (@kochatece12)") 
		print("\nSpecial Thanks to PokeconDeveloppers") 
		print("\n--------------------------------------------------")
		print("\n・サザレの目の前に立ったらレポートを書きましょう")
		print("\n・カイオーガ等ワンパンできるポケモン必須")
		print("\n--------------------------------------------------")
		print("\n以上の項目をしっかり確認したらスタートしましょう")
		print("\n--------------------------------------------------\n\n")
		self.wait(3.0)
		# マイコンをSwitchに認識させる
		self.pressRep(Button.ZL, repeat=3, duration=0.05, interval=0.8, wait=0.5)

		# ----------------------------------------------------------------------------------------------------------------------
		# ソフトリセット時にオープニング画面でAボタンを押してからフィールド画面に移行するまでの待機時間．
		# 作者の環境では約18秒でしたが厳選に使用するデータの環境に合わせて適宜編集してください．
		self.WAIT_TIME = 18.0
		# LINE Notifyで発行したトークンを貼るとLINE通知が利用できます．利用しない場合はデフォルトのままでOK．エラー通知に利用します．
		self.Line_Notify_Token = "Gdp1DVv9ODbmsbd7Ci4OSfXP9EgQOAM2mdDCsmWJrJ2"
		# LINE送信のテストを行う場合は1，テストを行わない場合は0を入力してください．1にするとプログラム開始時に送信テストを行ったのち停止します．
		self.LINE_TEST = 0
		# ----------------------------------------------------------------------------------------------------------------------

		# 海外言語で厳選する方は以下をご確認ください ---------------------------------------------------------------------------------
		# 日本語以外のガチグマを厳選する場合、画像認識に使用するキャプチャの書き換えが必須となります．
		# 戦闘画面で技選択後，画面下部に表示される「野生のガチグマの～」の「ガチグマ」に該当する部分をPoke-Controllerでキャプチャしてください．
		# 余白を入れないように文字だけを切り取ったら，SV_A0_A0S0GACHIGUMAフォルダにGACHIGUMA_ATTACK.pngの名称で保存してください．
		# キャプチャ書き換え後に戦闘画面で正常に読み取りできない場合は当プログラム99行目の座標を編集してください．
		# -----------------------------------------------------------------------------------------------------------------------

		# 周回数を記録します
		self.LOOP_COUNT = 0
		# リセット時のエラー回数を記録します
		self.ERROR_COUNT = 0
		# プログラム開始時から時間を計測
		Program_start = time.time()
		# パラメータ0の時対象外、1の時対象
		self.Speed = 0
		# LINE通知テストを行う場合はここを通る
		if self.LINE_TEST == 1:
			print("\n-----------------------------")
			print("\n★LINE通知のテストを行います★")
			print("\n-----------------------------")
			print("\n通知が来ない場合LINEトークンに")
			print("\n間違いがないか確認してください")
			print("\n-----------------------------\n")
			# テスト用の内容をLINEに送信します
			self.LINE_Message("🖋LINE通知テスト\n"
							f"これはテスト用の通知内容です\n"
							f"現在の画面をキャプチャしています", True)
			# LINE通知後はプログラムを停止する
			self.finish()
		else:
			pass

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
			while not self.isContainTemplate('SV_A0_A0S0GACHIGUMA/!!!!.png', 0.97, use_gray=False, show_value=False):
				self.press(Button.A,0.05,0.05)
			self.wait(0.5)
			print("\n---------------------------------------")
			print("\n★赫月ガチグマとエンカウント 戦闘開始★")
			print("\n---------------------------------------")
			# コマンド出現まで待機
			while not self.isContainTemplate('SV_A0_A0S0GACHIGUMA/BATTLE_COMMANDS.png', 0.8, use_gray=True, show_value=False):
				self.wait(0.5)
			self.wait(1.0)
			# 攻撃コマンドを選択
			self.pressRep(Button.A, repeat=2, duration=0.05, interval=0.8, wait=1.7)
			# 演出待機
			self.wait(16.5)
			# 判定
			# 捕まえるを選択
			self.press(Button.A,0.05,0.05)
			self.wait(0.6)
			# ボール選択
			# 左を押下
			self.press(Direction.LEFT, wait=0.3)
			# 左を押下
			self.press(Direction.LEFT, wait=0.3)
			# 左を押下
			self.press(Direction.LEFT, wait=0.3)
			# ムーンボールを選択
			self.press(Button.A,0.05,0.05)
			self.wait(20.0)
			# 図鑑登録でテキスト送り
			self.press(Button.A,0.05,0.05)
			self.wait(1.0)
			# ステータス確認
			# 下を押下
			self.press(Direction.DOWN, wait=0.5)
			# ガチグマのステータス確認を選択
			self.press(Button.A,0.05,0.05)
			self.wait(1.0)
			# ガチグマのステータス画面へ移行
			self.press(Direction.RIGHT, wait=1.0)
			# 攻撃判定（103判定）
			if self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/103.png', [248,272,1088,1139], 0.9, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\n★A0-1です★")
				print("\n---------------------------------------")
				# A0を厳選する場合
				if self.Speed == 0:
					#notification.notify(title='★S0赫月ガチグマ厳選',message='S0出現の可能性あり',app_name='Poke-Controller')
					print("\n---------------------------------------")
					print("\n★A0-1赫月ガチグマを捕獲しました★")
					print("\n---------------------------------------")
					# 少しだけ待つ
					self.wait(5.0)
					# 動画を保存する
					self.press(Button.CAPTURE,1.0,5.0)
					# Syumiru Add Start 20230916
					# 厳選完了報告をLINEに送信します
					self.LINE_Message("🖋LINE通知\n"
								f"赫月ガチグマを捕獲しました\n"
								f"確認お願いします。", True)
					# HOMEボタンを長押ししてスリープ
					self.press(Button.HOME,2,2)
					self.press(Button.A,0.05,0.05)
					# Syumiru Add  Ehd  20230916
					# プログラムを終了する
					self.finish()
				# A0かつS0を厳選する場合
				else:
				# 素早さ判定（77判定）
					if self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/77.png', [449,472,957,991], 0.9, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\n★A0-1かつS0の可能性がある赫月ガチグマを捕獲しました★")
						print("\n---------------------------------------")
						# 少しだけ待つ
						self.wait(5.0)
						# 動画を保存する
						self.press(Button.CAPTURE,1.0,5.0)
						# Syumiru Add Start 20230916
						# 厳選完了報告をLINEに送信します
						self.LINE_Message("🖋LINE通知\n"
									f"A0-1かつS0の\n"
									f"赫月ガチグマを捕獲しました", True)
						# HOMEボタンを長押ししてスリープ
						self.press(Button.HOME,2,2)
						self.press(Button.A,0.05,0.05)
						# Syumiru Add  Ehd  20230916
						# プログラムを終了する
						self.finish()
					# 素早さ判定（78判定）
					elif self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/78.png', [449,472,957,991], 0.9, use_gray=True, show_value=False):
						print("\n---------------------------------------")
						print("\n★A0-1かつS1の可能性がある赫月ガチグマを捕獲しました★")
						print("\n---------------------------------------")
						# 少しだけ待つ
						self.wait(5.0)
						# 動画を保存する
						self.press(Button.CAPTURE,1.0,5.0)
						# Syumiru Add Start 20230916
						# 厳選完了報告をLINEに送信します
						self.LINE_Message("🖋LINE通知\n"
									f"A0-1かつS1の\n"
									f"赫月ガチグマを捕獲しました", True)
						# HOMEボタンを長押ししてスリープ
						self.press(Button.HOME,2,2)
						self.press(Button.A,0.05,0.05)
						# Syumiru Add  Ehd  20230916
						# プログラムを終了する
						self.finish()
			# 攻撃判定（124判定）※テスト
			if self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/124.png', [248,272,1088,1139],  0.9, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\nA31です")
				print("\n---------------------------------------")	
			# 攻撃判定（103判定）※テスト
			elif self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/103.png', [248,272,1088,1139], 0.9, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\nA0-1です")
				print("\n---------------------------------------")	
			# 素早さ判定（99判定）※テスト
			if self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/99.png', [449,472,957,991], 0.9, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\nS31です")
				print("\n---------------------------------------")
			# 素早さ判定（77判定）※テスト
			elif self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/77.png', [449,472,957,991], 0.9, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\nS0です")
				print("\n---------------------------------------")
			# 素早さ判定（78判定）※テスト
			elif self.isContainTemplateSuper('SV_A0_A0S0GACHIGUMA/78.png', [449,472,957,991], 0.9, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\nS1です")
				print("\n---------------------------------------")
			print("\n---------------------------------------")
			print("\n5秒後にソフトリセットします")
			print("\n---------------------------------------")
			self.wait(5.0)	
			# ソフトリセット
			self.SOFT_RESET()
			# プログラムの先頭に戻る
			self.wait(0.5)						
   
	# ソフトリセット用の関数(関数作成：お修羅さん(@_Oshura_))
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
			while not (self.isContainTemplate('SV_A0_A0S0GACHIGUMA/OPENING.png',0.8, use_gray=True, show_value=False)):
				self.wait(0.1)
			self.wait(7.0)
			self.pressRep(Button.A, repeat=5, duration=0.05, interval=0.5)
			# フィールド画面に移行するまで待機する
			self.wait(self.WAIT_TIME)
			# 起動直後にソフトエラー表示が出ることがあるためチェックを行う
			if self.isContainTemplate('SV_A0_A0S0GACHIGUMA/ERROR.png',0.8, use_gray=True, show_value=False):
				print("\n---------------------------------------")
				print("\n★ソフトリセット中にエラーが発生しました★")
				print("\n---------------------------------------")
				self.LINE_image(f"ERROR通知\nプログラム名: S0赫月ガチグマ厳選", True)
				# SOFT_RESET()の先頭の処理に戻る
				self.SOFT_ERROR = True
				self.ERROR_COUNT += 1
			# 本体の再起動が必要なエラーが出ている場合は直ちにプログラムを停止する
			elif self.isContainTemplate('SV_A0_A0S0GACHIGUMA/ERROR_2.png',0.8, use_gray=True, show_value=False):
				#notification.notify(title='★S0赫月ガチグマ厳選',message='危険なエラーが発生したため動作を停止します',app_name='Poke-Controller')
				self.LINE_image(f"ERROR通知\n危険なエラーが発生しているため\nプログラムの動作を停止しました\nプログラム名: S0赫月ガチグマ厳選", True)
				print("\n---------------------------------------")
				print("\n重要なエラー 続行不可のため動作停止します")
				print("\n---------------------------------------\n")
				self.finish()
			# 起動直後にソフトエラー表示が出ていない場合はここを通る
			else:
				# メインのプログラムに戻る
				return True
			
	# 本家Poke-Controllerをお使いの方もLINE通知が送れるようにしました(関数作成：こちゃてすさん(@Kochatece12))
	def LINE_Message(self,notification_message, Picture=False):
		"""
		他のプログラムにLINE通知を導入する場合
		１.この関数全体をプログラムの一番下に入れる。(インデント込み)
		２.以下の関数呼び出しをコピーし、プログラムの任意の位置に入れる

		・テキストのみを通知する場合
		self.LINE_Message("通知したい文章")
		・poke-Controllerに映っている映像を画像として送信する場合
		self.LINE_Message("通知したい文章", True)
		"""
		from PIL import Image
		import io
		try:
			import requests
		except:
			print("\n---------------------------------------")
			print("\nLINE通知を実行できません")
			print("\nrequestsモジュールエラーです")
			print("\n---------------------------------------\n")		
		try:
			line_notify_api = "https://notify-api.line.me/api/notify"
			headers = {"Authorization": f"Bearer {self.Line_Notify_Token}"}
			data = {"message": f"{notification_message}"}
			files = {}
			if Picture == True:
				image_bgr = self.camera.readFrame()
				image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
				image = Image.fromarray(image_rgb)
				png = io.BytesIO()  # 空のio.BytesIOオブジェクトを用意
				image.save(png, format="png")  # 空のio.BytesIOオブジェクトにpngファイルとして書き込み
				b_frame = png.getvalue()  # io.BytesIOオブジェクトをbytes形式で読みとり
				files = {"imageFile": b_frame}
			requests.post(line_notify_api, headers = headers, data = data, files=files)
		except:
			print("\n---------------------------------------")
			print("\nLINE通知を正常に実行できません")
			print("\nトークン設定を確認してください")
			print("\n---------------------------------------\n")

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