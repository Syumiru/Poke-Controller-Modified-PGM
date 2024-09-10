# Poke-Controller-Modified-PGM
ポケコンPGM置き場です。
ポケコン導入済が前提条件です。

更新していただける方がいらっしゃればご連絡ください。
大歓迎です。

## PGM導入手順
1.DL
<br>
ReleasesからSource code(zip)をDL
<br>
2.配置
<br>
解凍後、Poke-Controller-Modified-PGM-x.x.x内のファイルを\Poke-Controller-Modified\SerialController\にコピペして下さい。
<br>

## PGM更新手順
1.バックアップ
<br>
自分で更新したファイルをバックアップする（setting.iniなど）
<br>
2.DL
<br>
ReleasesからSource code(zip)をDL
<br>
3.配置
<br>
解凍後、Poke-Controller-Modified-PGM-x.x.x内のファイルを\Poke-Controller-Modified\SerialController\にコピペして下さい。
<br>
4.差分更新
<br>
バックアップしたsetting.iniの設定などを手動更新してください。
<br>
※古いファイルを上書きすると追加されたini設定項目が消え、PGMが動作しない場合があります。

## PGM共通オプション
setting.iniファイルを確認し必要に応じて変更して下さい。
変更方法の説明はファイル内にあります。

## PGM紹介
### 1.SV_A0_A0S0GACHIGUMA
【概要】
<br>
赫月ガチグマ自動捕獲PGMです。

ini設定に従い以下の個体を捕獲し実数値を確認する作業を繰り返します。
<br>
（サザレに話しかける→ムービー→戦闘→捕獲→（図鑑登録）→捕獲後強さを見てステータス確認→リセットor処理終了）
<br>
捕獲完了後本体をスリープします。
<br>
1.A0-1
<br>
2.A0-1かつS0-1
<br>
1周3分ほどなので1時間で20回捕獲します。
<br>
※A0-1かつS0-1のみを厳選したい方は下記の個体を用意してください。効率化させ以下の作業を繰り返します。
<br>
（ⅰ）（戦闘→すばやさ実数値79のポケモンが先に動けばS0-1の可能性あり→捕獲→捕獲後強さを見てA0-1かステータス確認→リセットor処理終了）
<br>
（ⅱ）（戦闘→すばやさ実数値79のポケモンより先にガチグマが動けばS0-1の可能性なし→リセット）
<br>
<br>
<A0-1かつS0-1厳選時おすすめ個体>
<br>
S0オリーヴァLv.100はなびらのまい冷静こだわりメガネ努力値S16C252残り自由がおすすめです。
<br>
具体的には、S個体値0~5のオリーヴァが必要で最遅S0の場合は努力値をすばやさに20振れば性格冷静ですばやさ実数値79になります。
<br>
S0個体を狙う場合は実数値78にしましょう。
<br>
<br>
S0-1のみを手早く厳選したい方はお修羅さんのPGMがおすすめです。
https://drive.google.com/drive/u/0/folders/1RIktFkyo1QeqIJUd81McMMMUVlyo6F9O
<br>
1周2分ほどでしたので1時間で30回捕獲チャンスがあります。

【オプション】
<br>
**setting.iniファイルを確認し必要に応じて変更して下さい。**
変更方法の説明はファイル内にあります。

【前提】
<br>
**0.settting.iniを確認/環境に合わせて修正することを推奨**します
<br>
**各環境で実数値の画像判定が正しく行われることを確認**してからテストオプションを外すことを推奨します
<br>
1.イベント直前でセーブされていること
<br>
2.ワンパンできるポケモンが先頭
<br>
例：Lv.100カイオーガのしおふき、Lv.100オリーヴァのこだわりメガネはなびらのまい、Lv100ペリッパーのこだわりメガネウェザーボール
<br>
3.日本語ROM
<br>
対象画像を差し替えれば他言語ROMでも動作する想定です。
<br>
※海外言語で厳選を行う方や画像をうまく読み込めない方はTemplateフォルダの画像の書き換えが必須です。
<br>
Templateフォルダ/Syumiru/SV_A0_A0S0GACHIGUMAの画像をPoke-Controllerでキャプチャした自分の画像に書き換えて下さい。
<br>
ペイントアプリなどで吹き出しや文字を切り取り、自分の画像をSV_A0_A0S0GACHIGUMAフォルダに○○.pngと同じ名称で置換して下さい．
<br>
4.設定「手持ち/ボックス」は「自分で選ぶ」を設定（捕獲直後にステータス確認できるようにするため）
<br>
5.手持ちは6匹埋めておく（捕獲直後にステータス確認できるようにするため）

【使用実績】
<br>
A0-1ガチグマ/A0-1かつS0-1ガチグマ（30時間）の捕獲は自己確認しました。
A0-1かつS0-1ガチグマの捕獲は他ユーザー様から10件以上ご報告いただいております。
平均実行時間は60時間ほどです。

【今後の更新予定】
<br>
繫体字とENGLISHの動作確認は行う可能性が高いです。

【Special Thanks】
<br>
お修羅さん（@_Oshura_）のPGMを基に作成させていただきました。

### 2.paojian_c0
【概要】
<br>
C0パオジアン厳選PGMです。厳選判定が完了した段階でPGMがストップします。

【オプション】
<br>
setting.iniファイルを確認し必要に応じて変更して下さい。
変更方法の説明はファイル内にあります。

【前提】
<br>
1.先頭はHP400S204のウイのみもちフワライド
<br>
わざはちからをすいとる/ぶんなげる/おきみやげ
<br>
2.2番目はかえんだまもち攻撃上昇補正6VアメタマLv100
<br>
3.3番目はかえんだまもち攻撃下降補正6VアメタマLv100
<br>
4.4番目はかえんだまもち無補正6VアメタマLv100
<br>
5.5番目はかえんだまもちこんらん無補正6VアメタマLv100
<br>
各アメタマ調整については下記を参照してください。
https://github.com/Syumiru/Poke-Controller-Modified-PGM/issues/9
<br>
3.日本語ROM
<br>
対象画像を差し替えれば他言語ROMでも動作する想定です。

【使用実績】
<br>
日本語ROMで無補正C0パオジアンを捕獲しました。

【今後の更新予定】
<br>
繫体字とENGLISHの動作確認は行う可能性が高いです。

【Special Thanks】
<br>
ひびきさんのPGMを改修しています。

# 免責事項
PGMの利用によって生じた何らかのトラブル・損失・損害等の一切の責任を負いかねますのでご了承ください。
<br>
PGMを利用する場合は、自己責任で行う必要があります。

# 利用規定
当サイトのPGMは以下の場合、ご利用をお断りします。
<br>
1.公序良俗に反する目的での利用
<br>
2.イメージを損なうような攻撃的・差別的・性的・過激な利用
<br>
3.反社会的勢力や違法行為に関わる利用
<br>
4.PGM自体やPGMがインストールされた物品をコンテンツ・商品として再配布・販売
<br>
5.その他著作者が不適切と判断した場合
