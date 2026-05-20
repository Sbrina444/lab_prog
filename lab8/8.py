import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.resizable(True, True)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.game_over = False

        self.create_widgets()

        self.center_window()

        self.window.minsize(500, 600)

    def center_window(self):
        self.window.update_idletasks()
        width = 650
        height = 700
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        main_frame = tk.Frame(self.window, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(
            main_frame,
            text="КРЕСТИКИ-НОЛИКИ",
            font=("Arial", 28, "bold"),
            fg="#2c3e50",
            bg="white"
        )
        title_label.pack(pady=(20, 10))

        self.status_label = tk.Label(
            main_frame,
            text="Ход игрока X",
            font=("Arial", 16, "bold"),
            fg="#e74c3c",
            bg="white"
        )
        self.status_label.pack(pady=(0, 20))

        game_container = tk.Frame(main_frame, bg="#2c3e50", padx=3, pady=3)
        game_container.pack(pady=20, expand=True)

        self.game_frame = tk.Frame(game_container, bg="#2c3e50")
        self.game_frame.pack()

        button_size = 80

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.game_frame,
                    text="",
                    font=("Arial", 48, "bold"),
                    width=4,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col),
                    relief=tk.RAISED,
                    borderwidth=3,
                    bg="#ecf0f1",
                    fg="#2c3e50",
                    activebackground="#bdc3c7"
                )
                self.buttons[i][j].grid(row=i, column=j, padx=2, pady=2)

        control_frame = tk.Frame(main_frame, bg="white")
        control_frame.pack(pady=20)

    def make_move(self, row, col):
        if self.board[row][col] != "" or self.game_over:
            return

        if self.current_player == "X":
            color = "#e74c3c"
            text_color = "#e74c3c"
        else:
            color = "#27ae60"
            text_color = "#27ae60"

        self.buttons[row][col].config(
            text=self.current_player,
            fg=text_color,
            font=("Arial", 52, "bold"),
            state=tk.DISABLED,
            disabledforeground=text_color,
            bg="#ffffff"
        )

        self.board[row][col] = self.current_player

        if self.check_win():
            self.game_over = True
            winner = "X" if self.current_player == "X" else "O"
            messagebox.showinfo("Победа!", f"Победил игрок {winner}!")
            self.status_label.config(text=f"Победил {winner}!", fg="#f39c12")
            self.disable_all_buttons()
            return

        if self.check_draw():
            self.game_over = True
            messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
            self.status_label.config(text="Ничья!", fg="#95a5a6")
            return

        self.current_player = "O" if self.current_player == "X" else "X"

        if self.current_player == "X":
            self.status_label.config(text="Ход игрока X", fg="#e74c3c")
        else:
            self.status_label.config(text="Ход игрока O", fg="#27ae60")

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                self.highlight_winning_cells([(i, 0), (i, 1), (i, 2)])
                return True

        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                self.highlight_winning_cells([(0, j), (1, j), (2, j)])
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.highlight_winning_cells([(0, 0), (1, 1), (2, 2)])
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.highlight_winning_cells([(0, 2), (1, 1), (2, 0)])
            return True

        return False

    def highlight_winning_cells(self, cells):
        for row, col in cells:
            self.buttons[row][col].config(
                bg="#f1c40f",
                activebackground="#f1c40f"
            )

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['state'] != tk.DISABLED:
                    self.buttons[i][j].config(state=tk.DISABLED)

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text="",
                    state=tk.NORMAL,
                    bg="#ecf0f1",
                    fg="#2c3e50",
                    disabledforeground="#2c3e50"
                )

        self.status_label.config(text="Ход игрока X", fg="#e74c3c")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()