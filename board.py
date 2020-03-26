import numpy as np
from typing import List, Tuple

class Piece:

    def __init__(self, size: int, color: str) -> None:
        self.size = size
        self.color = color

    def __eq__(self, other):
        return self.size == other.size and self.color == other.color

    def __ne__(self, other):
        return self.size != other.size or self.color != other.color

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __repr__(self):
        return "(%s, %s)" % (self.size, self.color)

class Board:
    def __init__(self) -> None:
        self.size = 3
        self.players = {"black": Player("black"),
                        "white": Player("white")}
        self.state = np.array([[[], [], []],
                               [[], [], []],
                               [[], [], []]])
        self.lines = []
        major_diagonal = []
        minor_diagonal = []
        for i in range(0, self.size):
            horizontal_line = []
            vertical_line = []
            for j in range(0, self.size):
                horizontal_line.append([i, j])
                vertical_line.append([j, i])
            self.lines.append(horizontal_line)
            self.lines.append(vertical_line)
            major_diagonal.append([i, i])
            minor_diagonal.append([size - 1 - i, i])
        self.lines.append(major_diagonal)
        self.lines.append(minor_diagonal)


    def place_piece(self, from_tile: Tuple[int, int],
                    to: Tuple[int, int],
                    piece: Piece) -> None:
        if not can_place_piece(from_tile, to, piece):
            raise ValueError(
                    "Can't place piece {} from {} to {}".format(piece, from_tile, to))
    
        player = self.players[color]
        if from_tile is None:
            player.consume_piece(piece.size)
        else:
            state[from_tile] = state[from_tile][1:]
        state[to] = state[to].insert(0, piece)


    def size_available(self, color: str, size: int) -> bool:
        return self.players[color].available_pieces[size] > 0

    def can_place_piece(self, from_tile: int,
                        to: Tuple[int, int],
                        piece: Piece) -> bool:
        # If you're not taking from the board, you must have that piece
        # available on your bench.
        if from_tile is None and not size_available(piece.color, piece.size):
            return False

        # If there's a piece on the destination square, then it must be
        # larger than the existing piece.
        if state[to] != [] and size <= state[to][0].size:
            return False

        if from_tile is not None:
            # Ensures the piece we're moving from the board is actually
            # at the top of it's stack
            if state[from_tile] == [] or state[from_tile] != piece:
                return False
        
        return True

 
    def find_winner(self) -> str:
        has_winner = False
        for line in self.lines:
            has_winner |= check_line_for_winner(line)
        return has_winner

    def check_line_for_winner(self, line: List[List[int]]) -> bool:
        if not line[0] or not line[1] or not line[2]:
            return False
        return line[0][0].color == line[1][0].color == line[2][0].color

    def has_winning_move(self, color: str) -> bool:
        for line in self.lines:
          break  
     def get_number_on_line(self, color: str, line: List[List[int]]):


class Player:

    def __init__(self, color: str) -> None:
        self.color = color

    board_memory = np.array([[[], [], []],
                             [[], [], []],
                             [[], [], []]])

    available_pieces = {3: 2, 2: 2, 1: 2}

    def consume_piece(self, size):
        available_pieces[size] -= 1
