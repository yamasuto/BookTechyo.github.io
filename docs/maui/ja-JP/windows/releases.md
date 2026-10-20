# リリース履歴

## 1.3.0

- WIP ファイルから読みたい本を登録する
- [SQLITEの脆弱性対応（Android用のパッケージに脆弱性があった）](https://github.com/yamasuto/ReadingNotes.Maui/issues/35)
- [バックアップファイル読み込みでレコードの表示順が逆転する不具合を修正しました。](https://github.com/yamasuto/ReadingNotes.Maui/issues/38)
- Web検索のタイムアウトを10秒から60秒に変更しました。
- Web検索の取得する結果の上限個数の範囲を3以上1000以下に変更しました。
- Web検索の結果を見つかった時に表示するように修正しました。検索結果表示に`yidld return`を使うようにしました。
- [Web検索結果に巻次・部編番号がある場合は、書籍タイトルに巻次・部編番号を表示するように修正しました。](https://github.com/yamasuto/ReadingNotes.Maui/issues/48)
- [設定画面画面のデザインを変更して、項目を追加しました。併せて読書の手帳について画面もデザインを変更しました。](https://github.com/yamasuto/ReadingNotes.Maui/issues/50)
- フィルターと並び替えのシートで、ボタンの位置を上部に移動しました。
- フィルターと並び替えのシートは、最大で表示するように変更しました。
- [[Android] 説明、感想の入力ページで適用ボタンの位置を変更しました（隠れることがあるのを回避）。](https://github.com/yamasuto/ReadingNotes.Maui/issues/41)

## 1.2.0

- **.NET 10**
- パッケージのアップグレード
- パフォーマンス改善
- 誤字訂正
- バーコード読み取りにWindowsのOCR（Windows.Media.Ocr API）も利用するようにしました。
- ISBN検索・タイトル検索の検索方法の判定を変更しました。
- NDLのデータプロバイダー `国立国会図書館新着書誌情報`（iss-ndl-opac-inprocess）を書籍検索サービスに追加しました。
- フィルターに読了年を追加しました。
- 賞のフィルターのオン・オフ切り替えを簡単にしました。
- 登録書籍検索文字列・フィルター・並び替え条件を保存して、次回起動時に復元するようにしました。

## 1.1.0

- 復元、インポートで表示するファイル選択ダイアログで拡張子を限定するように変更しました。
- バーコード読み取りで使うZXing.Netを0.16.11に更新しました。
- アプリのcsprojファイルのPropertyGroupにSelfContainedとRuntimeIdentifierを追加し、それぞれtrue、win-x64を指定することで.NET ランタイムを同梱するように変更しました。

## 1.0.0

- 初回リリース
