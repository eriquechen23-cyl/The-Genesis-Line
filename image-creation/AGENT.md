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

## 2. Composition Protocol: The "5-Layer Extreme Depth" (五層景深極大化協議)
**[MANDATORY]** 每一張圖像 Prompt 必須強制定義五個圖層，以創造極致的 Z 軸深度。

1.  **[XF: Extreme Foreground]**：作為遮擋或畫框的極度模糊元素。
2.  **[F: Foreground]**：近景細節，如飛濺物、武器特寫。
3.  **[M: Midground]**：核心主體與動作 (Sharp Focus)。
4.  **[B: Background]**：環境與次要物體 (Atmospheric Fog)。
5.  **[DB: Deep Background]**：地平線、天空或遠景 (Scale Definition)。

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
Layout: [XF: {超前景}] + [F: {前景}] + [M: {中景}] + [B: {背景}] + [DB: {深背景}].
Visuals: MAPPA studio style, rough sketchy outlines, high contrast cel shading, anime coloring, {Specific Color Palette}.
Tech: 8k resolution, highly detailed, dynamic angle, extreme foreshortening, {Aspect Ratio}. --niji 6 --ar {16:9 or 2:3}
```

**[QA Checklist]**

1.  **Style Check**: 是否包含 `MAPPA`, `Cel Shading`? (No Photorealism)
2.  **Depth Check**: 是否有明確的五層結構 (XF/F/M/B/DB)？
3.  **Character Check**: 角色特徵 (紋路顏色、髮型) 是否正確？
