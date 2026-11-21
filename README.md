# さいとーの部屋

日記と音楽の記録を少しずつ置いていく、公開型の小さな個人サイト。

**Webサイト:** https://kuukiyomeyo.github.io/saito-room/

## 構成

- `index.html`：玄関。日記・音楽棚への入口と最新更新
- `diary.html`：日記の一覧
- `music.html`：アルバムレビューと音楽ノートの一覧
- `_layouts/default.html`：全ページ共通のメニューとフッター
- `_layouts/post.html`：記事本文のレイアウト
- `style.css`：共通の見た目
- `_config.yml`：Jekyllの設定
- `templates/`：記事作成用のひな形（サイトには掲載されない）

GitHub Pagesの標準機能であるJekyllを利用。記事を増やすと一覧とトップの新着欄が自動更新されます。

## 記事を追加する（AI運営の基本）

1. 日記や音楽の感想をさいとーが用意する。
2. ChatGPTが文章を整えて確認用の案を作る。事実や本人の意見を勝手に作らない。
3. さいとーが「この内容で掲載して」と承認する。
4. ChatGPTが `_posts/YYYY-MM-DD-english-slug.md` というファイルを追加する。
5. `main` ブランチへの変更がGitHub Pagesに反映される。

記事のひな形は `templates/diary-example.md` と `templates/music-album-example.md` と `templates/music-note-example.md` にあります。

### 記事に必要な設定例

日記：

```yaml
---
title: "今日のこと"
date: 2026-11-22 12:00:00 +0900
section: diary
categories: [diary]
description: "日記の紹介"
---
```

アルバム感想：

```yaml
---
title: "作品名について"
date: 2026-11-22 12:00:00 +0900
section: music
categories: [music]
kind: album
artist: "アーティスト名"
release_year: "発売年"
description: "レビューの紹介"
---
```

音楽についての自由な文章では `kind: note` にします。日付は記事の実際の日付に変更。

## 運営方針

- コメント、いいね、フォロー、閲覧カウンターは設置しない。
- 個人の評価や日記の内容は、本人の言葉を尊重する。
- 下書きや個人情報を公開リポジトリへ置かない。**作業用ブランチも公開リポジトリでは誰でも見られる**ため、機密の下書きは禁止。
- ファイルを追加・変更する前には公開範囲と本人の承認を確認する。
- アルバムジャケットや歌詞は権利を確認せずコピーしない。
- 「更新しなければならない」というルールは作らない。
