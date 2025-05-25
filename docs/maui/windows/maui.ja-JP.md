# 読書の手帖（.NET MAUI版）

![メイン](./images/ja-JP/00.ListWindow.png)

## 1. 説明

本の感想やメモを管理するアプリケーションです。

[.Net 8](https://dotnet.microsoft.com/ja-jp/)をインストールしたWindows 11やAndroidのスマートフォンで動きます。

本のバーコードをカメラで読み取って登録できます。

[読書管理ビブリア](https://biblia978.com/)や[ブクログ](https://booklog.jp/)で作成した記録も読み込めます。

### 1-2. 動機

iPhone SEで読書管理ビブリアを使っていましたが、Pixelに代えたため同じような広告がなく無料で使えるアプリが必要になり作成しました。

読書管理ビブリアでエクスポートしたCsvファイルを既存のアンドロイドアプリ（）に読み込ませれば済んだのですが、以下機能を追加すべく実装することにしました。

- 広告が煩わしい
- 青空文庫の本を登録したい
- 楽天にない本も登録したい
  - なお、楽天ブックスAPIはアプリIDの管理を本アプリ単体で実装できなかったため利用していません

## 2. 使い方

**読書の手帖**を起動したら、本の記録を登録します。

記録が終わったら、**読書の手帖**を終了します。

### 2-1. 読書の手帖を起動する

Windowsのスタートアップ等から、**読書の手帖（Book Techyo）** をクリックして起動します。

![スタートアップ](./images/ja-JP/01.Start.png)

<!-- TODO 他の位置へ
### 2-2. 手帖ファイルを新規作成する、もしくは読み込む

**読書の手帖**のメニュー **ファイル** / **新規作成** をクリックし、新しく手帖ファイルを作成します。

![CreateNew](./images/ja-JP/02.CreateNew.png)

すると**読書の手帖**は本の記録がない画面を表示します。

![New](./images/ja-JP/03.New_ListWindow.png)

もしくは、**読書の手帖**のメニュー **ファイル** / **開く** をクリックし、以前に作成した手帖ファイルを読み込みます。

![Open](./images/ja-JP/04.Open.png)

すると**読書の手帖**は以前に作成した本の記録を表示します。

![Opened](./images/ja-JP/05.Opened_ListWindow.png) 
-->

### 2-3. 本の記録を登録する

**読書の手帖**の![+アイコン](../common/images/add_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

![Add](./images/ja-JP/06.Add_add.png)

![+アイコン](../common/images/add_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、バーコード読み取り ![バーコード読み取り](../common/images/barcode_scanner_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)、書籍のタイトルで検索 ![書籍のタイトルで検索](../common/images/title_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)、空の記録を追加 ![空の記録を追加](../common/images/draft_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)を表示します。

![Add Sub](./images/ja-JP/06-01.Add_sub.png)

<!-- 本の記録がある場合は、一番上の記録をクリックしてから、**読書の手帖**のメニュー **編集** / **追加** / **上に追加** もしくは **下に追加** をクリックします。

![Add](./images/ja-JP/07.Add_above.png) 

**読書の手帖**は、本の記録を入力する詳細画面を表示します。タイトルや著者等を入力して、OKボタンを押下すると本の記録を登録完了できます。

![Adding](./images/ja-JP/08.Adding_DetaiWindow.png)

-->

#### 2-3-1. バーコード読み取り

バーコード読み取り ![バーコード読み取り](../common/images/barcode_scanner_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、バーコード読み取り画面を表示します。

![CameraRecognizing](./images/ja-JP/13.CameraRecognizing.png)

書籍のバーコード（978で始まる数学が書いてある方）をカメラにかざし、読み取りが成功するまで位置を調整してください。

カメラ画像左上の数字は読み取りを行った回数を示します。

カメラ画像の下にあるスキャン間隔を増減すると読み取りを試みる単位時間当たりの回数を変更できます。
間隔を小さくしたほうが早く読み取りに成功する可能性が増えますが、負荷が増えます。

<!-- TODO 許可を表示するかも -->

バーコードの読み取りに成功すると、**読書の手帖**は読み取ったISBNを使って検索を行い結果を表示します。

![Barcord Scaned ISBN Search](./images/ja-JP/13-01.barcordScanedSearch.png)

一覧で書籍を選択して ダブルクリックしてください。

**読書の手帖**は、本の記録を入力する詳細画面に検索結果を反映します。

![Barcord Scaned Detail](./images/ja-JP/13-02.barcordScanedDetail.png)

項目に入力して、![apply](../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は一覧に登録します。

#### 2-3-2. 書籍のタイトルをキーにしてインターネットを検索する

![書籍のタイトルで検索](../common/images/title_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、検索画面を表示します。

![Search](./images/ja-JP/09.SearchingByTitle.png)

テキストボックスに検索する書籍のタイトルを入力して![検索開始ボタン](../common/images/search_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は検索を行い結果を一覧で表示します。

なお、検索で利用するサービスおよびサービスごとの検索結果の上限数は[設定画面](#3-設定)で指定します。

![Search Results](./images/ja-JP/09-1.SearchingByTitleResults.png)

一覧で書籍を選択して ダブルクリックしてください。

**読書の手帖**は、本の記録を入力する詳細画面に検索結果を反映します。

![Search Detail](./images/ja-JP/09-2.SearchingByTitleDetail.png)

項目に入力して、![apply](../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は一覧に登録します。

#### 2-3-3. 空の記録を追加する

![空の記録を追加](../common/images/draft_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、空の本の記録を入力する詳細画面を表示します。

![Draft](./images/ja-JP/10.Draft.png)

項目に入力して、![apply](../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は一覧に登録します。

### 2-4. 本の記録を編集する

**読書の手帖**で編集する記録を選択すると、本の記録を入力する詳細画面を表示します。

![Editing](./images/ja-JP/15.Editing.png)

変更して、![apply](../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、変更した内容を反映した画面を表示します。

![Edited](./images/ja-JP/16.Edited.png)

### 2-6. 読書の手帖を終了する

**読書の手帖**の右上側にある×ボタンをクリックするか、タスクバーの**読書の手帖**を右クリックして表示したメニューから[ウィンドウを閉じる]をクリックします。

![Exit](./images/ja-JP/18.Exit.png)

この時、**読書の手帖**は**未保存の変更を破棄します**ので注意してください。

## 3. 設定

**読書の手帖**の左上にある![menu](../common/images/menu_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックして、表示したメニューから[設定]をクリックすると、設定画面を表示します。

![Shell](./images/ja-JP/19.Shell.png)

![Configuration](./images/ja-JP/20.Configuration.png)

設定画面には上から

- 書籍検索サービスを利用する・しない、および優先度の指定
- 各書籍検索サービスで取得する結果の上限個数
- アプリ設定を開くボタン

があります。

### 3-1. 書籍検索サービスを利用する・しない、および優先度の指定

左側のチェックボックスにチェックがある検索サービスを使って書籍検索を行います。

全部チェックを外すと検索を行いません。

上にあるサービスから順番に検索を行います。

検索サービスの右側に![バーコード](../common/images/barcode_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)がグレーでない色になっていればISBNでの検索時に利用します。![書籍のタイトルで検索](../common/images/title_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)がグレーでない色になっていれば書籍タイトルでの検索時に利用します。

### 3-2. 各書籍検索サービスで取得する結果の上限個数

3以上100以下の整数を指定します。

### 3-3. アプリ設定を開くボタン

クリックするとアプリ設定の画面を表示します。

![AppSettings](./images/ja-JP/21.AppSettings.png)

## 4. バックアップと保存

---
