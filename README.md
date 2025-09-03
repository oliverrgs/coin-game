# Lazy Susan Coin Game Simulator

A Python simulator for the fascinating Lazy Susan coin puzzle game, complete with multiple game modes and AI demonstrations of optimal strategies.

## Game Rules

You are shown a Lazy Susan with four upside-down red solo cups arranged in a square. Under each cup is a coin showing either heads (H) or tails (T). The coins start in a random arrangement where not all are the same.

**Goal**: Get all coins to show the same side (all heads or all tails).

**Each Turn**:
1. The Lazy Susan spins (you can't know which cup is which)
2. You select two cups to examine
3. You can see the coins under those cups
4. You can flip 0, 1, or both of those coins
5. The cups are covered again and the process repeats

## How to Play

### Basic Game
```bash
python coin_game_simulator.py
```

### Advanced Features
```bash
python advanced_coin_game.py
```

The advanced version includes:
- Human play mode (can see coins)
- Blind play mode (cannot see coins)
- AI demonstration of optimal strategy
- AI demonstration of random strategy
- Strategy analysis

## Optimal Strategy

**The optimal strategy guarantees a win in at most 4 turns:**

1. **Always choose cups in a consistent pattern** (e.g., always choose adjacent cups)
2. **If you see two different coins**, flip one to make them the same
3. **If you see two same coins**, don't flip them

**Why this works:**
- By choosing the same pattern each time, you eventually see all coins
- Making pairs the same creates a "snowball effect"
- The strategy is deterministic and guaranteed to succeed

## Blind Variant Strategy

Even if you can't see the coins, you can still guarantee a win:

1. **Always choose cups in a consistent pattern**
2. **Always flip exactly one coin** (creates pairs)
3. **This also guarantees a win in ≤4 turns!**

## Mathematical Proof

The optimal strategy works because:
- There are only 4 coins, so you'll see all of them within 4 turns
- Making pairs the same increases the probability of winning
- The strategy is memoryless and doesn't require tracking previous states

## Game Modes

1. **Human Play**: You can see the coins and make informed decisions
2. **Blind Play**: You cannot see the coins - pure strategy game
3. **Optimal AI**: Watch the AI demonstrate the optimal strategy
4. **Random AI**: Watch the AI use random moves (much less effective)

## Example Game Flow

```
Turn 1: Choose cups 1 & 2, see H & T, flip one → H & H
Turn 2: Choose cups 1 & 2, see H & H, no flip needed
Turn 3: Choose cups 1 & 2, see H & H, no flip needed
Turn 4: Choose cups 1 & 2, see H & H, no flip needed
WIN! All coins are heads
```

## Why Random Strategy Fails

A random strategy has no guarantee of winning because:
- You might never see all coins
- Random flips can undo progress
- No systematic approach to creating pairs

## Educational Value

This game demonstrates:
- **Deterministic vs. probabilistic strategies**
- **Information theory** (what you can and cannot know)
- **Game theory** (optimal decision making)
- **Algorithm design** (guaranteed solutions)

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Running the Simulator

1. Download the Python files
2. Open a terminal/command prompt
3. Navigate to the directory containing the files
4. Run `python advanced_coin_game.py`
5. Choose your game mode and enjoy!

## Strategy Challenge

Try to:
1. Win the game in the fewest turns possible
2. Develop your own strategy and compare it to the optimal one
3. Understand why the blind variant strategy works
4. Analyze what information is actually needed to guarantee a win

This game is a perfect example of how mathematical thinking can turn an apparently random puzzle into a solvable problem with a guaranteed solution!
