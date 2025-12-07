# DIRECTOR'S PROTOCOLS: Output Template

**[FILE: outputs/08_FinalPrompt_Clip{N}.md]**

# Video Prompt: {Slug} (Clip {N})

**[State]** {Time/Location/Context}

**[MONTAGE SEQUENCE] (Storyboarder's Blueprint):**
> `Sequence: [Beat 1: {Shot Type}] -> [Beat 2: {Shot Type}] -> [Beat 3: {Shot Type}]`

**[COMPOSITION LAYERS] (Painter's Stack):**
> Ref: {production/cinematographer/AGENT.md}
*   **L1 (Foreground)**: {Elements closest to camera}
*   **L2 (Character)**: {Main Subject Focus, @Tag action details}
*   **L3 (Midground)**: {Immediate environment}
*   **L4 (Background)**: {World setting}
*   **L5 (VFX/Atmosphere)**: {Lighting, fog, particles}

**[AUDIO & VOICE] (Sound Designer's Mix):**
> Ref: {post_production/sound-designer/AGENT.md}
*   **CV**: {Character Name} (Type: {Voice Type})
*   **BGM**: {Music Track Name/Style}

**Time-Coded Beats (Sora Guide):**
*   **[0.0s] Beats1**: **[{Shot Type}]** {Action & Camera}
    *   **L1 (FG)**: {Foreground Details}
    *   **L2 (Char)**: {Character Action & Details}
    *   **L3 (MG)**: {Midground Details}
    *   **L4 (BG)**: {Background Details}
    *   **L5 (VFX)**: {Atmosphere & Lighting}
    *   **Dialogue**: "[{Japanese Line}]" **SFX**: "[{Katakana}] ({Meaning})"
*   **[X.Xs] Beats2**: **[{Shot Type}]** {Action & Camera}
    *   **L1 (FG)**: {Foreground Details}
    *   **L2 (Char)**: {Character Action & Details}
    *   **L3 (MG)**: {Midground Details}
    *   **L4 (BG)**: {Background Details}
    *   **L5 (VFX)**: {Atmosphere & Lighting}
    *   **Dialogue**: "[{Japanese Line}]" **SFX**: "[{Katakana}] ({Meaning})"
> ...until all beats are listed...

**Master Prompt (Sora Optimized):**
> {core/prompt_engineer.md}
> **[Camera]**: {production/cinematographer/AGENT.md}
> **[Style]**: {production/art-director/AGENT.md}
> **[Audio]**: {post_production/sound-designer/AGENT.md}

**[TECHNICAL SPECS] (Render Config):**
*   **Model**: Runway Gen-3 Alpha
*   **Aspect Ratio**: --ar 16:9
*   **Frame Rate**: 24fps
*   **Motion Bucket**: {Value}
*   **Micro-QA**: {post_production/beat-inspector/AGENT.md}

**[NEGATIVE PROMPT] (Safety Protocol):**
> {core/negative_prompt.md}

**[CRITIC'S VERDICT]**
> **Score**: {post_production/critic/AGENT.md}/100
> **Comment**: {post_production/critic/AGENT.md}
