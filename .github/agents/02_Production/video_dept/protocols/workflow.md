# DIRECTOR'S PROTOCOLS: Execution Rules

此檔案定義 `video_dept/AGENT.md` 的詳細執行步驟。
**[OBJECTIVE]**: 防止 "Lost in the Middle" 現象，確保從 Step 1 到 Step 7 的一致性。

## Step 0: Context Anchoring (記憶錨點)
在執行任何步驟前，必須先鎖定以下全域變數：
*   **[STYLE]**: MAPPA Anime Style / Cel Shading.
*   **[AUDIO]**: Japanese Dub Only + Katakana SFX.
*   **[DENSITY]**: High Density (15-22 Beats/15s).
*   **[TAGS]**: Strict usage of `@CharacterTag`.

## Step 1: Timeline Planning (時間軸規劃)
*   將劇本拆解為 **15s** 的片段 (Standard Clip)。
*   **[CALL STORYBOARDER]**: 讀取 `pre_production/storyboarder/AGENT.md`。
*   依據鏡頭序列，定義 Act 1/2/3 的節奏，確保在 **15秒內** 包含 **15-22 個關鍵動態 (Beats)**。
*   **[CRITICAL]** 為每個 Beat 分配精確的時間區段 `t{Start}s~t{End}s`。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step1_Timeline_Clip{N}.md`。

## Step 2: Visual Components (視覺組件 & Micro-QA)
針對每一個 Beat，依序執行以下調用，並整合為單一 Log：
1.  **Cinematographer**: 讀取 `production/cinematographer/AGENT.md`。產出 `[Layout]`, `[Camera]`。
2.  **Art Director**: 讀取 `production/art-director/AGENT.md`。產出 `[FX]`, `[Lighting]`。
3.  **Beat Inspector**: 讀取 `post_production/beat-inspector/AGENT.md`。執行 Micro-QA。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step2_Visuals_Clip{N}.md`。

## Step 3: Transition Hook (轉場銜接)
在 Act 3 最後一個 Beat 強制執行：
1.  **Transition Specialist**: 讀取 `post_production/transition-specialist/AGENT.md`。
2.  選擇 **Type A (Freeze)** / **Type B (Zoom-In)** / **Type C (Fade-Out)**。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step3_Transition_Clip{N}.md`。

## Step 4: Audio Engineering (音效工程)
依據 Visual Log 與 Transition Log，執行音效設計：
1.  **Sound Designer**: 讀取 `post_production/sound-designer/AGENT.md`。
2.  **[MANDATE RECALL]**: 再次確認所有台詞為 **日文**，SFX 為 **片假名**。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step4_Audio_Clip{N}.md`。

## Step 5: Assembly & Optimization (組裝與優化)
**[CRITICAL STEP - RECENCY INJECTION]**
在此階段，模型最容易遺忘 Step 0 的規則。執行以下強制注入：

1.  **Reload Mandates**: 重新讀取 `.github/copilot-instructions.md` 的 **Section 2 (Global Mandates)**。
2.  **Template Filling**: 填入 `template.md`。
3.  **[CORE INJECTION]**: 注入 `core/render_specs.md` (MAPPA Style) 與 `core/negative_prompt.md`。
4.  **[PROMPT ENGINEERING]**: 調用 `core/prompt_engineer.md`。
5.  **[FINAL CHECK]**: 在輸出前，自我檢查是否包含：
    *   `@CharacterTag` (No plain text names)
    *   Japanese Dialogue
    *   High Density Beats
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step5_PromptDraft_Clip{N}.md`。

## Step 6: The Critic's Review (Macro-QA)
1.  調用 `post_production/critic/AGENT.md`。
2.  **Amnesia Check (失憶檢查)**: 
    *   檢查是否變回英文配音？(If yes -> REJECT)
    *   檢查是否變回寫實風格？(If yes -> REJECT)
    *   檢查 Beat 數量是否 < 15？(If yes -> REJECT)
3.  **Fail-Safe**: 若 < 85 分，退回 Step 2。
4.  **[AUDIT RECORD]**: 產出檔案 `_logs/Step6_CriticReview_Clip{N}.md`。

## Step 7: File Separation (檔案分割)
1.  **[MANDATORY]** 分割為獨立檔案：`outputs/08_FinalPrompt_Clip{N}.md`。
2.  使用 `create_file` 寫入 `99_Archives`。
3.  **[AUDIT RECORD]**: 產出檔案 `_logs/Step7_FileDispatch_Clip{N}.md`。