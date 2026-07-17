#Task6 More on Classes
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Board: 
    valid_moves = [
        "upper left", "upper center", "upper right", 
        "middle left", "center", "middle right", 
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" ", " ", " "] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    # FIXED: Indented correctly to be inside the Board class
    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3 
        column = move_index % 3 
        
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
            
        self.board_array[row][column] = self.turn
        self.last_move = move_string # FIXED: Correctly tracking last_move as requested
        
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    def whats_next(self):
        # FIXED: Simplified, foolproof tie-game check
        # If there are no spaces left anywhere on the board, it's a tie
        cat = all(cell != " " for row in self.board_array for cell in row)
        
        win = False
        for i in range(3): # check rows
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                    win = True
                    break
                    
        if not win:
            for i in range(3): # check columns
                if self.board_array[0][i] != " ":
                    if self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                        win = True
                        break
                        
        if not win:
            if self.board_array[1][1] != " ": # check diagonals
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                    win = True
                    
        # Process outcomes in correct priority order: Win takes priority over a Tie
        if win:
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")
                
        if cat:
            return (True, "Cat's Game.")
            
        return (False, f"{self.turn}'s turn.")