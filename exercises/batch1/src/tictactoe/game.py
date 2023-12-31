"""TicTacToe example."""


class TicTacToe:
    """Represent a Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize a new instance of the TicTacToe class with an empty board."""
        self.board = [" " for _ in range(9)]  # Empty board represented by a list

    def print_board(self):
        """Print the current state of the game board."""
        for row in [self.board[i : i + 3] for i in range(0, 9, 3)]:
            print("| " + " | ".join(row) + " |")

    def is_winner(self, player):
        """Check if the specified player has won the game.

        Parameters:
        - player (str): The player to check for a win ('X' or 'O').

        Returns:
        - bool: True if the player has won, False otherwise.
        """
        # Check rows, columns, and diagonals
        for i in range(0, 9, 3):
            if self.board[i : i + 3] == [player, player, player]:
                return True
            if self.board[i : i + 7 : 3] == [player, player, player]:
                return True

        if self.board[0:9:4] == [player, player, player] or self.board[2:7:2] == [
            player,
            player,
            player,
        ]:
            return True

        for i in range(3):
            if self.board[i:9:3] == [player, player, player]:
                return True

        return False

    def is_board_full(self):
        """Check if the game board is full, indicating a tie.

        Returns:
        - bool: True if the board is full, False otherwise.
        """
        return " " not in self.board

    def is_valid_move(self, position):
        """Check if the specified move is valid.

        Parameters:
        - position (int): The position where the player wants to make a move.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        return 1 <= position <= 9 and self.board[position - 1] == " "

    def make_move(self, position, player):
        """Make a move on the game board.

        Parameters:
        - position (int): The position where the player wants to make a move.
        - player (str): The player making the move ('X' or 'O').

        Returns:
        - bool: True if the move is successful, False otherwise.
        """
        if self.is_valid_move(position):
            self.board[position - 1] = player
            return True
        else:
            return False


# Example of how to use the TicTacToe module
if __name__ == "__main__":
    game = TicTacToe()
    current_player = "X"

    while not game.is_board_full():
        game.print_board()
        position = int(input(f"Player {current_player}, enter your move (1-9): "))

        if game.make_move(position, current_player):
            if game.is_winner(current_player):
                print(f"Player {current_player} wins!")
                break
            elif game.is_board_full():
                print("It's a tie!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
