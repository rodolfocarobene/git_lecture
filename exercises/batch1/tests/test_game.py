"""Test game module."""

import pytest
from tictactoe.game import TicTacToe


@pytest.fixture
def new_game():
    """Fixture for creating a new instance of the TicTacToe class."""
    return TicTacToe()


def test_initial_board(new_game):
    """Check the initial state of the game board."""
    assert new_game.board == [" " for _ in range(9)]


def test_valid_move(new_game):
    """Check a valid move on the game board."""
    assert new_game.is_valid_move(5)
    assert new_game.make_move(5, "X")
    assert new_game.board == [" ", " ", " ", " ", "X", " ", " ", " ", " "]


def test_invalid_move(new_game):
    """Check an invalid move on the game board."""
    assert not new_game.is_valid_move(0)
    assert not new_game.is_valid_move(10)


def test_winner_horizontal(new_game):
    """Check if a player wins horizontally."""
    new_game.make_move(1, "X")
    new_game.make_move(2, "X")
    new_game.make_move(3, "X")
    assert new_game.is_winner("X")


def test_winner_vertical(new_game):
    """Check if a player wins vertically."""
    new_game.make_move(1, "O")
    new_game.make_move(4, "O")
    new_game.make_move(7, "O")
    assert new_game.is_winner("O")


def test_winner_diagonal(new_game):
    """Check if a player wins diagonally."""
    new_game.make_move(1, "X")
    new_game.make_move(5, "X")
    new_game.make_move(9, "X")
    assert new_game.is_winner("X")


def test_board_full(new_game):
    """Check if the game board is full."""
    for i in range(1, 10, 2):
        new_game.make_move(i, "X")
    for i in range(2, 10, 2):
        new_game.make_move(i, "O")
    assert new_game.is_board_full()


def test_tie_game(new_game):
    """Check if the game results in a tie."""
    new_game.make_move(1, "X")
    new_game.make_move(2, "O")
    new_game.make_move(3, "X")
    new_game.make_move(4, "O")
    new_game.make_move(5, "X")
    new_game.make_move(6, "O")
    new_game.make_move(7, "X")
    new_game.make_move(8, "O")
    new_game.make_move(9, "X")
    assert new_game.is_board_full()
    assert new_game.is_winner("X")
    assert not new_game.is_winner("O")
