# PromptVault: ローカル完結型 プロンプト管理ツール

AI時代におけるプロンプト管理。ローカルで安全、爆速でプロンプトを記録・検索・管理できます。

## 主な特徴とメリット

* 爆速保存: `Ctrl + S` で今見ているプロンプトを即座に保存。
* ローカル完結: クラウドサービスは不要。すべてのデータ（SQLite）はあなたのローカル環境で安全に管理されます。
* リアルタイム検索: 入力と同時に検索結果に即反映されるUIで、目的のプロンプトをすぐに見つけられます。
* クリーンなUI: HTMXとTailwind CSSによるシンプルでモダンなインターフェース。
* JSONエクスポート: 簡単にプロンプトデータをバックアップ・移行可能。

プロジェクト構造と技術スタック技術スタック (Tech Stack)
* 役割技術特徴バックエンドPython (FastAPI)高速でモダンなAPI構築フレームワーク
* フロントエンドHTMX + Tailwind CSSMinimalなJavaScriptで動的なUIを実現
* データベースSQLite (prompts.db)シングルファイルで管理が容易

## プロジェクト構造と技術スタック

### 技術スタック (Tech Stack)

| 役割 | 技術 | 特徴 |
| :--- | :--- | :--- |
| **バックエンド** | Python (FastAPI) | 高速でモダンなAPI構築フレームワーク |
| **フロントエンド** | HTMX + Tailwind CSS | MinimalなJavaScriptで動的なUIを実現 |
| **データベース** | SQLite (`prompts.db`) | シングルファイルで管理が容易 |

## プロジェクト構造

```
/
promptvault/
├── app.py                # FastAPI（Python）
├── index.html            # HTMX + Tailwind
├── style.css             # tailwindcssを利用しているので空白
├── prompts.db            # SQLite（1ファイルで完結）
└──  ChromeExt
　　　├── save_prompt.js        # Chrome拡張
　　　└── manifest.json         # Chrome拡張

```

## 環境構築と利用開始 (Getting Started)

### 1. リポジトリのクローン

```bash
git clone [https://github.com/tugaa360/promptvault.git](https://github.com/tugaa360/promptvault.git)
cd promptvault
2. 依存関係のインストール
Python 3.8以上が必要です。仮想環境の利用を推奨します。

Bash

# 依存ライブラリのインストール
pip install fastapi uvicorn jinja2 python-multipart
3. アプリケーションの起動
Bash

uvicorn app:app --reload --port=8000
起動後、ブラウザで http://127.0.0.1:8000 にアクセスしてください。
```

Chrome拡張機能の利用
この拡張機能（ChromeExtフォルダ内）を使うと、どのWebページからでもプロンプトを素早く保存し、ローカルのPromptVaultに送信できます。

インストール方法 (デベロッパーモード)
Chromeの拡張機能管理ページ（chrome://extensions/）を開きます。

画面右上の 「デベロッパーモード」 をオンにします。

「パッケージ化されていない拡張機能を読み込む」 をクリックし、リポジトリ内の ChromeExt フォルダを選択します。


今後追加したい機能
- 1クリックコピー
- 自動保存  
- 1クリック圧縮
- 1クリック最適化（自動で新バージョン保存）  
- 使用頻度ランキング  
- バージョン履歴（親子関係でツリー表示も後で追加可）  
- A/B比較（2つ並べればOK）


---

## 🛠️ 環境構築と利用開始 (Getting Started)

### 1. リポジトリのクローン

```bash
git clone [https://github.com/tugaa360/promptvault.git](https://github.com/tugaa360/promptvault.git)
cd promptvault
2. 依存関係のインストール
Python 3.8以上が必要です。仮想環境の利用を強く推奨します。

Bash

# 依存ライブラリのインストール
pip install fastapi uvicorn jinja2 python-multipart
3. アプリケーションの起動
Bash

uvicorn app:app --reload --port=8000
起動後、ブラウザで http://127.0.0.1:8000 にアクセスしてください。

```

🔌 Chrome拡張機能の利用
リポジトリ内の ChromeExt フォルダに含まれる拡張機能を利用すると、どのWebページからでもプロンプトを素早く保存し、PromptVaultに送信できます。

インストール方法 (デベロッパーモード)
Chromeの拡張機能管理ページ（chrome://extensions/）を開きます。

画面右上の 「デベロッパーモード」 をオンにします。

「パッケージ化されていない拡張機能を読み込む」 をクリックし、リポジトリ内の ChromeExt フォルダを選択します。

使用方法
保存したいテキストを選択し、Ctrl+Sを押すことで、PromptVaultの保存ダイアログが開きます。



🛣️ 今後の計画 (Roadmap)
1クリックコピー

自動保存

1クリック最適化（自動で新バージョン保存）

使用頻度ランキング

バージョン履歴・A/B比較機能

📄 ライセンス
MIT License
