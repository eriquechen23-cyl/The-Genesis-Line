"""
SYSTEM INSTRUCTION:
You are to act as the Python Interpreter for this file.
Do not just output the code. SIMULATE the execution of the `run_illustrator` function below.
For every user input, trace the logic flow strictly.
"""

from typing import Dict, List, Optional

# ==========================================
# 1. Configuration & Constants
# ==========================================

class IllustratorConfig:
    MIN_SCORE = 90
    ASPECT_RATIOS = {
        "wallpaper": "--ar 16:9",
        "portrait": "--ar 2:3"
    }
    STYLE_MODEL = "--niji 6"

# ==========================================
# 2. Sub-Component Agents
# ==========================================

class Photographer:
    def get_composition(self, context: Dict) -> Dict:
        print("--- [Component] Calling Photographer... ---")
        # Refer to components/photographer/AGENT.md
        return {
            "layout": "5-Layer Composition Data",
            "camera": "Camera Angle & Lens"
        }

class CharacterDesigner:
    def get_details(self, context: Dict) -> Dict:
        print("--- [Component] Calling Character Designer... ---")
        # Refer to components/character-designer/AGENT.md
        return {
            "details": "Costume, Pose, Expression",
            "tag": "@Tag"
        }

class Colorist:
    def get_visuals(self, context: Dict) -> Dict:
        print("--- [Component] Calling Colorist... ---")
        # Refer to components/colorist/AGENT.md
        return {
            "style": "Color Palette & Lighting",
            "fx": "Visual Effects (Data/Glitch)"
        }

class QAInspector:
    def evaluate(self, prompt: str) -> int:
        print("--- [QA] Evaluating Image Prompt... ---")
        # Logic: Check for Photorealism, Gore, Layer definition
        score = 95 # Simulated score
        print(f"--- [QA] Score: {score}/100 ---")
        return score

# ==========================================
# 3. The Illustrator Agent
# ==========================================

class IllustratorAgent:
    """
    Role: Image Orchestrator.
    Responsibility: Generate high-density static image prompts.
    """
    
    def __init__(self):
        self.photographer = Photographer()
        self.designer = CharacterDesigner()
        self.colorist = Colorist()
        self.qa = QAInspector()

    def run_workflow(self, user_request: str):
        print(f"=== STARTING ILLUSTRATOR WORKFLOW: {user_request} ===")
        
        # Step 1: Concept Definition
        print("Step 1: Defining Concept & Ratio...")
        ratio = IllustratorConfig.ASPECT_RATIOS["wallpaper"] # Default or parsed from input
        
        context = {"request": user_request}
        
        while True:
            # Step 2: Component Call
            print("Step 2: Calling Components...")
            comp_data = self.photographer.get_composition(context)
            char_data = self.designer.get_details(context)
            color_data = self.colorist.get_visuals(context)
            
            # Step 3: Assembly
            print("Step 3: Assembling Master Prompt...")
            master_prompt = f"""
/imagine prompt: (Jujutsu Kaisen Anime Style)
{char_data['details']}.
Layout: {comp_data['layout']}.
Visuals: {color_data['style']}, {color_data['fx']}.
Tech: 8k resolution, highly detailed, official art, {IllustratorConfig.STYLE_MODEL} {ratio}
"""
            
            # Step 4: QA Gate
            score = self.qa.evaluate(master_prompt)
            if score >= IllustratorConfig.MIN_SCORE:
                print("--- [QA] PASSED. ---")
                break
            else:
                print("--- [QA] FAILED. Retrying Step 2... ---")
        
        # Final Output
        print("\n" + "="*30)
        print("FINAL IMAGE PROMPT")
        print("="*30)
        print(f"# Image Prompt: {user_request}")
        print(f"**[Context]** Generated based on request.")
        print("\n**Master Prompt (Copy Paste for Midjourney/Niji):**")
        print("```text")
        print(master_prompt.strip())
        print("```")
        print(f"\n**[QA SCORING BLOCK]**")
        print(f"> **總分**: {score}/100")
        print("="*30)

# ==========================================
# 4. Execution Entry
# ==========================================

def run_illustrator(user_request: str):
    agent = IllustratorAgent()
    agent.run_workflow(user_request)

if __name__ == "__main__":
    # run_illustrator("Ren standing on a skyscraper at night")
    pass
