from typing import Union

import numpy as np

from numpy import matrix, ndarray

playing_board: Union[matrix, ndarray] = np.matrix(
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
    ]
)

final_result: Union[matrix, ndarray] = np.matrix(
    [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]
)


class PlayingPiece:
    matrix_arrangement: Union[matrix, ndarray] = np.zeros((4, 4))
    piece_length: int
    piece_height: int
    number_of_possible_rotation: int

    def __init__(
        self,
        matrix_arrangement: Union[matrix, ndarray],
        number_of_possible_rotation: int = 1,
    ):
        self.matrix_arrangement = matrix_arrangement
        self.piece_length = int(np.sum(np.nanmax(self.matrix_arrangement, 0)))
        self.piece_height = int(np.sum(np.nanmax(self.matrix_arrangement, 1)))
        self.number_of_possible_rotation = number_of_possible_rotation

    def translate(self, x_direction: int, y_direction: int) -> Union[matrix, ndarray]:
        translated_matrix: Union[matrix, ndarray] = np.zeros((4, 4))
        for i in range(4):
            for j in range(4):
                if self.matrix_arrangement[i, j] == 1:
                    translated_matrix[
                        i + x_direction, j + y_direction
                    ] = self.matrix_arrangement[i, j]
        return translated_matrix

    def rotate(self) -> Union[matrix, ndarray]:
        return self.matrix_arrangement.transpose()


class PlayingPieceThree(PlayingPiece):
    def rotate(self) -> Union[matrix, ndarray]:
        rotated_matrix: Union[matrix, ndarray] = np.zeros((4, 4))
        for i in range(4):
            for j in range(4):
                if self.matrix_arrangement[i, j] == 1 and i == 0:
                    rotated_matrix[j, 1] = self.matrix_arrangement[i, j]
                if self.matrix_arrangement[i, j] == 1 and i == 1:
                    rotated_matrix[j, 0] = self.matrix_arrangement[i, j]

        return rotated_matrix


class PlayingPieceFour(PlayingPiece):
    def rotate(self) -> Union[matrix, ndarray]:
        rotated_matrix: Union[matrix, ndarray] = np.zeros((4, 4))
        for i in range(4):
            for j in range(4):
                if self.matrix_arrangement[i, j] == 1 and i == 0:
                    rotated_matrix[j, 3] = self.matrix_arrangement[i, j]
                if self.matrix_arrangement[i, j] == 1 and i == 1:
                    rotated_matrix[j, 2] = self.matrix_arrangement[i, j]
                if self.matrix_arrangement[i, j] == 1 and i == 2:
                    rotated_matrix[j, 1] = self.matrix_arrangement[i, j]
                if self.matrix_arrangement[i, j] == 1 and i == 3:
                    rotated_matrix[j, 0] = self.matrix_arrangement[i, j]

        return rotated_matrix


piece_1: PlayingPiece = PlayingPiece(
    matrix_arrangement=np.matrix(
        [
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
)

piece_2: PlayingPiece = PlayingPiece(
    matrix_arrangement=np.matrix(
        [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )
)

piece_3: PlayingPieceThree = PlayingPieceThree(
    matrix_arrangement=np.matrix(
        [
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    ),
    number_of_possible_rotation=3,
)


piece_4: PlayingPieceFour = PlayingPieceFour(
    matrix_arrangement=np.matrix(
        [
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    ),
    number_of_possible_rotation=3,
)
