import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

class CoinGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lazy Susan Coin Game")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Game state
        self.coins = []
        self.turn_count = 0
        self.max_turns = 50
        self.game_mode = "human"
        self.selected_cups = []
        self.game_active = False
        self.cups_examined = set()  # Track which cups have been examined
        
        # Colors
        self.colors = {
            'bg': '#2c3e50',
            'cup_normal': '#34495e',
            'cup_selected': '#e74c3c',
            'cup_highlight': '#f39c12',
            'text': '#ecf0f1',
            'button': '#3498db',
            'button_hover': '#2980b9'
        }
        
        self.setup_ui()
        self.initialize_game()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Title
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text="🎠 LAZY SUSAN COIN GAME 🎠", 
            font=('Arial', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        title_label.pack()
        
        # Game info
        info_frame = tk.Frame(self.root, bg=self.colors['bg'])
        info_frame.pack(pady=10)
        
        self.turn_label = tk.Label(
            info_frame,
            text="Turn: 1/50",
            font=('Arial', 14),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        self.turn_label.pack()
        
        self.mode_label = tk.Label(
            info_frame,
            text="Mode: Human Play",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        self.mode_label.pack()
        
        # Cups display
        cups_frame = tk.Frame(self.root, bg=self.colors['bg'])
        cups_frame.pack(pady=30)
        
        self.cup_buttons = []
        for i in range(4):
            row = i // 2
            col = i % 2
            
            cup_btn = tk.Button(
                cups_frame,
                text=f"CUP {i+1}",
                font=('Arial', 16, 'bold'),
                width=8,
                height=3,
                bg=self.colors['cup_normal'],
                fg=self.colors['text'],
                relief='raised',
                bd=3,
                command=lambda idx=i: self.select_cup(idx)
            )
            cup_btn.grid(row=row, column=col, padx=10, pady=10)
            self.cup_buttons.append(cup_btn)
            
        # Action buttons
        action_frame = tk.Frame(self.root, bg=self.colors['bg'])
        action_frame.pack(pady=20)
        
        self.examine_btn = tk.Button(
            action_frame,
            text="Examine Selected Cups",
            font=('Arial', 12, 'bold'),
            bg=self.colors['button'],
            fg=self.colors['text'],
            relief='raised',
            bd=2,
            command=self.examine_cups,
            state='disabled'
        )
        self.examine_btn.pack(side=tk.LEFT, padx=10)
        
        self.spin_btn = tk.Button(
            action_frame,
            text="Spin Lazy Susan",
            font=('Arial', 12, 'bold'),
            bg=self.colors['button'],
            fg=self.colors['text'],
            relief='raised',
            bd=2,
            command=self.spin_lazy_susan
        )
        self.spin_btn.pack(side=tk.LEFT, padx=10)
        
        # Flip options (initially hidden)
        self.flip_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.flip_frame.pack(pady=20)
        
        self.flip_label = tk.Label(
            self.flip_frame,
            text="Which coins would you like to flip?",
            font=('Arial', 12, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        self.flip_label.pack()
        
        flip_buttons_frame = tk.Frame(self.flip_frame, bg=self.colors['bg'])
        flip_buttons_frame.pack(pady=10)
        
        self.flip_none_btn = tk.Button(
            flip_buttons_frame,
            text="Flip Neither",
            font=('Arial', 10),
            bg=self.colors['button'],
            fg=self.colors['text'],
            command=lambda: self.flip_coins(0)
        )
        self.flip_none_btn.pack(side=tk.LEFT, padx=5)
        
        self.flip_first_btn = tk.Button(
            flip_buttons_frame,
            text="Flip First Cup",
            font=('Arial', 10),
            bg=self.colors['button'],
            fg=self.colors['text'],
            command=lambda: self.flip_coins(1)
        )
        self.flip_first_btn.pack(side=tk.LEFT, padx=5)
        
        self.flip_second_btn = tk.Button(
            flip_buttons_frame,
            text="Flip Second Cup",
            font=('Arial', 10),
            bg=self.colors['button'],
            fg=self.colors['text'],
            command=lambda: self.flip_coins(2)
        )
        self.flip_second_btn.pack(side=tk.LEFT, padx=5)
        
        self.flip_both_btn = tk.Button(
            flip_buttons_frame,
            text="Flip Both Cups",
            font=('Arial', 10),
            bg=self.colors['button'],
            fg=self.colors['text'],
            command=lambda: self.flip_coins(3)
        )
        self.flip_both_btn.pack(side=tk.LEFT, padx=5)
        
        # Hide flip options initially
        self.flip_frame.pack_forget()
        
        # Game control buttons
        control_frame = tk.Frame(self.root, bg=self.colors['bg'])
        control_frame.pack(pady=20)
        
        self.new_game_btn = tk.Button(
            control_frame,
            text="New Game",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg=self.colors['text'],
            relief='raised',
            bd=2,
            command=self.new_game
        )
        self.new_game_btn.pack(side=tk.LEFT, padx=10)
        
        self.strategy_btn = tk.Button(
            control_frame,
            text="Strategy Hint",
            font=('Arial', 12, 'bold'),
            bg='#f39c12',
            fg=self.colors['text'],
            relief='raised',
            bd=2,
            command=self.show_strategy
        )
        self.strategy_btn.pack(side=tk.LEFT, padx=10)
        
        # Status display
        self.status_label = tk.Label(
            self.root,
            text="Welcome! Select two cups to examine.",
            font=('Arial', 12),
            bg=self.colors['bg'],
            fg=self.colors['text'],
            wraplength=700
        )
        self.status_label.pack(pady=20)
        
    def initialize_game(self):
        """Initialize a new game"""
        while True:
            self.coins = [random.choice(['H', 'T']) for _ in range(4)]
            if len(set(self.coins)) > 1:
                break
        self.turn_count = 0
        self.selected_cups = []
        self.game_active = True
        self.cups_examined = set()  # Reset examined cups
        
        self.update_display()
        self.hide_flip_options()
        
    def update_display(self):
        """Update the display"""
        self.turn_label.config(text=f"Turn: {self.turn_count + 1}/{self.max_turns}")
        self.mode_label.config(text=f"Mode: {'Blind' if self.game_mode == 'blind' else 'Human'} Play")
        
        # Update cup buttons
        for i, btn in enumerate(self.cup_buttons):
            if i in self.selected_cups:
                btn.config(bg=self.colors['cup_selected'])
            elif i in self.cups_examined:
                # Examined cups get a different color to show they can be clicked to flip
                btn.config(bg=self.colors['cup_highlight'])
            else:
                btn.config(bg=self.colors['cup_normal'])
            
            # Only show coin values if cups have been examined
            if hasattr(self, 'cups_examined') and i in self.cups_examined:
                if self.game_mode == 'human':
                    coin_text = f"\n{'Heads' if self.coins[i] == 'H' else 'Tails'}\n"
                else:
                    coin_text = f"CUP {i+1}\n???\n(Click to flip)"
            else:
                coin_text = f"CUP {i+1}"
            btn.config(text=coin_text)
                
        # Update examine button state
        if len(self.selected_cups) == 2:
            self.examine_btn.config(state='normal')
        else:
            self.examine_btn.config(state='disabled')
            
    def select_cup(self, cup_index):
        """Handle cup selection"""
        print(f"DEBUG: select_cup called with index: {cup_index}")
        print(f"DEBUG: game_active: {self.game_active}")
        
        if not self.game_active:
            print("DEBUG: Cup selection blocked - game not active")
            return
        
        # If cup is already examined, flip the coin instead of selecting
        if cup_index in self.cups_examined:
            print(f"DEBUG: Cup {cup_index} is examined, flipping coin instead")
            self.flip_single_coin(cup_index)
            return
            
        if cup_index in self.selected_cups:
            # Deselect cup (only if not examined)
            print(f"DEBUG: Deselecting cup {cup_index}")
            self.selected_cups.remove(cup_index)
        else:
            # Select cup
            if len(self.selected_cups) < 2:
                print(f"DEBUG: Adding cup {cup_index} to selection")
                self.selected_cups.append(cup_index)
            else:
                # Replace first selection
                print(f"DEBUG: Replacing first selection with cup {cup_index}")
                self.selected_cups[0] = cup_index
                
        print(f"DEBUG: Updated selected_cups: {self.selected_cups}")
        self.update_display()
        
    def examine_cups(self):
        """Examine the selected cups"""
        print(f"DEBUG: examine_cups called with selected_cups: {self.selected_cups}")
        print(f"DEBUG: game_mode: {self.game_mode}")
        print(f"DEBUG: game_active: {self.game_active}")
        
        if len(self.selected_cups) != 2:
            print(f"DEBUG: Wrong number of cups selected: {len(self.selected_cups)}")
            return
            
        # Mark these cups as examined
        self.cups_examined.update(self.selected_cups)
        
        if self.game_mode == 'blind':
            print("DEBUG: Blind mode - showing flip options")
            self.status_label.config(text="You cannot see the coins in blind mode! Choose your flip strategy.")
        else:
            cup1, cup2 = self.selected_cups
            coin1, coin2 = self.coins[cup1], self.coins[cup2]
            print(f"DEBUG: Human mode - showing coins: Cup {cup1+1}={coin1}, Cup {cup2+1}={coin2}")
            self.status_label.config(text="You can see the coin values under each cup. Choose your flip strategy.")
            
        print("DEBUG: About to call show_flip_options")
        self.update_display()  # Update display to show coin values
        self.show_flip_options()
        
    def show_flip_options(self):
        """Show the flip options"""
        print("DEBUG: show_flip_options called")
        print(f"DEBUG: flip_frame exists: {self.flip_frame is not None}")
        print(f"DEBUG: flip_frame.winfo_exists(): {self.flip_frame.winfo_exists()}")
        
        try:
            self.flip_frame.pack()
            print("DEBUG: flip_frame.pack() successful")
        except Exception as e:
            print(f"DEBUG: Error packing flip_frame: {e}")
            
        self.examine_btn.config(state='disabled')
        print("DEBUG: examine_btn disabled")
        
    def hide_flip_options(self):
        """Hide the flip options"""
        try:
            if self.flip_frame.winfo_exists():
                self.flip_frame.pack_forget()
                print("DEBUG: flip_frame hidden successfully")
            else:
                print("DEBUG: flip_frame doesn't exist, can't hide")
        except Exception as e:
            print(f"DEBUG: Error hiding flip_frame: {e}")
            
        self.examine_btn.config(state='normal')
        print("DEBUG: examine_btn enabled")
        
    def flip_coins(self, choice):
        """Apply coin flips based on choice"""
        if len(self.selected_cups) != 2:
            return
            
        cup1, cup2 = self.selected_cups
        
        if choice == 1:  # Flip first cup
            self.coins[cup1] = 'T' if self.coins[cup1] == 'H' else 'H'
            self.status_label.config(text=f"Flipped cup {cup1+1} to {'Heads' if self.coins[cup1] == 'H' else 'Tails'}")
        elif choice == 2:  # Flip second cup
            self.coins[cup2] = 'T' if self.coins[cup2] == 'H' else 'H'
            self.status_label.config(text=f"Flipped cup {cup2+1} to {'Heads' if self.coins[cup2] == 'H' else 'Tails'}")
        elif choice == 3:  # Flip both cups
            self.coins[cup1] = 'T' if self.coins[cup1] == 'H' else 'H'
            self.coins[cup2] = 'T' if self.coins[cup2] == 'H' else 'H'
            self.status_label.config(text="Flipped both cups!")
        else:  # No flip
            self.status_label.config(text="No coins flipped.")
            
        self.hide_flip_options()
        self.selected_cups = []
        
        # Check win condition
        if self.check_win_condition():
            self.game_won()
        else:
            # Update display after coin flips to show new coin values
            self.update_display()
    
    def flip_single_coin(self, cup_index):
        """Flip a single coin when clicking on an examined cup"""
        if cup_index not in self.cups_examined:
            return
            
        # Flip the coin
        self.coins[cup_index] = 'T' if self.coins[cup_index] == 'H' else 'H'
        print(f"DEBUG: Flipped single coin in cup {cup_index} to {self.coins[cup_index]}")
        
        # Update status
        self.status_label.config(text=f"Flipped cup {cup_index+1} to {'Heads' if self.coins[cup_index] == 'H' else 'Tails'}")
        
        # Update display to show new coin value
        self.update_display()
                
    def check_win_condition(self):
        """Check if all coins are the same"""
        return len(set(self.coins)) == 1
        
    def game_won(self):
        """Handle game win"""
        self.game_active = False
        messagebox.showinfo(
            "Congratulations! 🎉",
            f"You won in {self.turn_count + 1} turns!\nFinal state: {self.coins}"
        )
        self.status_label.config(text="🎉 YOU WON! 🎉")
        
    def game_lost(self):
        """Handle game loss"""
        self.game_active = False
        messagebox.showinfo(
            "Game Over 😔",
            f"You didn't win within {self.max_turns} turns.\nFinal state: {self.coins}"
        )
        self.status_label.config(text="😔 Game Over - You didn't win within the time limit.")
        
    def spin_lazy_susan(self):
        """Simulate spinning the Lazy Susan"""
        if not self.game_active:
            return
            
        self.status_label.config(text="🎠 Spinning the Lazy Susan...")
        self.root.update()
        time.sleep(1)
        
        # Check win condition before resetting
        if self.check_win_condition():
            self.game_won()
            return
        
        # Increment turn count when spinning
        self.turn_count += 1
        if self.turn_count >= self.max_turns:
            self.game_lost()
            return
        
        # Clear selection and hide flip options
        self.selected_cups = []
        self.cups_examined = set()  # Reset examined cups after spinning
        try:
            self.hide_flip_options()
        except Exception as e:
            print(f"DEBUG: Error in spin_lazy_susan when hiding flip options: {e}")
        self.update_display()
        
        self.status_label.config(text="The Lazy Susan has spun! Select two cups to examine.")
        
    def new_game(self):
        """Start a new game"""
        self.initialize_game()
        self.status_label.config(text="New game started! Select two cups to examine.")
        self.update_display()  # Ensure display is updated for new game
        
    def toggle_mode(self):
        """Toggle between human and blind modes"""
        if self.game_mode == 'human':
            self.game_mode = 'blind'
            self.mode_btn.config(text="Switch to Human Mode")
        else:
            self.game_mode = 'human'
            self.mode_btn.config(text="Switch to Blind Mode")
            
        # Reset examined cups when switching modes
        self.cups_examined = set()
        self.update_display()
        
    def show_strategy(self):
        """Show strategy hint"""
        strategy_text = """OPTIMAL STRATEGY (Guaranteed win in ≤4 turns):

1. Always choose cups in a consistent pattern (e.g., always adjacent)
2. If you see two different coins, flip one to make them the same
3. If you see two same coins, don't flip them

BLIND MODE STRATEGY:
- Use the same consistent cup selection pattern
- Always flip exactly one coin (creates pairs)
- This also guarantees a win in ≤4 turns!

Why this works:
- With only 4 coins, you'll see all of them within 4 turns
- Making pairs the same creates a 'snowball effect'
- The strategy is deterministic and guaranteed to succeed!"""
        
        messagebox.showinfo("Strategy Hint", strategy_text)

def main():
    root = tk.Tk()
    app = CoinGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
