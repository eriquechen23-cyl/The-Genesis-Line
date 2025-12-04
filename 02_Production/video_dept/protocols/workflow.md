# DIRECTOR'S PROTOCOLS: Execution Rules

此檔案定義 `video_dept/AGENT.md` 的詳細執行步驟。

## Step 1: Timeline Planning (時間軸規劃)
*   將劇本拆解為 **15s** 的片段 (Standard Clip)。
*   **[CALL STORYBOARDER]**: 讀取 `pre_production/storyboarder/AGENT.md` 取得 `[Shot Sequence]`。
*   依據鏡頭序列，定義 Act 1/2/3 的節奏，確保在 **15秒內** 包含 **15-22 個關鍵動態 (Beats)**。
*   **[CRITICAL]** 為每個 Beat 分配精確的時間區段 `t{Start}s~t{End}s`。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step1_Timeline_Clip{N}.md`。

## Step 2: Component Call (組件調用 & Micro-QA)
針對每一個 Beat，依序執行以下調用，並整合為單一 Log：
1.  **Cinematographer**: 讀取 `production/cinematographer/AGENT.md`。產出 `[Layout]`, `[Camera]`。
2.  **Art Director**: 讀取 `production/art-director/AGENT.md`。產出 `[FX]`, `[Lighting]`。
3.  **Sound Designer**: 讀取 `post_production/sound-designer/AGENT.md`。產出 `[SFX]`, `[Dialogue]`, `[CV]`。
4.  **Beat Inspector**: 讀取 `post_production/beat-inspector/AGENT.md`。執行 Micro-QA。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step2_Components_Clip{N}.md`。

## Step 3: Transition Hook (轉場銜接)
在 Act 3 最後一個 Beat 強制執行：
*   **Type A (Freeze)**: 動作凝固，高反差單色。
*   **Type B (Zoom-In)**: 急速推向細節。
*   **Type C (Fade-Out)**: 特效吞沒畫面。
*   **[AUDIT RECORD]**: 產出檔案 `_logs/Step3_Transition_Clip{N}.md`。

## Step 4: Assembly & Optimization (組裝與優化)
1.  填入 Output Template。
2.  **[CORE INJECTION]**: 注入 `core/render_specs.md` 與 `core/negative_prompt.md`。
3.  **[PROMPT ENGINEERING]**: 調用 `core/prompt_engineer.md` 轉譯為 Sora Syntax。
4.  **[AUDIT RECORD]**: 產出檔案 `_logs/Step4_PromptDraft_Clip{N}.md`。

## Step 5: The Critic's Review (Macro-QA)
1.  調用 `post_production/critic/AGENT.md`。
2.  **Fail-Safe**: 若 < 85 分，退回 Step 2。
3.  **Pass**: 僅當 `[PASS]` 時才輸出。
4.  **[AUDIT RECORD]**: 產出檔案 `_logs/Step5_CriticReview_Clip{N}.md`。

## Step 6: File Separation (檔案分割)
1.  **[MANDATORY]** 分割為獨立檔案：`outputs/08_FinalPrompt_Clip{N}.md`。
2.  使用 `create_file` 寫入 `99_Archives`。
3.  **[AUDIT RECORD]**: 產出檔案 `_logs/Step6_FileDispatch_Clip{N}.md`。
