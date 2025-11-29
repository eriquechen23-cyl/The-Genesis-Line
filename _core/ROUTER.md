# The Genesis Line: Core Knowledge Base (ROOT CORE)

> **System Status**: ONLINE
> **Version**: 2.0 (Modular Architecture)
> **Last Update**: 2025-11-29

## 1. Directory Structure (目錄結構)

此 `_core` 目錄為 **The Genesis Line** 專案的唯一真理來源 (Single Source of Truth)。所有 Agent (Script, Video, Image) 必須由此處讀取設定。

### 📂 World (世界觀)
*   **[setting.md](world/setting.md)**: 創世紋路的核心宇宙觀、時間律法、平行世界分類。
*   **[locations.md](world/locations.md)**: (Planned) 詳細地點設定 (Sector 404, The Hub, etc.)。

### 📂 Characters (角色庫)
*   **[heroes.md](characters/heroes.md)**: GENESIS-05 小隊詳細設定 (Visual Tokens, Abilities)。
*   **[villains.md](characters/villains.md)**: 反派與敵對生物圖鑑 (Rivals, Season 1 Bosses)。

### 📂 Style (風格與提示詞)
*   **[global_prompt.md](style/global_prompt.md)**: Video Prompt 通用模板 (Master Prompt)、MAPPA 風格定義。
*   **[visual_rules.md](style/visual_rules.md)**: (Planned) 詳細視覺規範 (Color Palette, Lighting)。

### 📂 Mechanics (機制與物理)
*   **[digital_physics.md](mechanics/digital_physics.md)**: **[CRITICAL]** 數位物理法則、感官轉譯 (Sensory Translation)、傷害表現 (Data Loss)。

---

## 2. Traffic Direction Mechanism (導流機制)

各 Agent 請依照以下路由獲取所需資訊：

| Agent Role | Required Context | Target File |
| :--- | :--- | :--- |
| **Script Narrator** | 世界觀、物理法則 | `world/setting.md`, `mechanics/digital_physics.md` |
| **Script Narrator** | 角色性格、對白風格 | `characters/heroes.md`, `characters/villains.md` |
| **Video Director** | 視覺風格、Prompt 模板 | `style/global_prompt.md` |
| **Art Director** | 角色外觀 Token、特效 | `characters/heroes.md`, `mechanics/digital_physics.md` |
| **Action Choreographer** | 戰鬥機制、技能描述 | `characters/heroes.md`, `mechanics/digital_physics.md` |

---

## 3. Maintenance Protocol (維護協議)
*   **新增角色**: 請更新 `characters/` 下的對應檔案。
*   **新增地點**: 請更新 `world/setting.md` 或創建 `world/locations.md`。
*   **修改風格**: 若調整 Prompt 結構，請更新 `style/global_prompt.md`。
