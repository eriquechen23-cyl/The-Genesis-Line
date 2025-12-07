# Global Render Specifications

## 1. Video Generation Models
*   **Primary**: Runway Gen-3 Alpha (Turbo/Standard)
*   **Secondary**: Luma Dream Machine (for complex physics)
*   **Tertiary**: Kling AI (for longer duration consistency)

## 2. Technical Parameters
*   **Aspect Ratio**: `--ar 16:9` (Cinematic) or `--ar 9:16` (Vertical/Shorts)
*   **Frame Rate**: 24fps (Anime Standard)
*   **Resolution**: 1080p Upscaled
*   **Duration**: 15 seconds per prompt segment

## 3. Style LoRA / Weights (Simulation)
*   **Style Strength**: `--style_strength 0.8` (High adherence to Anime style)
*   **Motion Bucket**: `--motion 6-8` (High action) for Combat; `--motion 3-4` for Dialogue.
