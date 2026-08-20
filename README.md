# tzuen-website

財團法人佛教慈恩育幼基金官方網站原始碼。

- 正式中文名稱：`財團法人佛教慈恩育幼基金`
- 正式英文名稱：`Buddhist Tzuen Children’s Welfare Foundation`
- 預定網域：`tzuen.org`
- 網站語言：繁體中文、英文
- 技術：HTML、CSS、JavaScript

本網站目前採用無框架的靜態架構，沒有資料庫與後端服務，適合部署到 GitHub Pages、Cloudflare Pages、Vercel 或其他靜態網站服務。

## 專案功能

- 中英文切換，並使用 `localStorage` 保存語言選擇。
- 基金會介紹與服務內容。
- 七項服務的預計辦理月份或期間。
- 立案證書與法人登記證明。
- 捐款、電子發票愛心碼與郵政劃撥資訊。
- 電話、Email、Facebook、地址與 Google Maps。
- 桌機、平板與手機響應式版面。
- Playwright 桌機與手機瀏覽器測試。

## 專案結構

```text
Tzuen/Website/
├── index.html                 # 網站 HTML 結構
├── styles.css                 # 品牌樣式與響應式版面
├── app.js                     # 雙語內容、服務卡片與互動功能
├── package.json               # 測試與建置指令
├── README.md                  # 專案使用及維護說明
├── AGENTS.md                  # AI Agent 每次工作時應遵守的資訊
├── implementation.md          # 網站規格、決策與實作進度
├── public/
│   ├── images/                # 最佳化後的 Logo 與活動照片
│   └── documents/             # 最佳化後的證書圖片
├── resource/
│   ├── Tzuen_Intro.md         # 基金會內容來源，可留在 Git
│   └── assets/                # 原始高解析素材，只留本機、不公開
├── scripts/
│   ├── build.mjs              # 建立可部署的 dist 目錄
│   └── create_slogan.py       # 早期 slogan 圖片處理工具
├── tests/
│   ├── site.test.mjs          # 靜態結構與內容測試
│   ├── browser_check.py       # Playwright 瀏覽器測試
│   └── screenshots/           # 測試截圖，不納入 Git
└── dist/                      # 建置結果，不納入 Git
```

## 環境需求

- Node.js 20 以上版本。
- npm。
- Python 3。
- 現代瀏覽器。

只有修改 HTML、CSS 或文字時，不需要安裝額外 npm 套件。

## 第一次使用

進入專案目錄：

```bash
cd Tzuen/Website
```

執行靜態測試：

```bash
npm test
```

建立可部署版本：

```bash
npm run build
```

建置完成後，網站會輸出到 `dist/`。

## 本機預覽

在專案目錄執行：

```bash
python3 -m http.server 4173
```

瀏覽器開啟：

```text
http://127.0.0.1:4173
```

結束伺服器時，在終端機按 `Control + C`。

## Playwright 瀏覽器測試

專案的 Playwright 安裝在 `.venv`，Chromium 安裝在 `.playwright-browsers`。這兩個目錄都不會提交到 Git。

若尚未建立測試環境：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install playwright pillow
PLAYWRIGHT_BROWSERS_PATH=.playwright-browsers .venv/bin/python -m playwright install chromium
```

先在第一個終端機啟動網站：

```bash
cd Tzuen/Website
python3 -m http.server 4173
```

再於第二個終端機執行：

```bash
cd Tzuen/Website
PLAYWRIGHT_BROWSERS_PATH=.playwright-browsers .venv/bin/python tests/browser_check.py
```

測試內容包括：

- 1440 × 1000 桌機版。
- 390 × 844 手機版。
- 中英文切換與語言保存。
- 手機導覽選單。
- 圖片與證書是否載入。
- 七項服務是否顯示。
- 頁面是否產生水平溢位。
- JavaScript runtime error。

測試成功時會顯示：

```text
Browser checks passed for desktop and mobile.
```

## 日常內容維護

### 修改中英文內容

大部分文字位於 `app.js` 的 `content` 物件：

- `'zh-TW'`：繁體中文內容。
- `en`：英文內容。

新增或修改翻譯時，兩個語言應使用相同的欄位名稱。修改後至少執行：

```bash
npm test
```

正式名稱不可自行縮寫或改寫：

- `財團法人佛教慈恩育幼基金`
- `Buddhist Tzuen Children’s Welfare Foundation`

郵政劃撥戶名是帳務資料，目前為 `佛教慈恩育幼基金會`，不要因網站正式名稱調整而連帶修改。

### 修改服務項目

七項服務位於 `app.js` 的 `services` 陣列。每項包含：

```javascript
{
  number: '01',
  date: '全年持續',
  title: '服務名稱',
  description: '服務說明',
  image: '圖片檔名.webp'
}
```

注意事項：

- 中文與英文服務數量必須一致。
- 每項都必須提供大約日期或辦理期間。
- 不要自行增加未經確認的服務人數或成果數字。
- 圖片檔名必須與 `public/images/` 中的檔案一致。

### 更新照片

原始素材放在 `resource/assets/`，網站使用的最佳化版本放在 `public/images/`。

維護原則：

- 不要覆寫或刪除原始照片。
- 網站照片優先使用 WebP。
- 一般活動照片長邊建議不超過 1600px。
- 首頁關鍵圖片可直接載入，其餘圖片使用 `loading="lazy"`。
- 檔案應在不明顯影響畫質的情況下降低容量。

使用 `cwebp` 轉換範例：

```bash
cwebp -q 78 -resize 1600 0 "resource/assets/原始照片.jpg" -o "public/images/activity-photo.webp"
```

### 更新 Logo 與 Hero slogan

- 網站 Logo 原始來源：`resource/assets/Logo圓型.png`，只留本機。
- 網站 Logo 最佳化版本：`public/images/logo-round.webp`。
- Hero 網站素材：`public/images/slogan-horizontal-white.svg`。
- `npm run build` 會隨 `public/` 將 Hero SVG 複製到 `dist/public/images/`。

修改 Hero 素材路徑時，要同步修改 `index.html` 與 `tests/site.test.mjs`。

### 更新證書

- 原始證書位於 `resource/assets/`，只留本機。
- 網站版本位於 `public/documents/`。
- 立案證書目前已順時針旋轉 90 度。
- 兩張證書在網站上使用相同大小的小型並排縮圖。
- 點擊縮圖會開啟較大的 WebP 圖片。

證書內容是法律資料，不要修改證書文字或自行增加政府認證說法。

## 修改後檢查

每次修改完成後建議依序執行：

```bash
npm test
npm run build
```

較大的版面或互動修改還要執行 Playwright 測試，並人工檢查：

- 首頁 Hero 是否清楚。
- 中英文是否都能閱讀。
- Header 與 Footer 名稱是否正確。
- 手機版是否沒有文字或圖片被切掉。
- 服務卡片介紹是否完整顯示。
- 證書是否同尺寸並排。
- 電話、Email、Facebook、捐款與地圖連結是否正確。

## Git 練習流程

以下流程適合每次開始一個小修改時使用。

### 1. 查看目前狀態

```bash
git status
```

先確認哪些檔案已修改，不要把不相關檔案一起提交。

### 2. 建立功能分支

```bash
git switch -c feat/update-homepage
```

常見分支名稱：

- `feat/update-homepage`：新增功能。
- `fix/mobile-layout`：修正錯誤。
- `docs/update-readme`：修改文件。
- `chore/optimize-images`：維護與素材最佳化。

### 3. 修改並檢查差異

```bash
git diff
```

只查看某個檔案：

```bash
git diff -- app.js
```

### 4. 執行測試

```bash
npm test
npm run build
```

### 5. 將檔案加入暫存區

建議逐一加入，不要一開始就使用 `git add .`：

```bash
git add index.html styles.css app.js
```

查看即將提交的內容：

```bash
git diff --staged
```

### 6. 建立提交

```bash
git commit -m "feat: update homepage content"
```

提交訊息格式：

```text
<類型>: <簡短說明>
```

常用類型：

- `feat`：新增功能或內容。
- `fix`：修正錯誤。
- `docs`：只修改文件。
- `style`：不影響功能的樣式調整。
- `test`：新增或修改測試。
- `chore`：工具、建置或素材維護。

### 7. 查看提交紀錄

```bash
git log --oneline --decorate --graph -10
```

### 8. 推送分支

第一次推送新分支：

```bash
git push -u origin feat/update-homepage
```

之後在同一分支只需要：

```bash
git push
```

### 9. 合併完成的分支

確認功能分支已提交並通過測試後：

```bash
git switch main
git pull --ff-only
git merge --no-ff feat/update-homepage
git push
```

如果專案使用 GitHub Pull Request，建議在 GitHub 審查並合併，不需要在本機直接執行 `git merge`。

## 常用 Git 復原方式

### 放棄尚未暫存的單一檔案修改

先查看差異：

```bash
git diff -- styles.css
```

確定不要保留後：

```bash
git restore styles.css
```

### 取消暫存但保留修改

```bash
git restore --staged styles.css
```

### 修正最近一次提交

如果已提交但尚未推送，建議另外建立一個修正提交，練習時較容易理解歷史：

```bash
git add styles.css
git commit -m "fix: correct homepage spacing"
```

不要在不理解影響範圍時使用：

```text
git reset --hard
git clean -fd
git push --force
```

這些指令可能永久刪除尚未提交的工作或改寫遠端歷史。

## Public Repository 安全原則

此 repository 預計公開，因此只提交網站運作、維護與審核需要的檔案。

可以提交：

- HTML、CSS、JavaScript、測試、建置腳本與 Markdown 文件。
- `public/images/` 中已壓縮且確認可公開的網站圖片。
- `public/documents/` 中網站實際顯示的壓縮證書。
- `public/images/slogan-horizontal-white.svg`。
- `resource/Tzuen_Intro.md` 等不含私人資料的內容來源。

不可提交：

- `resource/assets/` 原始高解析照片、Logo 與證書。
- 未確認公開授權的兒童照片。
- `.env`、API Key、密碼、Token、私鑰或登入資料。
- `.venv/`、`.playwright-browsers/`、`dist/` 與測試截圖。
- 內部企劃書、志工名冊、身分證件、保險資料或其他個資。

`.gitignore` 應包含：

```gitignore
resource/assets/
.venv/
.playwright-browsers/
dist/
tests/screenshots/
```

將檔案加入 `.gitignore` 只會阻止未來提交，不會刪除舊 commit 已收錄的內容。若原始素材已推送到 GitHub，repository 轉為 Public 前仍須清理 Git 歷史。

## 提交前檢查表

- `git status` 中只有本次相關檔案。
- `git diff` 已人工閱讀。
- 中英文正式名稱正確。
- 中文與英文內容同步。
- 所有圖片路徑存在。
- `npm test` 通過。
- `npm run build` 通過。
- 重要版面修改已通過 Playwright。
- 沒有提交 `resource/assets/`、`.venv/`、`.playwright-browsers/`、`dist/` 或測試截圖。
- 沒有 API 金鑰、密碼、Token 或私人資料。

## 部署注意事項

部署來源應使用 `npm run build` 產生的 `dist/`，不要直接部署整個工作資料夾，避免原始高解析素材一併上傳。

部署前還要確認：

- 正式網域與 HTTPS 設定。
- `tzuen.org` 與 `www.tzuen.org` 是否都能開啟。
- DNS 網站記錄不要覆蓋 Google Workspace 使用的 MX、TXT 記錄。
- 所有外部連結可正常開啟。
- Google Maps 在正式網域可載入。

未經明確確認，不要直接修改 DNS 或執行正式部署。

## 相關文件

- [實作規格](implementation.md)
- [Agent 工作規則](AGENTS.md)
- [基金會內容來源](resource/Tzuen_Intro.md)

# tzuen-website
