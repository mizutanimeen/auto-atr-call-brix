# Auto-ATR

## 概要
### バージョン v0.1.0
英語の課題として課せられる[ATR-CALL](https://atr.meijo-u.net/)を自動で解いてくれるプロジェクトです。

## 実行

### 必要設定
お手元の環境で`docker`を使えるようにしてください。

`.env`ファイルを`.sample_env`ファイルを参考に`docker-compose.yml`と同じディレクトリに作成してください。

### 実行コマンド
`docker-compose.yml`と同じディレクトリで以下のコマンドを実行してください。
```
docker-compose up -d --build
docker exec -it auto-atr bash
python main.py
```
その後、プロンプト上でクラス、コース、パートを選択してください。

例
```
0 : 2022中村　栄造_水･４限_Pre3-4
1 : 2022中村　栄造_水･４限_中級C-D
クラスを選択してください。
>> 1
0 : 中級C（テスト発音タイプ無し）(SG09)
1 : 中級D（テスト発音タイプ無し）(SG10)
コースを選択してください。
>>
```

### ブラウザで動作を確認
http://localhost:7900/ にアクセスし接続を押せばブラウザ上で動作を確認できます。

このポートはdocker-compose.yml内で定義されているので7900番が使用されている場合は変えてください。他のポートも同様です。

### 中止コマンド（長押し）
```
CTRL + C 
```
中止しても完了したレッスンは保存されます。

## 仕様
### ファイル名
ファイル名 = コース パート 問題形式 .csv
#### コース
コースの後ろについてる(SG00)の様なSG00をファイル名として使う。
- Pre3 -> SG17
#### パート
パート1-5をp1-5と表現
- パート2 -> p2
#### 問題形式
英日と日英は同じ問題だったため同じファイルを使う。
- 単語訳：英日 -> je
- 単語訳：日英 -> je 
- （聴）単語訳 -> li
- （聴）語句並べ替え -> ファイルなし
- 語句並べ替え -> ファイルなし
#### 例
中級C(SG09)パート２単語訳：英日 -> SG09p2je.csv
### 注意点
- 最終的には自分でweb開いて確認してね
- ファイルはプログラム内で自動生成されます。
- 年や先生は区別していないので、もし問題が異なる場合はアップロードされている答えは使い物になりません。恐らく同一の問題だと思われます。

## 答えデータの共有
このプログラムは答えが存在しない場合、１回目間違えながら答えを制作し、２回目から正解していく設計になっています。なので制作した答えを共有すれば他の人がより便利に利用できるようになります。

共有方法としては差分がdata/*.csvのみのプルリクエストを送ってください。

答えが未完成でも前述した通り2回実行すれば完了するので答えの共有は重要ではありますが必須ではありません。

https://blog.mogmet.com/github-abecedarian-send-pull-request/

## 参考URL
- https://qiita.com/ha_ru/items/86dfaae4c92e4a7be13f
- https://pandas.pydata.org/docs/user_guide/index.html#user-guide
- https://blog.mogmet.com/github-abecedarian-send-pull-request/
- https://kurozumi.github.io/selenium-python/api.html#module-selenium.webdriver.remote.webelement

## メモ書き
- pythonの書き方わからん
- printの場所もう少し制限する
- テストスクリプト作る
- 終了判定を実行中の要素取得にした方が時間の自由度上がる
- https://kurozumi.github.io/selenium-python/navigating.html ドラックアンドドロップ
- lesson.pyに含まれているtask関係の関数をtaskに移す
