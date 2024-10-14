from enum import Enum

class difficulty(Enum):
    VERY_EASY = 1
    EASY = 2
    NORMAL = 3
    HARD = 4
    VERY_HARD = 5

difficulty_map = {"very easy": difficulty.VERY_EASY.value,
                  "easy": difficulty.EASY.value,
                  "normal": difficulty.NORMAL.value,
                  "hard": difficulty.HARD.value,
                  "very hard": difficulty.VERY_HARD.value}