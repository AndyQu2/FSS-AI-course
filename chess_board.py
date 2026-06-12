import numpy as np


class ChessBoardConfig:
    def __init__(self, column: int, row: int):
        self.column = column
        self.row = row

class ChessBoard:
    def __init__(self, config: ChessBoardConfig, num_player: int):
        self.config = config
        self.num_player = num_player

        self._board = np.full((config.row, config.column), -1, dtype=np.int64)

    def set_status(self, column: int, row: int, player_id: int):
        if column >= self.config.column:
            raise ValueError(f"Column {column} out of range")
        elif row >= self.config.row:
            raise ValueError(f"Row {row} out of range")

        if player_id <= 0 or player_id >= self.num_player:
            raise ValueError(f"Player id {player_id} out of range")

        self._board[row, column] = player_id

    def print_board(self):
        for i in enumerate(self._board):
            for j in enumerate(i):
                print(j, end=" ")
            print("\n")