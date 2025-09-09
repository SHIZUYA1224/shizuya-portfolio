# SHIZUYA Portfolio（Day1-2 スターター）

最小構成のポートフォリオ（黒 × 黄 × 白）。**まずは“公開できる箱”を最短で作る**ことを目的にしたテンプレートです。

## 収録物
- `index.html` … トップページ（単一ページ内に Works / About / Contact セクション）
- `styles.css` … 最小スタイル（ダーク + アクセント黄色）
- `assets/logo.svg` … プレースホルダロゴ（SHI）
- `assets/favicon.png`, `assets/og.png` … プレースホルダ（必要なら差し替え）

## 使い方（ローカル検証）
### 1) ダブルクリック
`index.html` をブラウザで開くだけでも表示できます（ただし一部の機能は `file://` では制限されます）

### 2) 簡易HTTPサーバー
Pythonがあれば以下でローカル配信できます：
```bash
# どちらか
python3 -m http.server 5500
python -m http.server 5500
```
→ http://localhost:5500 を開く

## Git / GitHub Pages 公開（最短）
```bash
# 初回のみ（ユーザー名/メールは自身のものに）
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# リポジトリ初期化
git init
git add .
git commit -m "feat: initial SHIZUYA Day1-2 starter"

# GitHubで新規リポジトリ作成後に（HTTPS例）
git remote add origin https://github.com/<YOUR_ID>/<REPO_NAME>.git
git branch -M main
git push -u origin main
```

### GitHub Pages
- GitHub の **Settings → Pages**
- **“Deploy from a branch”**, Branch: `main`, Folder: `/ (root)` を選択  
- 表示された URL があなたのサイトURLです

## 差し替えポイント
- `index.html` の文言・プロフィール・リンク
- `Works` のカードに実作品の画像/動画リンクを追加
- ロゴ/OG画像/ファビコンをオリジナルに差し替え

---

© SHIZUYA
