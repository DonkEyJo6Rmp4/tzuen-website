# 財團法人佛教慈恩育幼基金網站建置計畫

## 1. 目標與優先順序

本階段目標不是一次做完整大型網站，而是先完成一個可信、清楚、可公開瀏覽的基金會官方網站，主要用途是支援 `tzuen.org` 網域上線，以及申請 Google Workspace for Nonprofits 時能提供正式組織資訊、合法證明、聯絡方式與公益服務內容。

第一優先順序：

1. 建立 `tzuen.org` 主站。
2. 完成中英文切換。
3. 清楚呈現基金會身份、宗旨、服務內容、合法立案文件、聯絡與捐款資訊。
4. 網站可部署到 GitHub 後接 DNS。
5. 保留未來擴充 `hongfasi.tzuen.org` 宏法寺官網的架構。

本輪開始實作網站程式碼，先完成可供 `tzuen.org` 上線審核使用的雙語單頁版本，並同步記錄實作與驗證進度。

## 2. 網站資訊架構

建議第一版採用「首頁式五區塊 + 可獨立路由頁面」的設計。這樣對 Google Workspace for Nonprofits 審核者來說資訊容易確認，之後也可以慢慢拆成完整頁面。

必要頁面或功能如下：

1. 首頁 / 我們是誰
2. 年度服務與活動
3. 合法立案與法人證明
4. 最新消息
5. 聯絡我們與捐款支持

建議路由：

- `/`：首頁，含基金會一句話定位、主要 CTA、服務摘要、捐款入口。
- `/about`：我們是誰，整理緣起、宗旨、核心價值與服務對象。
- `/work`：每年的付出與活動，呈現營隊、育幼院關懷、獎助學金、核棗糕義賣、白米物資關懷等。
- `/legal`：立案證明與法人登記證。
- `/news`：最新消息，初版只顯示「網站建置中，請耐心等候」。
- `/contact`：電話、Email、Facebook、地址、地圖、捐款方式。

若要更快完成，也可以先做單頁網站，導覽列錨點為：

- `#about`
- `#work`
- `#legal`
- `#news`
- `#contact`

建議實作時採用單頁為第一版，後續再升級為多頁，因為申請 Google Workspace for Nonprofits 更重視資訊完整與可信度，不需要一開始就有複雜 CMS。

## 3. 內容規劃

### 3.1 首頁：我們是誰

首頁主訊息應直接回答三件事：

1. 這是一個正式基金會。
2. 基金會長期服務弱勢兒少、育幼院與偏鄉孩子。
3. 大眾可以聯絡、捐款、認識服務內容。

中文主標（品牌 slogan）：

「讓自己成為最溫暖的陽光」— 傳孝法師

英文主標（品牌 slogan）：

`Be the Sunshine That Warms Every Heart.`

主視覺規格：

- 原始素材：`Tzuen/assets/slogan橫式.svg`
- Hero 只顯示一次置中的 slogan，不重複副標、說明文字或右側墨寶卡片。
- 原始 SVG 約 47 MB，且內含 NUL 異常字元造成瀏覽器無法完整渲染，因此不直接提供給瀏覽器；原檔完整保留。
- 中文版只顯示白色橫式墨寶縮圖；英文版在墨寶下方淡淡顯示 `Be the Sunshine That Warms Every Heart.`。

首頁 CTA：

- 主要按鈕：`立即捐款` / `Donate`
- 次要按鈕：`認識我們` / `About Us`
- 聯絡按鈕：`聯絡我們` / `Contact`

### 3.2 年度服務與活動

根據 `Tzuen_Intro.md`，第一版應整理成七大服務方向，且每一項皆顯示約略服務時間：

1. 育幼院與弱勢兒少長期關懷：全年持續進行。
2. 兒童教育與成長陪伴：全年持續進行，寒暑假增加營隊與團體活動。
3. 冬令營、夏令營與兒童營隊：每年寒假約 1–2 月、暑假約 7–8 月。
4. 偏鄉與教育資源不足地區服務：全年依合作單位需求安排，主要配合寒暑假服務行動。
5. 獎助學金與學習支持：每年約 10–11 月辦理。
6. 核棗糕義賣與育幼院新年關懷：每年約 12 月啟動，持續至農曆年前。
7. 白米與民生物資關懷：每年中元普渡後，約 9 月辦理整理與發放。

每個服務方向建議包含：

- 一句話標題
- 2 到 3 句說明
- 對應照片
- 約略日期或辦理期間，以日期標籤清楚呈現
- 可量化但不誇大的描述，例如「每年寒暑假辦理兒童營隊」、「每年 10、11 月推動獎助學金」、「每年農曆年前推動核棗糕義賣」

注意事項：

- 不要自行補不存在的服務人數。
- 若要寫歷年成果數字，需要使用者提供資料或標註待補。
- 可使用現有照片檔名對應活動類別。

### 3.3 合法立案與法人證明

此頁是 Google Workspace for Nonprofits 申請的重要信任區塊。

必放資訊：

- 組織名稱：財團法人佛教慈恩育幼基金
- 立案字號：高市社福字第81658號
- 立案證書圖片：`重要資料_立案證書.jpg`
- 法人登記證圖片：`重要資料_法人登記證.jpg`

建議版面：

- 上方用文字摘要列出組織名稱、立案字號、所在地。
- 下方兩張證書卡片，支援點擊放大。
- 每張圖片需有清楚 alt text。

建議 alt text：

- `財團法人佛教慈恩育幼基金立案證書`
- `財團法人佛教慈恩育幼基金法人登記證書`

注意事項：

- 不要改寫證書上的法律資訊。
- 不要宣稱「已通過 Google Workspace for Nonprofits」。
- 若圖片解析度不足，先照現有素材使用，未來再掃描高清版替換。

### 3.4 最新消息

第一版只需要最小可用內容。

中文：

「網站建置中，請耐心等候。更多基金會活動與公告將陸續更新。」

英文：

`Our website is currently under construction. More foundation updates and announcements will be published soon.`

可以加上 Facebook 連結，讓訪客先看現有動態：

- `https://www.facebook.com/tzuen.org`

### 3.5 聯絡我們與捐款支持

聯絡資訊：

- 電話：`+886 07-2365645`
- Email：`tzuen76201061@gmail.com`
- Facebook：`https://www.facebook.com/tzuen.org`
- 地址：`800高雄市新興區仁愛一街296號`

地圖需求：

- 網站內嵌 Google Map。
- 提供直接開啟 Google Maps App 的連結。

建議 Google Maps 查詢連結：

`https://www.google.com/maps/search/?api=1&query=800高雄市新興區仁愛一街296號`

捐款資訊：

- 標題：`成為最溫暖的陽光`
- 郵政劃撥帳號：`04771311`
- 戶名：`佛教慈恩育幼基金會`
- 捐款連結：`https://39buy.co/charity/item/44015`
- 愛心捐電子發票：`728`

捐款 CTA 建議：

- `立即捐款`
- `愛心捐電子發票 728`
- `郵政劃撥支持`

## 4. 雙語設計

第一版建議使用固定語系資料檔，不要依賴 Google Translate。

資料結構建議：

```txt
src/content/zh-TW.ts
src/content/en.ts
```

或如果使用純 HTML/JS：

```txt
data/i18n.js
```

語言切換需求：

- 預設顯示繁體中文。
- 導覽列右上角提供 `中文 / EN` 切換。
- 使用者切換後可保存到 `localStorage`。
- HTML `lang` 屬性要跟著切換。

翻譯策略：

- 英文以正式、簡潔、可信為主。
- 不逐字翻譯佛教與公益用語，優先讓國際審核者理解。
- 正式中文名稱固定為 `財團法人佛教慈恩育幼基金`。
- 正式英文名稱固定為 `Buddhist Tzuen Children’s Welfare Foundation`，不得省略或改寫。

## 5. 視覺設計方向

風格定位：

- 溫暖
- 可信
- 童心
- 佛教慈悲精神
- 乾淨但不冰冷

主視覺概念：

「一束柔和陽光照進孩子的成長路上」

視覺元素：

- 蓮花線稿
- 柔和陽光
- 手繪愛心、嫩芽、雲朵
- 活動照片卡片
- 圓角卡片與紙張質感

色彩使用：

- 背景以 `#FFFDF8` 為主。
- 導覽列、Footer、主標題用 `#0F2A47`。
- 服務卡片標題與 icon 可用 `#7263A8`。
- 重點數字、蓮花、分隔線用 `#F2B35B`。
- 捐款與主要行動按鈕用 `#F27C38`。
- 兒童故事或營隊卡片可用 `#FFE8EE`。
- 教育課程可點綴 `#8ECFF5`。
- 成功或完成狀態才用 `#73B17A`。

字體建議：

- 中文標題可用 Noto Serif TC 或思源宋體類型，營造正式與溫度。
- 中文內文可用 Noto Sans TC 或思源黑體，確保可讀性。
- 英文可搭配 Merriweather / Source Sans 3 / Nunito Sans 類型。
- 若要避免載入外部字體，需改用本機 fallback，但視覺會較普通。

## 6. 素材使用規劃

可用素材：

- 夏令營照片：`夏令營1.jpg` 到 `夏令營4.jpg`
- 核棗糕義賣：`核棗糕義賣.png`
- 獎助學金：`獎助學金1.jpg` 到 `獎助學金3.jpg`
- 白米發放：`白米發放1.jpg` 到 `白米發放2.jpg`
- 送愛育幼院：`送愛育幼院1.JPG` 到 `送愛育幼院4.JPG`
- 證書：`重要資料_立案證書.jpg`、`重要資料_法人登記證.jpg`

建議首頁圖片配置：

- Hero：優先使用夏令營或送愛育幼院照片，呈現孩子與陪伴感。
- 服務卡片：每個服務方向對應一張圖片。
- 合法證明：只出現在 Legal 區塊，不混入一般活動照片。

圖片處理注意：

- 加上 `loading="lazy"`。
- 裁切比例一致，避免版面跳動。
- 若未來使用 Next.js 或 Astro，可加入圖片最佳化。
- 本輪建立最佳化副本，不覆寫原始照片；一般活動圖片輸出 WebP，長邊控制於約 1,600px，證書則保留足以辨識文字的較高解析度。
- Hero 與首屏圖片應預載或使用高優先級，其餘圖片使用 lazy loading，並設定寬高避免版面位移。
- 不要用 AI 生成圖片替代真實公益照片，真實照片更可信。

## 7. 技術架構建議

因為初期需求是靜態網站、雙語、快速部署，建議選擇以下其中一種：

### 方案 A：Astro

優點：

- 非常適合內容型網站。
- 靜態輸出簡單，SEO 友善。
- 未來可擴充部落格、最新消息、活動頁。
- 圖片與內容結構容易維護。

缺點：

- 需要初始化新專案。

### 方案 B：Vite + React

優點：

- 開發快速。
- 語言切換與互動元件容易寫。
- 未來若要加入複雜功能比較彈性。

缺點：

- 對純內容網站來說稍微比 Astro 重。

### 方案 C：純 HTML/CSS/JS

優點：

- 最快。
- 依賴最少。
- GitHub Pages 很容易部署。

缺點：

- 未來內容管理、路由、雙語維護較容易亂。

建議採用：

第一版若以速度為最高優先，使用 `Vite + React` 或 `Astro`。若後續確定會做最新消息、活動文章、宏法寺子站，建議用 `Astro`。

## 8. 專案結構建議

若採 Astro：

```txt
Tzuen/Website/
  AGENTS.md
  implementation.md
  package.json
  astro.config.mjs
  src/
    content/
      tzuen.zh-TW.ts
      tzuen.en.ts
    layouts/
      SiteLayout.astro
    pages/
      index.astro
      hongfasi/
        index.astro
    components/
      LanguageToggle.astro
      Hero.astro
      ServiceCards.astro
      LegalDocuments.astro
      ContactDonation.astro
  public/
    tzuen/
      assets/
```

若採 Vite + React：

```txt
Tzuen/Website/
  AGENTS.md
  implementation.md
  package.json
  index.html
  src/
    main.tsx
    App.tsx
    content/
      zh-TW.ts
      en.ts
    components/
      Header.tsx
      Hero.tsx
      WorkSection.tsx
      LegalSection.tsx
      NewsSection.tsx
      ContactSection.tsx
    styles/
      theme.css
  public/
    assets/
```

## 9. 宏法寺子站規劃

`hongfasi.tzuen.org` 暫時只規劃，不實作。

未來可能方向：

- 宏法寺簡介
- 法會公告
- 佛學課程
- 寺院歷史
- 聯絡與交通
- 與慈恩育幼基金會的歷史關係

架構建議：

- 若使用 Astro，可用 `/hongfasi` 先開發，再部署時設定子網域 rewrite 或獨立 build。
- 若要完全分離品牌，可在同一 repository 中使用 monorepo：

```txt
apps/
  tzuen/
  hongfasi/
packages/
  shared-ui/
```

第一版不建議 monorepo，因為目前主站上線比較急。

## 10. 部署與 DNS 規劃

使用者已租用 `tzuen.org`。建議流程：

1. 本機完成初版網站。
2. 初始化 Git repository 或使用既有 repository。
3. Push 到 GitHub。
4. 選擇部署平台。
5. 設定自訂網域 `tzuen.org` 與 `www.tzuen.org`。
6. DNS 指向部署平台。
7. 等 HTTPS 憑證生效。
8. 最後再將網站 URL 用於 Google Workspace for Nonprofits 申請。

部署平台建議：

- GitHub Pages：成本低，適合靜態網站，但自動化與 preview 較少。
- Cloudflare Pages：DNS 與 Pages 可以整合，適合已有網域管理需求。
- Vercel：前端部署快速，preview 方便。

DNS 注意事項：

- 不要在網站完成前改 DNS。
- 先確認部署平台給的目標記錄。
- 主網域與 `www` 都要處理。
- 未來 Google Workspace 需要 MX、TXT 驗證記錄，避免與網站記錄混淆。

## 11. Google Workspace for Nonprofits 審核導向檢查表

網站需要讓審核者快速確認：

- 組織名稱清楚。
- 非營利與公益目的清楚。
- 有實際服務內容。
- 有合法立案或登記證明。
- 有可聯絡的電話、Email、地址。
- 網域與組織名稱高度相關。
- 捐款資訊透明。
- 網站不是空殼或只有建置中頁面。

因此第一版一定要避免：

- 只有一頁 Coming Soon。
- 沒有證書。
- 沒有聯絡資訊。
- 沒有服務內容。
- 中英文內容不一致到讓人誤會。

## 12. 實作階段與目前進度

本輪採用零框架依賴的靜態 HTML、CSS 與 JavaScript，以降低首版部署複雜度與載入成本。進度如下：

1. [x] 選定技術棧：靜態 HTML、CSS、JavaScript。
2. [x] 建立專案基礎檔案、測試與 build scripts。
3. [x] 建立原始素材的 WebP 最佳化副本，原檔不覆寫。
4. [x] 建立中英文內容與語言切換，選擇保存於 `localStorage`。
5. [x] 建立品牌色、字體、光影與響應式設計系統。
6. [x] 完成 Header、Footer、手機選單與 Language Toggle。
7. [x] 完成 Hero、墨寶主視覺與 About。
8. [x] 完成七項 Work 服務內容與中英文約略日期。
9. [x] 完成 Legal 證書區與點擊查看原則。
10. [x] 完成 News 建置中區與 Facebook 導流。
11. [x] 完成 Contact、Google Map、Donation。
12. [x] 完成手機、平板與桌面 responsive 樣式。
13. [x] 完成基本 SEO description、語意標籤及圖片 alt。
14. [x] 靜態測試與 build 驗證。
15. [x] Playwright 實際瀏覽器驗收：桌機 1440×1000 與手機 390×844 均通過。
16. [ ] GitHub repository、部署平台與 DNS：待使用者決定，不在本輪異動。

## 13. 驗收標準

初版完成時至少要符合：

- 首頁可正常載入。
- 手機與桌機版面不破。
- 中文與英文可切換。
- 五個必要內容區塊都存在。
- 立案證書與法人登記證可看到。
- 捐款連結可點擊。
- Facebook 連結可點擊。
- Email 可用 `mailto:` 開啟。
- 電話可用 `tel:` 開啟。
- Google Maps 內嵌可看，直接開啟 Maps 的連結可點。
- Build 指令成功。
- 沒有明顯 console error。

## 14. 待使用者確認事項

網站初版已完成；部署前仍需確認：

1. GitHub repository 名稱。
2. 部署平台偏好：GitHub Pages、Cloudflare Pages、Vercel。
3. 是否需要把宏法寺子站也放在同一個 repository。

## 15. 本輪產出紀錄（2026-08-02）

- 英文 slogan 統一為 `Be the Sunshine That Warms Every Heart.`。
- 47 MB 原始 `slogan橫式.svg` 完整保留，但因檔案異常不直接提供給瀏覽器；Hero 改為單一置中 slogan。
- 將活動照片長邊縮至約 1,600px、證書寬度縮至約 1,800px並轉為 WebP，最佳化素材合計約 2.5 MB。
- 七項服務均加入中英文約略日期，未自行虛構精確活動日。
- 完成雙語單頁網站、捐款、合法證明、最新消息、聯絡方式與 Google Map。
- `npm test` 與 `npm run build` 已通過。
- Playwright 與專用 Chromium 已安裝於專案隔離環境；桌機與手機版的圖片載入、雙語切換、語言保存、手機選單、水平溢位及 JavaScript runtime error 檢查均通過。
- 瀏覽器驗收腳本：`tests/browser_check.py`；驗收截圖輸出至 `tests/screenshots/`（不納入 Git）。
- 品牌修正：所有網站 Logo 改用 `Logo圓型.png` 的 192px WebP 版本；正式名稱統一為「財團法人佛教慈恩育幼基金」／`Buddhist Tzuen Children’s Welfare Foundation`；Footer slogan 改為「教育・文化・慈善，讓自己成為最溫暖的陽光」；立案證書順時針旋轉 90 度。
- Hero 使用從原始墨寶資料重組的透明白色橫式縮圖；英文版只加一行淡色 slogan。Our Work 標題改為 `Care Through Every Season`，服務卡介紹完整顯示，立案證書縮圖改為跨欄放大。
- Hero 最終改為直接使用 `Tzuen/assets/slogan橫式白.svg`；立案證書與法人登記證改為同尺寸、小型雙欄並排縮圖。
