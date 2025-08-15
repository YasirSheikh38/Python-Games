import tkinter as tk
from tkinter import messagebox
import random

PLAYER_X = "X"
PLAYER_O = "O"

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.buttons = [[None]*3 for _ in range(3)]
        self.current = PLAYER_X
        self.create_widgets()
        self.mode = "pvp"  # Change to "pve" for vs AI

    def create_widgets(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.master, text="", font=("Arial", 40), width=5, height=2,
                                command=lambda row=r, col=c: self.click(row, col))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

        self.reset_button = tk.Button(self.master, text="Reset", font=("Arial", 16),
                                      command=self.reset_board)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def click(self, row, col):
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current} wins!")
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.switch_player()
                if self.mode == "pve" and self.current == PLAYER_O:
                    self.ai_move()

    def switch_player(self):
        self.current = PLAYER_O if self.current == PLAYER_X else PLAYER_X

    def check_winner(self):
        # Rows and columns
        for i in range(3):
            if (self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != ""):
                return self.buttons[i][0]["text"]
            if (self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != ""):
                return self.buttons[0][i]["text"]
        # Diagonals
        if (self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != ""):
            return self.buttons[0][0]["text"]
        if (self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != ""):
            return self.buttons[0][2]["text"]
        return None

    def is_draw(self):
        return all(self.buttons[r][c]["text"] != "" for r in range(3) for c in range(3)) and not self.check_winner()

    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]["text"] = ""
        self.current = PLAYER_X

    def ai_move(self):
        # Simple AI: Random empty cell
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.buttons[r][c]["text"] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.buttons[row][col]["text"] = self.current
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current} wins!")
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.switch_player()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
