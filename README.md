# 🎠 Lazy Susan Coin Game

A strategic puzzle game where you must get all coins to show the same face (all heads or all tails) by examining cups and flipping coins strategically.

## 🎯 Game Rules

### Setup
- Four upside-down red solo cups are arranged in a square on a Lazy Susan
- Under each cup is a coin (random arrangement of heads/tails, not all the same)
- Goal: Get all coins to be all heads or all tails

### Gameplay
1. **Select Cups**: Click on two cups to select them for examination
2. **Examine Cups**: Click "Examine Selected Cups" to see what's underneath
3. **Cups Become Locked**: Once examined, cups cannot be deselected
4. **Flip Individual Coins**: Click on any examined cup to flip its coin
5. **Spin Lazy Susan**: When ready, spin to check if you've won and reset the game

### Key Mechanics
- **Examination Phase**: Select 2 cups, examine them to see coin values
- **Flipping Phase**: Click examined cups to flip individual coins (no turn cost)
- **Spinning Phase**: Spin the Lazy Susan to check win condition and reset
- **Turn Counting**: Turns only increment when spinning the Lazy Susan
- **Win Condition**: All coins must be the same (checked only when spinning)

### Winning
- You win when all 4 coins show the same face (all heads or all tails)
- Win condition is only checked when you spin the Lazy Susan
- You have 50 spins to achieve victory

## 🧠 Optimal Strategy

### Guaranteed Win in ≤4 Spins

1. **Consistent Cup Selection**: Always choose cups in the same pattern (e.g., always adjacent)
2. **Strategic Flipping**: 
   - If you see two different coins, flip one to make them the same
   - If you see two same coins, don't flip them
3. **Multiple Attempts**: You can flip coins multiple times before spinning
4. **Systematic Approach**: Use the same cup selection pattern each time

### Why This Works
- With only 4 coins, you'll see all of them within 4 spins
- Making pairs the same creates a 'snowball effect'
- The strategy is deterministic and guaranteed to succeed
- You can experiment with different coin arrangements before spinning

## 🎮 How to Play

1. **Start the Game**: Run `python coin_game_gui.py`
2. **Select Two Cups**: Click on any two cups to select them
3. **Examine Cups**: Click "Examine Selected Cups" button
4. **See Coin Values**: Cups now show their coin values and become locked
5. **Flip Coins**: Click on examined cups to flip individual coins
6. **Spin When Ready**: Click "Spin Lazy Susan" to check for victory
7. **Repeat**: Continue until you win or reach 50 spins

## 🎨 Game Features

- **Visual Feedback**: Different colors for selected, examined, and normal cups
- **Real-time Updates**: See coin values change immediately after flipping
- **Turn Counter**: Track your progress toward the 50-spin limit
- **Strategy Hints**: Built-in strategy guide for optimal play
- **New Game**: Start fresh anytime with the New Game button

## 🚀 Getting Started

```bash
# Make sure you have Python installed
python coin_game_gui.py
```

## 🎯 Tips for Success

- **Be Patient**: Take your time to get the coins right before spinning
- **Plan Ahead**: Think about which cups to examine next
- **Learn Patterns**: Notice how your choices affect the game state
- **Practice**: The more you play, the better you'll understand the strategy

## 🔧 Technical Details

- Built with Python and Tkinter
- Cross-platform compatibility
- Responsive GUI with intuitive controls
- Debug logging for troubleshooting

---

**Good luck! Can you solve the Lazy Susan puzzle in the fewest spins possible?** 🎉
