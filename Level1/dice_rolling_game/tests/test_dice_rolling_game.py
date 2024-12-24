import pytest
from app.dice_rolling_game import roll_dice


def test_roll_dice_single():
    result = roll_dice(1)
    assert len(result) == 1
    assert 1 <= result[0] <= 6


def test_roll_dice_multiple():
    num_dice = 5
    result = roll_dice(num_dice)
    assert len(result) == num_dice
    for value in result:
        assert 1 <= value <= 6


def test_roll_dice_invalid():
    with pytest.raises(ValueError):
        roll_dice(0)
