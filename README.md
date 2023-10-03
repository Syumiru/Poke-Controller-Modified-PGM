# Poke-Controller-Modified-PGM
ポケコンPGM置き場です。
ポケコン導入済が前提条件です。

更新していただける方がいらっしゃればご連絡ください。
大歓迎です。

【PGM導入方法】
<br>
2通りあります。
<br>
方法①
<br>
右上緑色のcode→（codespacrタブが開かれている場合は）local→Download ZIPを押下しDL
<br>
\Poke-Controller-Modified\SerialController\にコピペして下さい。
<br>
方法②
<br>
ReleasesからSource code(zip)をDL
<br>
解凍後、Poke-Controller-Modified-PGM-x.x.x内のファイルを\Poke-Controller-Modified\SerialController\にコピペして下さい。

【PGM共通オプション】
<br>
iniファイルを確認し必要に応じて変更して下さい。
<br>
◆プログラム開始前に確認していただきたいこと（PC側でのチェック項目）e.g.SV_A0_A0S0GACHIGUMA
<br>
・SV_A0_A0S0GACHIGUMA.pyをPoke-Controller-Modified/SerialController/Commands/PythonCommandsのImageProcessingOnlyフォルダに入れます。
<br>
・Syumiruフォルダをフォルダ状態のままPoke-Controller-Modified/SerialControllerのTemplateフォルダに入れます。
<br>
※海外言語で厳選を行う方や画像をうまく読み込めない方はTemplateフォルダの画像の書き換えが必須です。
<br>
Templateフォルダ/Syumiru/SV_A0_A0S0GACHIGUMAの画像をPoke-Controllerでキャプチャした自分の画像に書き換えて下さい。
<br>
ペイントアプリなどで吹き出しや文字を切り取り、自分の画像をSV_A0_A0S0GACHIGUMAフォルダに○○.pngと同じ名称で保存して下さい．


## PGM紹介
### 1.SV_A0_A0S0GACHIGUMA
【概要】
<br>
赫月ガチグマ自動捕獲PGMです。

以下の個体を捕獲し実数値を確認する作業を繰り返します。
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
※A0-1かつS0-1のみを厳選したい方は効率化させ以下の作業を繰り返します。
<br>
（ⅰ）（戦闘→すばやさ実数値78のポケモンが先に動けばS0-1の可能性あり→捕獲→捕獲後強さを見てA0-1かステータス確認→リセットor処理終了）
<br>
（ⅱ）（戦闘→すばやさ実数値78のポケモンより先にガチグマが動けばS0-1の可能性なし→リセット）
<br>
A0-1かつS0-1厳選を両立したい方は最遅S0オリーヴァLv.100性格冷静の努力値S16C252残り自由をご用意下さい。
（A0-1かつS0-1厳選用にすばやさ実数値78のオリーヴァLv.100最遅の個体を用意すること。）
<br>
具体的には、S個体値0~4のオリーヴァが必要で最遅S0の場合は努力値をすばやさに16振れば性格冷静ですばやさ実数値78になります。
<br>
オリーヴァLv.100にこだわりメガネを持たせ一番上の技をはなびらのまいにすることで、冷静のC特化でガチグマもワンパンできます。
<br>
S0-1のみを手早く厳選したい方はお修羅さんのPGMがおすすめです。
https://drive.google.com/drive/u/0/folders/1RIktFkyo1QeqIJUd81McMMMUVlyo6F9O
<br>
1周2分ほどでしたので1時間で30回捕獲チャンスがあります。

【オプション】
<br>
iniファイルを確認し必要に応じて変更して下さい。

【前提】
<br>
1.イベント直前でセーブされていること
<br>
2.ワンパンできるポケモンが先頭
<br>
例：Lv.100カイオーガのしおふき、Lv.100オリーヴァのこだわりメガネはなびらのまい
<br>
3.日本語ROM
<br>
対象画像を差し替えれば他言語ROMでも動作する想定です。
<br>
4.設定「手持ち/ボックス」は「自分で選ぶ」を設定（捕獲直後にステータス確認できるようにするため）
<br>
5.手持ちは6匹埋めておく（捕獲直後にステータス確認できるようにするため）

【使用実績】
<br>
A0-1ガチグマ/A0-1かつS0-1ガチグマ（30時間）の捕獲は自己確認しました。
A0-1かつS0-1ガチグマの捕獲は他ユーザー様から2例ご報告いただいております。
45時間or100時間以上かかったそうです。

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
iniファイルを確認し必要に応じて変更して下さい。

【前提】
<br>
1.先頭はHP400S204のウイのみもちフワライド
<br>
わざはちからをすいとる/ぶんなげる/おきみやげ
<br>
2.2番目はかえんだまもち攻撃上昇補正6VアメタマLv100(努力値はなし)
<br>
3.3番目はかえんだまもち攻撃下降補正6VアメタマLv100(努力値はなし)
<br>
4.4番目はかえんだまもち無補正6VアメタマLv100(努力値はなし)
<br>
5.5番目はかえんだまもちこんらん無補正6VアメタマLv100(努力値はなし)
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
