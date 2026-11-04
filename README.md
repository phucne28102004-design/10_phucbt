# 旅トモ｜旅行プラン相談アプリ

友達や家族との旅行について、行き先・日数・予算・同行者・興味を選ぶと、おすすめの観光プランを提案するWebアプリです。

## 使用技術
- Python
- Flask
- HTML / CSS
- 外部API・APIキー不要

## ファイル構成
- `app.py`：入力内容を受け取り、旅行プランを作成する処理
- `requirements.txt`：必要なPythonライブラリ
- `templates/index.html`：入力フォームと結果画面
- `static/style.css`：画面デザイン
- `render.yaml`：Renderの公開設定

## ローカルで実行
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
ブラウザで http://127.0.0.1:5000 を開きます。

## GitHubへアップロード
1. ZIPを解凍します。
2. 中にある `app.py` などのファイルとフォルダをGitHubリポジトリの一番上にアップロードします。
3. `templates` と `static` フォルダもそのままアップロードします。

## Renderで公開
1. Renderにログインし、「New +」→「Web Service」を選びます。
2. GitHubリポジトリを接続します。
3. Build Command：`pip install -r requirements.txt`
4. Start Command：`gunicorn app:app`
5. 「Deploy」を押し、公開URLを開きます。

このアプリはサンプルデータから提案するため、APIキーや有料サービスは必要ありません。
