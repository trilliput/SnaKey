import pytest
from snakey.game import weighted_choice


def test_weighted_choice_with_empty_weights():
    """
    If argument weights is empty,
    then weighted_choice raises an exception
    """
    # Act
    with pytest.raises(ArithmeticError) as expected_excetpion:
        weighted_choice({})

    # Assert
    assert expected_excetpion.match('This should not happen.')


def test_weighted_choice_with_non_integer_values():
    """
    If argument weights contains non integer values
    then weighted_choice raises an exception
    """
    # Act & Assert
    with pytest.raises(TypeError):
        weighted_choice({'key': 'string'})


def test_weighted_choice():
    """
    In a list of 100 results of weighted_choice they key with much greater value appears more often
    """
    # Arrange
    input = {'lower': 0, 'a': 1, 'b': 2, 'c': 3, 'greater': 10}
    counts = {key: 0 for key in input}

    # Act
    for _ in range(100):
        actual_result = weighted_choice(input)
        counts[actual_result] += 1

    # Assert
    assert 'lower' in counts
    assert 'greater' in counts
    assert counts['lower'] < counts['greater']