import pytest
from SnaKey.game import weighted_choice


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