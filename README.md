# The Genesis Line: Studio Architecture

## Overview
This repository follows the **"Anime Studio Model"** structure, designed to simulate a professional animation production pipeline.

## Directory Structure

### 📂 00_World_Bible (The IP Core)
*   **Role**: The single source of truth for the IP.
*   **Contents**:
    *   `characters/`: Character profiles and visual tokens.
    *   `mechanics/`: Magic systems (Genesis Lines) and combat rules.
    *   `locations/`: World settings and maps.
    *   `style_guide/`: Visual directives (MAPPA style, color palettes).

### 📂 01_Pre_Production (Narrative Dept)
*   **Role**: Scriptwriting, Storyboarding, and World Building.
*   **Agent**: `The Showrunner` (Lead Narrator).
*   **Components**:
    *   `scriptwriter/`: Action choreography & philosophy.
    *   `world_architect/`: Environmental design.
    *   `storyboarder/`: Visual planning.

### 📂 02_Production (Visual Dept)
*   **Role**: Generating visual assets (Video & Image).
*   **Sub-Departments**:
    *   `video_dept/`: **The Director**. Focuses on timeline, camera movement, and 15s clips.
    *   `image_dept/`: **The Illustrator**. Focuses on high-res static composition and layering.

### 📂 03_Post_Production (Editing Dept)
*   **Role**: Sound design, video editing, and final polish.
*   *(Currently a placeholder for future expansion)*

### 📂 99_Archives (Storage)
*   **Role**: Storage for completed projects and past seasons.
*   **Contents**:
    *   `Season_1_The_Lost_Eden/`: Completed Season 1 assets.
    *   `Muscle_Line/`: Side projects.

## How to Use
1.  **Start at Root**: Open `AGENT.md` to see the Routing Protocol.
2.  **Select Intent**: Choose your task (Script, Video, Image).
3.  **Execute**: The system will route you to the correct department folder.
