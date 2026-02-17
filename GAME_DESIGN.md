# Chrono Shift - Game Design Document

## Overview
A puzzle-platformer where you control two characters in different time periods simultaneously. Navigate through temporal puzzles by coordinating actions between the past and present.

## Visual Style
- **Past Timeline:** Warm sepia tones, hand-drawn aesthetic, floating dust particles
- **Present Timeline:** Cool blues and cyans, digital/glitch effects, scanlines
- **Transition:** When both characters align, create a temporal rift visual effect (purple/gold energy)
- **Art Style:** Minimalist geometric with organic textures

## Gameplay Mechanics

### Core Mechanics
1. **Dual Character Control:** 
   - Press `1` to control Past character, `2` for Present character
   - Or use `Tab` to swap between characters
   - Both characters move simultaneously in their respective timelines

2. **Movement:**
   - Arrow keys or WASD for movement
   - Space to jump
   - Characters have slightly different physics (past is floaty, present is precise)

3. **Temporal Sync Points:**
   - When both characters occupy the same x-position in their timelines, a sync point activates
   - At sync points, platforms become interactive across timelines
   - Green = synchronized, Red = out of sync

4. **Level Progression:**
   - Reach the exit portal in both timelines to complete a level
   - Some exits only unlock when synced

### Controls
- **Arrow Keys / WASD:** Move left/right
- **Space:** Jump
- **1 / 2:** Switch timeline focus
- **Tab:** Toggle between timelines
- **R:** Restart level

### Level Design (5 Levels)
1. **Tutorial:** Basic movement in both timelines
2. **Jump Timing:** Learn to time jumps across timelines
3. **Sync Gates:** First sync point puzzle
4. **Platform Cooperation:** Use one character to help the other
5. **Final Challenge:** Complex temporal puzzle

## Technical Implementation
- Single HTML file with embedded CSS and JavaScript
- HTML5 Canvas rendering at 60fps
- No external dependencies
- Mobile: Touch controls (left/right buttons + jump)
- Responsive: Works on desktop and mobile
