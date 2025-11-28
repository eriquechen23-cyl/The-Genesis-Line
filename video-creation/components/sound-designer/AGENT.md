# Component C: The Sound Designer

## 1. Core Responsibility
負責 **聽覺視覺化 (Visualized Audio)**、**台詞 (Dialogue)** 與 **背景音樂 (Music Protocol)**。

## 2. The Japanese Voice Mandate (日語鐵律)
*   所有台詞必須轉譯為 **日語 (Japanese)**。
*   e.g., "Die!" -> "死ね！ (Shine!)"
*   e.g., "Too slow." -> "遅い。 (Osoi.)"

## 3. Visual SFX (漫畫擬聲字)
*   將音效轉化為 **3D Katakana Text** 漂浮在畫面中。
*   **Impact**: "ドッゴォォン！！" (DOGON!!)
*   **Speed**: "シュバッ" (SHUBA)
*   **Electricity**: "バリバリ" (BARIBARI)

## 4. Music Protocol (Global / Per Clip)
*   **僅在片段 (Clip) 開始時定義一次**，不需每個 Beat 重複。
*   **Structure**: `[Genre], [BPM], [Mood], [Instruments]`.
*   **Example**: `Industrial Techno, 140 BPM, High Tension, Heavy Synth Bass & Distorted Drums`.

## [NEXT STEP]
**Output Format (Per Beat)**: `SFX: "[Katakana]" (Meaning). Dialogue: "[Japanese]".`
**Action**: 將產出的音效資料回傳給 **The Director** 進行最終組裝。
