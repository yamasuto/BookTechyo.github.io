# 読書の手帖（.NET MAUI版）

![メイン](./images/ja-JP/00.ListWindow.png)

## 1. 説明

本の感想やメモを管理するアプリケーションです。

[.Net 9](https://dotnet.microsoft.com/ja-jp/)をインストールしたWindows 11[^0]やAndroid[^2]のスマートフォンで動きます。

本のバーコードをカメラで読み取って登録できます。

[読書管理ビブリア](https://biblia978.com/)や[ブクログ](https://booklog.jp/)で作成した記録も読み込めます。

### 1-1. 作成した理由

iPhone SE[^1]で読書管理ビブリアを使っていましたが、Google Pixel[^2]に代えたため同じような広告がなく無料で使えるアプリが必要になり作成しました。

読書管理ビブリアでエクスポートしたCsvファイルを既存のアンドロイドアプリ（[Yomoo](https://play.google.com/store/apps/details?id=com.nosuke.yomoo&hl=ja)、[bondaviの記録](https://play.google.com/store/apps/details?id=jp.bondavi.likes.global&hl=ja)、[蔵書マネージャー](https://play.google.com/store/apps/details?id=com.bsy_web.bookmanager&hl=ja)、等）に読み込ませれば済んだのですが、以下解消したり、機能を追加すべく実装することにしました。

- 広告が煩わしい
- 不具合が直らない
- 青空文庫の本を登録したい
- 楽天にない本も登録したい
  - なお、楽天ブックスAPIはアプリIDの管理を本アプリ単体で実装できなかったため利用していません

## 2. 使い方

**読書の手帖**を起動したら、本の記録を登録します。

記録が終わったら、**読書の手帖**を終了します。

### 2-1. 読書の手帖を起動する

Windowsのスタートアップ等から、**読書の手帖（Book Techyo）** ![icon](../../../note.png)をクリックして起動します。

![スタートアップ](./images/ja-JP/01.Start.png)

### 2-2. 本の記録を登録する

**読書の手帖**の![+アイコン](../../common/images/add_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

![Add](./images/ja-JP/06.Add_add.png)

![+アイコン](../../common/images/add_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、バーコード読み取り ![バーコード読み取り](../../common/images/barcode_scanner_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)、書籍のタイトルで検索 ![書籍のタイトルで検索](../../common/images/title_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)、空の記録を追加 ![空の記録を追加](../../common/images/draft_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)を表示します。

![Add Sub](./images/ja-JP/06-01.Add_sub.png)

#### 2-2-1. バーコード読み取り

バーコード読み取り ![バーコード読み取り](../../common/images/barcode_scanner_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

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

項目に入力して、![apply](../../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は一覧に登録します。

#### 2-2-2. 書籍のタイトルをキーにしてインターネットを検索する

![書籍のタイトルで検索](../../common/images/title_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、検索画面を表示します。

![Search](./images/ja-JP/09.SearchingByTitle.png)

テキストボックスに検索する書籍のタイトルを入力して![検索開始ボタン](../../common/images/search_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は検索を行い結果を一覧で表示します。

なお、検索で利用するサービスおよびサービスごとの検索結果の上限数は[設定画面](#3-設定)で指定します。

![Search Results](./images/ja-JP/09-1.SearchingByTitleResults.png)

一覧で書籍を選択して ダブルクリックしてください。

**読書の手帖**は、本の記録を入力する詳細画面に検索結果を反映します。

![Search Detail](./images/ja-JP/09-2.SearchingByTitleDetail.png)

項目に入力して、![apply](../../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は一覧に登録します。

#### 2-2-3. 空の記録を追加する

![空の記録を追加](../../common/images/draft_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、空の本の記録を入力する詳細画面を表示します。

![Draft](./images/ja-JP/10.Draft.png)

項目に入力して、![apply](../../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、**読書の手帖**は一覧に登録します。

### 2-3. 本の記録を編集する

**読書の手帖**で編集する記録を選択すると、本の記録を入力する詳細画面を表示します。

![Editing](./images/ja-JP/15.Editing.png)

変更して、![apply](../../common/images/check_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

**読書の手帖**は、変更した内容を反映した画面を表示します。

![Edited](./images/ja-JP/16.Edited.png)

なお、詳細画面で![Delete](../../common/images/delete_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると記録を破棄します。

### 2-4. 本の記録を検索する

文字列検索または状態を対象にして検索できます。

<!-- タグも選択できるようにしたい -->

#### 2-4-1. タイトル等を対象として検索する

タイトル、著者、説明、感想を対象として、指定した文字列を含む本の記録を検索します。

![FilterByText](./images/ja-JP/17-1.FilterByText.png)

検索文字列を指定するテキストボックスに文字列を入力し、ENTERキーを押下するか、![search](../../common/images/search_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

見つかった記録のみ一覧に表示します。

検索結果の表示をキャンセルする場合は、![Cancel](../../common/images/cancel_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

#### 2-4-2. 状態フィルター

**読書の手帖**の右上側にある![Filter](../../common/images/filter_alt_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックすると、下側に状態フィルターを示します。

チェックありの状態だけを一覧に表示します。

![BottomSheet](./images/ja-JP/17-2-1.FilterByStatus.png)

状態をクリックしてチェックありなしを切り替えると、一覧に表示している本の記録を更新します。

![BottomSheet changed](./images/ja-JP/17-2-2.FilterByStatus.png)

状態フィルターを閉じる場合は、右上の![Cancel](../../common/images/cancel_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックします。

![BottomSheet Closed](./images/ja-JP/17-2-3.FilterByStatus.png)

### 2-5. 読書の手帖を終了する

**読書の手帖**の右上側にある![Close](../../common/images/close_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックするか、タスクバーの**読書の手帖**を右クリックして表示したメニューから[ウィンドウを閉じる]をクリックします。

![Exit](./images/ja-JP/18.Exit.png)

この時、**読書の手帖**は**未保存の変更を破棄します**ので注意してください。

## 3. 設定

**読書の手帖**の左上にある![menu](../../common/images/menu_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックして、表示したメニューから[設定]をクリックすると、設定画面を表示します。

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

検索サービスの右側に![バーコード](../../common/images/barcode_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)がグレーでない色になっていればISBNでの検索時に利用します。![書籍のタイトルで検索](../../common/images/title_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)がグレーでない色になっていれば書籍タイトルでの検索時に利用します。

### 3-2. 各書籍検索サービスで取得する結果の上限個数

3以上100以下の整数を指定します。

### 3-3. アプリ設定を開くボタン

クリックするとアプリ設定の画面を表示します。

![AppSettings](./images/ja-JP/21.AppSettings.png)

## 4. バックアップと保存

**読書の手帖**の左上にある![menu](../../common/images/menu_32dp_1F1F1F_FILL0_wght400_GRAD0_opsz40.png)をクリックして、表示したメニューから[バックアップと復元]をクリックすると、バックアップと復元画面を表示します。

![Shell](./images/ja-JP/19.Shell.png)

![BackupRestore](./images/ja-JP/22.backupRestore.png)

バックアップと復元画面には上から

- バックアップボタン
- 復元ボタン
- すべて削除ボタン
- 他のサービス
  - ビブリア
    - インポートボタン
    - エクスポートボタン
  - ブクログ
    - インポートボタン

があります。

### 4-1. バックアップボタン

クリックすると指定したファイルに、登録した本の記録をYamlで出力します。

### 4-2. 復元ボタン

クリックすると指定したファイルを読み込み本の記録を**追加**します。

既存の登録をすべて削除してから読み込む場合は、[登録してある記録を空にしてから復元する]チェックボックスをチェックしてからボタンをクリックしてください。

### 4-3. すべて削除ボタン

クリックすると登録している本の記録をすべて削除します。

### 4-4. 他のサービス

### 4-4-1.  ビブリア

- インポート：[読書管理ビブリア](https://biblia978.com/)のバックアップでDropboxに出力した[CSVファイル](https://biblia978.com/support/articles/15/)をインポートします。
- エクスポート：登録した本の記録を[読書管理ビブリア](https://biblia978.com/)の復元で読み込める[CSVファイル](https://biblia978.com/support/articles/15/)としてエクスポートします。

読書管理ビブリアのバックアップは[Dropbox](https://www.dropbox.com/)にファイルを作成します。復元はDropboxにあるファイルを読み込みます。**読書の手帖**はDropboxにアクセスできないため、私はWindowsにインストールした[Dropbox Lite](https://apps.microsoft.com/detail/9WZDNCRFJ0PK?hl=ja&gl=JP&ocid=pdpshare)アプリを使い以下のように操作しています。

- **読書の手帖**でインポートする
  1. 読書管理ビブリアでバックアップを行う
  2. Dropbox Liteを起動する（読書管理ビブリアでのDropboxと同じアカウント）
  3. Dropbox Liteで「Dropbox/アプリ/Biblia/books.csv」を選択して「名前をつけて保存」でWindowsのローカルフォルダー（ドキュメントフォルダー等）に出力
  4. **読書の手帖**で、[すべて削除]を行ってのち、先に保存したCSVファイルをインポートする

- **読書の手帖**でエクスポートして、読書管理ビブリアで復元する
  1. **読書の手帖**の[ビブリア] [エクスポート]でファイル名にbooks.csvを指定して保存する
  2. Dropbox Liteで「Dropbox/アプリ/Biblia」に上のbooks.csvをアップロードする
  3. 読書管理ビブリアで「すべてのデータを削除」を行ってのち、復元を実行する

### 4-4-2. ブクログ

- インポート：ウェブ版[ブクログ](https://booklog.jp/)のエクスポートで出力した[CSVファイル](https://booklog.zendesk.com/hc/ja/articles/360048930533-%E4%BB%96%E3%81%AE%E8%AA%AD%E6%9B%B8%E7%AE%A1%E7%90%86%E3%82%B5%E3%82%A4%E3%83%88%E3%81%8B%E3%82%89%E3%83%96%E3%82%AF%E3%83%AD%E3%82%B0%E3%81%B8%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92%E7%A7%BB%E8%A1%8C%E3%81%97%E3%81%9F%E3%81%84%E3%81%A7%E3%81%99)をインポートします。

---

[^0]: Windows及び関連する名称並びにそれぞれのロゴは、米国Microsoft Corporationの米国およびその他の国における登録商標です。
[^1]: iPhoneはApple inc.の登録商標です。iPhone商標は、アイホン株式会社のライセンスに基づき使用されています。
[^2]: 「Google」「Google Pixel」「Android」は、Google LLCの商標または登録商標です。
