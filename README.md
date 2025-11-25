# PromptVault

プロンプト管理で悩まない、Pythonで作ったツール。

- Ctrl+S で今見てるプロンプトを即保存
- 検索即反映
- 削除アニメ付き
- JSONエクスポート付き
- ローカルで完結（クラウド不要）

## プロジェクト構造

```
/
promptvault/
├── app.py                # FastAPI（Python）
├── templates/index.html  # HTMX + Tailwind
├── static/style.css      # tailwindcssを利用しているので空白
├── prompts.db            # SQLite（1ファイルで完結）
└──  ChromeExt
　　　├── save_prompt.js        # Chrome拡張
　　　└── manifest.json         # Chrome拡張

```

今後追加したい機能
- 1クリックコピー
- 自動保存  
- 1クリック圧縮
- 1クリック最適化（自動で新バージョン保存）  
- 使用頻度ランキング  
- バージョン履歴（親子関係でツリー表示も後で追加可）  
- A/B比較（2つ並べればOK）

Python環境: Python 3.8以上がインストールされていることを確認します。

依存関係のインストール: 以下のコマンドで必要なライブラリをインストールします。

Bash

pip install fastapi uvicorn jinja2 python-multipart

起動コマンド

bash

uvicorn app:app --reload --port=8000
