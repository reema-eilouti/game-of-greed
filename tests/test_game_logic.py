import pytest
from game_of_greed.game_logic import GameLogic

def test_roll_dice_length():
    """
    A sequence of correct length is returned
    """
    result = GameLogic.roll_dice(6)
    actual = len(result)
    expected = 6
    assert actual == expected

def test_roll_dice_range():
    """
    Each item in sequence is an integer with value between 1 and 6
    """
    result = GameLogic.roll_dice(6)
    for num in result:
        if num > 6 or num < 1:
            assert False, 'roll_dice output must be between 1 and 6'