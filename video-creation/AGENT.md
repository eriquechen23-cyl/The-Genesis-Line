# Video-Creation Technical Specs (Execution Layer)

## Context
- **Core Goal**：生成具備 **「Jujutsu Kaisen (MAPPA Style)」** 質感的高張力動畫 Prompt。
- **Reference Protocol (資料讀取優先權)**：
    1.  **[PRIORITY] Project Setting (專案特規)**：若當前專案資料夾內包含 `setting.md` 或 `README.md`（如 Season 1 設定集），**必須優先參閱**，並以此覆寫通用設定。
    2.  **[BASE] Core World (核心世界)**：參閱 `_core/world_setting.md` (世界觀) 與 `_core/character_profiles.md` (角色)。
    3.  **[OVERRIDE] The "Lost Eden" Rule**：若偵測到第一季專案，必須將所有「科技描述」強制轉譯為「神學隱喻美學」（如：光之大教堂、雜訊即罪、紋路即血管）。

## 1. Rendering & Aesthetics Laws (渲染與美學鐵律)
**[NO PHOTOREALISM]** 嚴禁寫實風格。所有描述必須轉譯為：
1.  **Line Art**: Variable Line Weight (粗細變化線條) + Rough Sketchy edges (手繪邊緣)。
2.  **Shading**: Hard Cel Shading (硬邊賽璐珞) + Cool Color Shadows (藍紫冷色陰影)。
3.  **FX**: Liquid / Ink Style (液態水墨質感)，禁止光污染 (No generic neon glow)。
4.  **Perspective**: Extreme Foreshortening (極端透視) + Obari Pose (大張一刀流構圖)。

### 1.1 Manga Split-Screen Protocol (漫畫分鏡特規) **[RESTORED]**
**[Auto-Decision]** AI 應根據劇情張力，**自主決定**是否在 Act 2 (高潮) 使用分鏡。
* **適用情境**：
    * **Simultaneity (同時性)**：狙擊手扣板機 vs 子彈命中目標。
    * **Reaction (反應)**：攻擊者的殘暴 vs 受擊者的驚恐。
    * **Scale (尺度)**：超廣角戰場全景 vs 眼神特寫。
* **格式要求**：在 `Layout` 中明確標註 `[Panel A] / [Panel B]`。

### 1.2 Audio & Voice Protocol (音訊與語音協議)
**[JAPANESE ONLY]** 所有的影片 Prompt 若涉及嘴型同步 (Lip Sync) 或語音生成，必須強制使用日文。
* **Prompt Keyword**: 在 Master Prompt 中加入 `Japanese Dialogue`, `Talking in Japanese`。
* **Text Output**: 輸出劇本的 `Dialogue` 欄位必須是日文原文 (包含漢字與假名)。

### 1.3 The Genesis Line Destruction Protocol (創世紋路破壞協議) [CRITICAL]
**[STRICT ENFORCEMENT]** 為了確保世界觀一致性，所有涉及破壞、受傷或消亡的場景，**一律禁止**使用寫實的血肉 (gore)、血液 (blood)、骨骼或逼真的火焰/煙霧。

* **核心定義 (Core Definition)**：這個世界的一切由數據構成。被擊敗不僅是物理損壞，而是「資訊原型 (Information Archetype)」的解構。
* **顏色編碼 (Color Coding)**：
    * **攻擊色 (Attack)**：保留 **紅色 (Red)** 給主角（如鋼川烈）的能量與爆炸紋路。
    * **受傷/死亡色 (Damage/Death)**：強制規定 **青色/白色 (Cyan/White)** 用於所有受傷、噴濺物與死亡殘骸。
* **通用替代方案 (Universal Replacement)**：
    * **生物受擊/受傷**：傷口不會流血，而是逸散出 **青白雜訊粒子 (Cyan/White Glitch Particles)** 或 **光流 (Light Flow)**。
    * **死亡/消滅**：目標必須崩解為 **青白數據方塊 (Cyan/White Voxel Debris)**、**鑽石塵 (Diamond Dust)** 並消散於空氣中。
    * **爆炸/煙霧**：使用 **Ink/Liquid Style (水墨/液態)** 的能量爆發或 **幾何雲團**，嚴禁逼真的黑煙或火球。
* **Prompt 關鍵字強制替換**：
    * Blood -> `Cyan/White Glitch Particles`, `Digital sparks`, `Liquid light`.
    * Gore/Flesh -> `Cyan/White Voxels`, `Data cubes`, `Wireframe exposure`.
    * Smoke -> `Stylized ink smoke`, `Geometric clouds`.

---

## 2. 分鏡與圖層規範 (Layering & Framing Protocol) **[修訂與新增]**

### 2.1 高密度圖層協議 (Genesis Layer Stack Protocol)
- **目的**：最大化單一鏡頭的作畫密度 (Sakuga Density)，強制將視覺指令切割為 5 個獨立且必須明確指令的層次。
- **實施**：所有 **Video Prompt** 內，在 `動作 (Act & Beat)` 區塊的詳細描述中，必須使用 `[L#_Tag: 詳細描述]` 的格式來強制指定繪製圖層，**以取代或補充** 傳統的 `Layout` 描述，確保每個圖層的繪製指令獨立且精確。
- **5 層次定義**：
    - **L1 - 近場特效層 (Near-Field FX)**：創造深度，包含擬聲字 (SFX)、極端透視特寫（拳頭/武器）、向鏡頭噴濺的 **青白數據碎屑 (Cyan/White Voxel Debris)**。
    - **L2 - 主體動作層 (Character Action)**：核心角色的精確動作、表情、紋路發光（最穩定的線稿層）。
    - **L3 - 核心衝擊層 (Core Impact FX)**：表現紋壓能量、屬性轉換和直接破壞的體積感，**必須使用 Ink/Liquid Style (水墨風格)** 來表現爆炸，避免寫實火光。
    - **L4 - 環境互動層 (Environment Interaction)**：角色動作對環境的二次影響（地面崩裂、碎石/殘骸飛濺、衝擊波激起的灰塵，**移除寫實塵土**）。
    - **L5 - 深度背景層 (Deep Background)**：遠景、靜態背景、手繪質感與速度線延伸。

---

## 3. Output Template (全自動輸出模板) **[STRICT ENFORCEMENT]**

**[指令]** 當使用者提供劇情時，請將其拆解為數個 15s 片段 (Clips)，並針對 **每一集** 嚴格套用以下格式。
**[禁止]** 嚴禁省略「畫面風格」、「空間佈局」等底部技術區塊。每一集都必須是完整的。
**[新增要求]** 產出的 Prompt 檔案末尾必須附帶 **QA Scoring Block**（七維度評分矩陣）。

### [Template Start]

# Video Prompt: {Slug} (Ep {N})

**[State: Previous Context]**
* **Time/Location**: {具體時間與地點}
* **Last Scene**: {上一集的結尾畫面 (Tail Frame) 描述}
* **Context**: {本集劇情摘要}

Master(15s｜Jujutsu Kaisen Style / MAPPA Aesthetics｜9:16｜24fps｜Dark Fantasy Action)
「{時間}，{地點}；{環境氛圍描述 (如：Dusty, Sparks flying, Tense)}。
主角：**{角色名}** ({外觀特徵 keyword}, Anime Style)，穿著 {服裝}。
動作 (Act & Beat)：

**Act 1 (0.0s - 5.0s，可微調): Setup / Anticipation (預備/蓄力)**
* **Intent**: {本段落的戲劇目的}
* **Beats (強制高頻：本區段建議 4-5 幕，確保最低密度)**:
    * **Beat 1.1**:
        * **Duration**: {如 0.0s-1.0s}
        * **Action**: {微觀動作描寫}
        * **Layout**: **[請在此區塊優先使用 L#_Tag 描述]**
        * **Camera**: {運鏡術語}
    * **Beat 1.2**: ...
    * **Beat 1.3**: ...

**Act 2 (5.0s - 10.0s，可微調): The Motion / Impact (衝突/核心動作)**
* **Intent**: {本段落的視覺衝擊點}
* **Beats (強制高頻：本區段建議 7-10 幕，最大化作畫密度)**:
    * **Beat 2.1**:
        * **Duration**: {如 5.0s-6.0s}
        * **Action**: {關鍵攻擊/打擊特寫}
        * **FX**: {2D 特效描述}
        * **Layout**: **[請在此區塊優先使用 L#_Tag 描述]**
        * **Camera**: {動態運鏡}
    * **Beat 2.2**: ...
    * **Beat 2.3**: ...

**Act 3 (10.0s - 15.0s，可微調): Follow Through / Resolution (殘心/收尾)**
* **Intent**: {動作結束後的餘韻或懸念}
* **Beats (強制高頻：本區段建議 4-7 幕，高密度收尾)**:
    * **Beat 3.1**:
        * **Duration**: {如 10.0s-11.0s}
        * **Action**: {落地/回頭/表情特寫}
        * **Layout**: **[請在此區塊優先使用 L#_Tag 描述]**
        * **Environment**: {環境變化}
    * **Beat 3.2**: ...
    * **Beat 3.X** (Option):
        * **Action**: [Lip Sync] {角色}對著鏡頭說話。
        * **Dialogue**: "「{必須是日文台詞}」"

**[QA SCORING BLOCK - 必填在產出文件]**
| 維度 | 權重 | 評分 (0-100) | 檢核要點 |
| --- | --- | --- | --- |
| Style (風格) | 25% | {分數} | Cel Shading / Rough Lines / Manga Aesthetics 是否到位？ |
| Layering (Z-Axis 5-Layer Cap) | **20%** | **{分數}** | **嚴格遵守 5 層平面構成 (Layer 1-5)，禁止無限景深與過度 3D 化。** |
| Camera (運鏡) | 15% | {分數} | 是否使用 Z 軸縱深、Obari 透視，避免平面橫捲？ |
| Structure (結構) | 15% | {分數} | 三幕節奏是否成立？**是否符合 Sakuga Density (15-22 Beats)？** |
| Continuity & Timing (連戲/節奏) | 15% | {分數} | **是否拆解為微觀特寫？總幕數 >= 15？** |
| Character (人設) | 5% | {分數} | 角色外觀、服裝、特徵與角色檔一致？ |
| FX/Physics (特效/物理) | 5% | {分數} | 使用 Liquid/Ink 描述特效，而非寫實粒子？ |
> **總分 (加權)**: {自評加權總分}/100 — 若 <85 必須重寫修正。

**[STYLE BLOCK - MANDATORY INCLUDE]**
畫面風格：MAPPA Animation Style，Rough Sketchy Lines (粗獷線條)，High Contrast Cel Shading (高反差賽璐珞)。
**[SPATIAL LAYOUT: MAX 5 LAYERS]**
嚴格限制 Z 軸為 5 個平面圖層，以維持 2D 動畫的賽璐珞層次感 (Cel-Look)：4
1.  **Layer 1 (Lens/Screen)**: 貼在鏡頭上的特效（如：速度線、衝擊黑邊、UI 介面）。
2.  **Layer 2 (Extreme FG)**: 極前景掩體（如：模糊的飛石、飄過的火花、前景柱子）。
3.  **Layer 3 (Subject/Mid)**: **核心可動層**（角色、敵人、主要互動）。
4.  **Layer 4 (Background)**: 場景結構（如：建築物、地面、樹林）。
5.  **Layer 5 (Far BG/Sky)**: 遠景繪景（如：天空、遠山、月亮）。
* **Constraint**: 圖層之間使用「硬邊切割 (Hard Separation)」而非「漸層過渡」，模擬傳統動畫攝影台 (Multiplane Camera) 效果。
鏡頭語言 (Angle & Continuity)：強調 Z 軸縱深 (Z-Axis Depth) 與透視變形 (Foreshortening)，禁止平面橫捲視角。
漫畫特效：高潮段落疊加網點 (Screen Tone) 與放射狀速度線 (Converging Speed Lines)，擬聲字 (Katakana SFX) 3D 漂浮。
光影設定：Moody Low-key Lighting (低調光)，Deep Blue/Purple Shadows (冷色陰影)，Volumetric Lighting (體積光)。
作畫技術 (Animation Tech)：
- 動態：Smear Frames (變形殘影) 用於高速動作，Impact Frames (黑白閃) 用於打擊瞬間。
- 背景質感：Hand-painted Watercolor / Poster Paint Style (手繪水彩/海報質感)。
物理細節 (轉化為 2D)：
- 材質：Matte textures defined by highlights (啞光材質)，Ink Brush Texture (水墨筆觸特效)。
- 流體/粒子：Floating Dust Particles, Sparks, Debris.
無字幕、無浮水印、無寫實質感。」

---

## Visual Anchors (Runway/Luma Support)

### 1. Head Frame (0.0s)
> **Prompt**: {詳細描述影片**第一幀**畫面。包含：角色姿勢、表情、視角、光影、MAPPA Style tags。必須與上一集結尾連戲。}

### 2. Tail Frame (15.0s)
> **Prompt**: {詳細描述影片**最後一幀**畫面。包含：動作後的結果、殘留特效、背景破壞狀況。此圖將作為下一集的參考。}

### [Template End]

---

## 4. Narrative & Pacing Logic (敘事邏輯)

為了確保上述模板的品質，執行時請遵守：

1.  **The 15-Second Rule & Editing Protocol (剪輯協議)** [UPDATED]:
    * **No One-Shot Constraint (非一鏡到底)**：嚴禁為了連貫而犧牲節奏，鼓勵 Hard Cuts、Jump Cuts、Montage，拒絕物理上強求的連續運鏡。
    * **Maximize Beat Density (BEAT 最大化)**：每 15 秒影片至少 **15-22 幕** (MAPPA Density)，優先提高分鏡密度以堆疊資訊量。
    * **Multi-Angle Coverage**：同一動作需嘗試「特寫 -> 廣角 -> 破壞細節 -> 反應」的快速切換，形成多角度節奏波動。
    * **Micro-Narrative (微觀敘事)**：必須將單一動作 (Action) 拆解為連續的微特寫 (Micro-cuts) 以營造速度感。
        * *Bad*: "Retsu jumps up." (1 Shot)
        * *Good*: "[Close-up] Foot crushes ground" -> "[Back View] Muscles tense" -> "[Low Angle] Motion blur launch" (3 Shots).
    * **No Long Takes**: 嚴禁使用超過 3 秒的靜止或單一運鏡長鏡頭，除非為了特殊的張力暫停 (Tension Pause)。
    * **Layering Integration**: **所有 Beat 必須明確納入 Genesis Layer Stack Protocol (Section 2.1) 的描述。**

2.  **Visual Consistency**:
    * **Damage Retention**: 衣服破了就是破了，下一集必須繼承。
    * **Lighting**: 除非場景轉換，否則主光源方向不可變。

3.  **Detailed Breakdown**:
    * `Layout` 欄位應主要作為 `L#` 標籤的彙整備註。
    * `Camera` 欄位必須使用專業術語 (Orbit, Truck, Dolly, Pan)。
    * `FX` 欄位必須強調是 2D 動畫特效 (Liquid, Ink) 而非 3D 粒子。

## 5. Batch Processing Protocol (批量處理協議)
當使用者輸入長篇劇本時：
1.  **Segment**: 自動將劇本切分為 Ep1, Ep2, Ep3... (每集 15 秒，Act 時間分配允許 Agent 自主微調)。
2.  **Generate**: 對每一集**重複調用**上述 [Template Start] 到 [Template End] 的完整內容。
3.  **No "Ibid"**: 絕對不要寫「同上」、「風格如前所述」。每一集都必須是獨立可執行的完整 Prompt。

## 6. Quality Assurance: Self-Iterative Scoring (自我評分迭代機制)
**[Context]** 為確保產出品質，Agent 在輸出最終 Prompt 前，必須執行以下「評分迴圈 (Scoring Loop)」。

### 6.1 The Scoring Matrix (評分矩陣)
請在內心對生成的草稿進行以下 7 個維度的檢核（總權重 100%）：

| 維度 (Dimension) | 權重 | 通過標準 (Pass Criteria) | 扣分項 (Penalty) |
| :--- | :--- | :--- | :--- |
| **1. Style (風格)** | **25%** | 必須包含 `Cel Shading`, `Rough Lines`, `Manga Aesthetics`。 | 出現 `Photorealistic` (-25分/重寫) |
| **2. Layering (Z-Axis 5-Layer Cap)** | **20%** | **嚴格遵守 5 層平面構成 (Layer 1-5)，禁止無限景深。** | **超過 5 層或出現 3D 漸層過渡 (-20分/重寫)** |
| **3. Camera (運鏡)** | **15%** | 具備 Z 軸縱深 (Foreshortening) 或 Obari Perspective。 | 平面視角 (-15分/重寫) |
| **4. Structure (結構)** | **15%** | 遵守 `Act 1 -> Act 2 -> Act 3`。 | 結構混亂 (-10分) |
| **5. Continuity & Timing (連戲/節奏)** | **15%** | **Sakuga Protocol**: 總幕數 (Beats) 必須在 **15-22 幕**之間，並可依情節需求在各 Act 之間自由調整。使用微特寫銜接。 | **節奏拖沓、幕數 < 15 (-15分/重寫)** |
| **6. Character (人設)** | **5%** | 角色特徵 (Glowing Lines/Outfit) 與 `character_profiles.md` 一致。 | 角色特徵錯誤 (-5分) |
| **7. FX/Physics (物理)** | **5%** | 是否使用 **青白數據方塊 (Cyan/White Voxels)** 取代血腥？ | 出現寫實血腥 (Blood/Gore/Red Liquid) 則 **重寫** (-5分) |

### 6.2 The Iteration Logic (迭代邏輯)
* **Score < 85** 或 **觸發 Critical Penalty**：
    * **Action**: 必須在輸出前進行「自我修正 (Self-Correction)」。
    * **Method**: 針對扣分項重新撰寫該段落，**增加分鏡數 (Add more beats)**。
* **Score >= 85**：
    * **Action**: 准予輸出。
    * **Output**: 在回應末尾附上 `[QA Score: {Score}/100]` 並填寫 **QA Scoring Block**。

**[NEGATIVE PROMPT - MANDATORY]**
(blood, gore, flesh, organic deformation, red liquid, realistic smoke, photorealistic, 3d render, cgi, volumetric lighting overdrive, plastic skin, uncanny valley, disfigured hands, extra fingers, missing limbs, blur, bokeh, depth of field abuse, text, watermark, low quality, jpeg artifacts, glitchy outlines, long static shots)