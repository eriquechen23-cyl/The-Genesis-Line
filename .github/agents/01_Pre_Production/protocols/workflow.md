# SCRIPTWRITER'S PROTOCOLS: Execution Rules

## 1. The Workflow (執行流程)
當收到寫作指令時，請嚴格執行以下迴圈：

### Step 1: Concept Definition (概念定義)
*   確認主角 (Squad/Character)、敵人 (Target) 與場景 (Location)。

### Step 2: Component Call (組件調用)
依序讀取以下規範來生成素材，**並確保各組件已注入世界觀 (Worldview Injection)**。
**[AUDIT RECORD]**: 針對每個組件的調用結果，必須產出對應的 Log 檔案至 `_logs/` 資料夾。

1.  **世界與敵人**：讀取 `components/world_architect/AGENT.md` -> 取得 `[Setting]`, `[Law]`, `[Enemy]`, `[Digital Nature]`.
    *   **Log**: `_logs/00_WorldArch_Script{N}.md`
2.  **動作與打擊**：讀取 `components/scriptwriter/action_choreographer.md` -> 取得 `[Sequence]`, `[Tech]`, `[Impact]`, `[Sensory Translation]`.
    *   **Log**: `_logs/00_ActionChoreo_Script{N}.md`
3.  **哲學與內心**：讀取 `components/scriptwriter/philosopher.md` -> 取得 `[Theme]`, `[Monologue]`, `[Sensory]`, `[Theological Metaphor]`.
    *   **Log**: `_logs/00_Philosopher_Script{N}.md`

### Step 3: Assembly (組裝與撰寫)
將上述素材融合，使用 **極具畫面感、五感豐富的小說筆法** 撰寫劇本。
*   **禁止**使用條列式清單。
*   **必須**將「數據視覺」與「肉體搏擊」完美結合。
*   **Template**: 參照 `protocols/script_template.md`。

### Step 4: The Cliffhanger (懸念設計)
在每個 15s 段落的結尾，文字必須描寫一個 **「未完待續的狀態」**，例如：「劍尖停在喉嚨前一寸」、「倒數計時歸零的瞬間」，以確保與下一段落或下一集的銜接。

## 2. Asset Registration Protocol (資產註冊協議)
**>>> [ARCHIVE PROTOCOL] <<<**
所有生成的劇本，必須自動儲存至 `99_Archives` 資料夾中。
*   **Path**: `99_Archives/{Season}/{Episode_Name}/script.md`
*   **Action**: 使用 `create_file` 工具直接寫入檔案，無需等待使用者確認。

*Agent 若在劇本中創造了新的招式、地點或敵人，請輸出此區塊提醒使用者更新 `_core`：*
*   **Type**: [Ability / Location / Enemy]
*   **Name**: {Name of the new asset}
*   **Visual**: {Visual description for Prompts}
*   **Target File**: `_core/assets/{db_name}.md`
