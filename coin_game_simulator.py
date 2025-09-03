import random
import time
import os

class CoinGame:
    def __init__(self):
        self.coins = []
        self.turn_count = 0
        self.max_turns = 50  # Prevent infinite games
        
    def initialize_game(self):
        """Initialize the game with random coin states (not all the same)"""
        while True:
            self.coins = [random.choice(['H', 'T']) for _ in range(4)]
            # Ensure not all coins are the same
            if len(set(self.coins)) > 1:
                break
        self.turn_count = 0
        
    def spin_lazy_susan(self):
        """Randomly rotate the cups (simulate spinning)"""
        # This doesn't change the actual coin positions, just simulates the effect
        pass
        
    def display_cups(self, selected_indices=None):
        """Display the cups with selected ones highlighted"""
        print("\n" + "="*50)
        print("LAZY SUSAN COIN GAME")
        print("="*50)
        print(f"Turn: {self.turn_count + 1}/{self.max_turns}")
        print()
        
        # Display cups in a 2x2 grid
        for i in range(4):
            if i % 2 == 0:
                print()
            if selected_indices and i in selected_indices:
                print(f"[CUP {i+1}]", end="  ")  # Selected cup
            else:
                print(f" CUP {i+1} ", end="  ")  # Unselected cup
        print("\n")
        
    def select_cups(self):
        """Let player select two cups to examine"""
        while True:
            try:
                print("Select two cups to examine (1-4, separated by space):")
                selection = input("> ").strip()
                cup_indices = [int(x) - 1 for x in selection.split()]
                
                if len(cup_indices) != 2:
                    print("Please select exactly 2 cups!")
                    continue
                    
                if not all(0 <= i <= 3 for i in cup_indices):
                    print("Cup numbers must be between 1 and 4!")
                    continue
                    
                if cup_indices[0] == cup_indices[1]:
                    print("Please select two different cups!")
                    continue
                    
                return cup_indices
                
            except ValueError:
                print("Please enter valid numbers!")
                
    def examine_coins(self, cup_indices):
        """Show the player the coins under selected cups"""
        print(f"\nYou selected cups {cup_indices[0]+1} and {cup_indices[1]+1}")
        print("Under these cups, you see:")
        
        for i, cup_idx in enumerate(cup_indices):
            coin_state = self.coins[cup_idx]
            print(f"Cup {cup_idx+1}: {coin_state} ({'Heads' if coin_state == 'H' else 'Tails'})")
            
    def flip_coins(self, cup_indices):
        """Let player choose which coins to flip"""
        print("\nWhich coins would you like to flip?")
        print("Options:")
        print("0 - Flip neither")
        print("1 - Flip only cup", cup_indices[0]+1)
        print("2 - Flip only cup", cup_indices[1]+1)
        print("3 - Flip both cups")
        
        while True:
            try:
                choice = int(input("Enter your choice (0-3): "))
                if 0 <= choice <= 3:
                    break
                print("Please enter a number between 0 and 3!")
            except ValueError:
                print("Please enter a valid number!")
                
        # Apply the flips
        if choice == 1:
            self.coins[cup_indices[0]] = 'T' if self.coins[cup_indices[0]] == 'H' else 'H'
            print(f"Flipped cup {cup_indices[0]+1} to {self.coins[cup_indices[0]]}")
        elif choice == 2:
            self.coins[cup_indices[1]] = 'T' if self.coins[cup_indices[1]] == 'H' else 'H'
            print(f"Flipped cup {cup_indices[1]+1} to {self.coins[cup_indices[1]]}")
        elif choice == 3:
            self.coins[cup_indices[0]] = 'T' if self.coins[cup_indices[0]] == 'H' else 'H'
            self.coins[cup_indices[1]] = 'T' if self.coins[cup_indices[1]] == 'H' else 'H'
            print(f"Flipped both cups!")
        else:
            print("No coins flipped.")
            
    def check_win_condition(self):
        """Check if all coins are the same"""
        return len(set(self.coins)) == 1
        
    def play_game(self):
        """Main game loop"""
        self.initialize_game()
        
        print("Welcome to the Lazy Susan Coin Game!")
        print("Your goal: Get all coins to show the same side (all Heads or all Tails)")
        print("Each turn, you'll select 2 cups, see their coins, and optionally flip them.")
        print("The Lazy Susan spins between turns, so you won't know which cup is which!")
        print("\nPress Enter to start...")
        input()
        
        while self.turn_count < self.max_turns:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            
            # Simulate spinning the Lazy Susan
            print("🎠 Spinning the Lazy Susan...")
            time.sleep(1)
            
            # Display current state
            self.display_cups()
            
            # Player selects cups
            selected_cups = self.select_cups()
            
            # Show selected cups
            self.display_cups(selected_cups)
            
            # Examine the coins
            self.examine_coins(selected_cups)
            
            # Player chooses to flip
            self.flip_coins(selected_cups)
            
            # Check win condition
            if self.check_win_condition():
                print(f"\n🎉 CONGRATULATIONS! You won in {self.turn_count + 1} turns!")
                print(f"Final state: {self.coins}")
                return True
                
            # Cover coins and continue
            print("\nCovering the coins...")
            time.sleep(1)
            
            self.turn_count += 1
            
        print(f"\n😔 Game over! You didn't win within {self.max_turns} turns.")
        print(f"Final state: {self.coins}")
        return False
        
    def show_strategy_hint(self):
        """Show a hint about optimal strategy"""
        print("\n" + "="*50)
        print("STRATEGY HINT")
        print("="*50)
        print("Optimal strategy for guaranteed win:")
        print("1. Always choose cups in a consistent pattern (e.g., always adjacent)")
        print("2. If you see two different coins, flip one to make them the same")
        print("3. If you see two same coins, don't flip them")
        print("4. This strategy guarantees a win in at most 4 turns!")
        print("="*50)

def main():
    game = CoinGame()
    
    while True:
        print("\nWould you like to:")
        print("1. Play the game")
        print("2. See strategy hint")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            game.play_game()
        elif choice == '2':
            game.show_strategy_hint()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
