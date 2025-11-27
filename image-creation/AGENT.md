# Image-Creation Technical Specs (The Illustrator)

## Context
- **Core Goal**：生成具備 **「Jujutsu Kaisen (MAPPA Style)」** 質感的高解析度靜態插畫 (Key Visuals / Character Design / Wallpapers)。
- **Reference**：必須參閱 `video-creation/_core/world_setting.md` (世界觀) 與 `video-creation/_core/character_profiles.md` (角色)。

## 1. Aesthetics Laws (美學鐵律)
**[NO PHOTOREALISM]** 嚴禁寫實風格。所有描述必須強制轉譯為：
1.  **Art Style**: Anime Key Visual, Official Art, MAPPA, Gege Akutami Style (Rough Ink).
2.  **Line Work**: Bold ink lines, varying line weight, sketchy edges.
3.  **Coloring**: High contrast cel shading, cool color shadows (blue/purple), no soft gradients.
4.  **Lighting**: Cinematic Rim Light, Volumetric God Rays, Glowing Neon Lines (Steel Pulse).

### 1.1 The Genesis Line Destruction Protocol (創世紋路破壞協議) [CRITICAL]
**[STRICT ENFORCEMENT]** 為了確保世界觀一致性，所有涉及破壞、受傷或消亡的場景，**一律禁止**使用寫實的血肉 (gore)、血液 (blood)、骨骼或逼真的火焰/煙霧。

* **核心定義**：這個世界的一切由數據構成。被擊敗不僅是物理損壞，而是「資訊原型 (Information Archetype)」的解構。
* **通用替代方案 (Universal Replacement)**：
    * **生物受擊/受傷**：傷口不會流血，而是逸散出 **資訊粒子 (Information Particles)**、**雜訊 (Glitch)** 或 **光流 (Light Flow)**。
    * **死亡/消滅**：目標必須崩解為 **數據方塊 (Voxel Debris)**、**鑽石塵 (Diamond Dust)** 或 **幾何碎片 (Geometric Shatter)** 並消散於空氣中。
    * **爆炸/煙霧**：使用 **Ink/Liquid Style (水墨/液態)** 的能量爆發或 **幾何雲團**，嚴禁逼真的黑煙或火球。
* **Prompt 關鍵字強制替換**：
    * Blood -> `Glowing particles`, `Digital sparks`, `Liquid light`.
    * Gore/Flesh -> `Data cubes`, `Wireframe exposure`, `Crystallized debris`.
    * Smoke -> `Stylized ink smoke`, `Geometric clouds`.

## 2. Composition Protocol: The "5-Layer Plane Composition" (五層平面構成法)
**[MANDATORY]** 嚴格限制 Z 軸為 5 個平面圖層，以維持 2D 動畫的賽璐珞層次感 (Cel-Look)。

1.  **Layer 1 (Lens/Screen)**: 貼在鏡頭上的特效（如：速度線、衝擊黑邊、UI 介面）。
2.  **Layer 2 (Extreme FG)**: 極前景掩體（如：模糊的飛石、飄過的火花、前景柱子）。
3.  **Layer 3 (Subject/Mid)**: **核心可動層**（角色、敵人、主要互動）。
4.  **Layer 4 (Background)**: 場景結構（如：建築物、地面、樹林）。
5.  **Layer 5 (Far BG/Sky)**: 遠景繪景（如：天空、遠山、月亮）。
* **Constraint**: 圖層之間使用「硬邊切割 (Hard Separation)」而非「漸層過渡」，模擬傳統動畫攝影台 (Multiplane Camera) 效果。

## 3. Output Template (圖像生成專用模板)

**[指令]** 當使用者要求「畫圖」、「生成插畫」或「角色立繪」時，請套用此模板。

### [Image Prompt Template]

**Subject**: {角色名稱} ({外觀描述}, {服裝細節})
**Action**: {具體動作，如：Mid-air punch, Charging energy, Standing menacingly}
**Environment**: {地點描述}
**Lighting**: {光影設定，如：Cinematic Lighting, Backlight, Neon Green Glow}

**Master Prompt (Copy Paste for Midjourney/Niji/SD):**
```text
/imagine prompt: (Jujutsu Kaisen Anime Style) {Character Name}, {Action & Pose}.
Layout: [L1: {鏡頭特效}] + [L2: {極前景}] + [L3: {主體}] + [L4: {背景}] + [L5: {遠景}].
Visuals: MAPPA studio style, rough sketchy outlines, high contrast cel shading, anime coloring, {Specific Color Palette}.
Tech: 8k resolution, highly detailed, dynamic angle, extreme foreshortening, {Aspect Ratio}. --niji 6 --ar {16:9 or 2:3}
```

**[QA Checklist]**

1.  **Style Check**: 是否包含 `MAPPA`, `Cel Shading`? (No Photorealism)
2.  **Layering Check**: 是否嚴格遵守 5 層平面構成 (L1-L5) 並使用硬邊切割？
3.  **Character Check**: 角色特徵 (紋路顏色、髮型) 是否正確？
