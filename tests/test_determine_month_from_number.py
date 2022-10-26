import pytest

from src.main import determine_month_from_number


@pytest.mark.parametrize('month_integer', [*range(1, 12)])
def test_passes_when_month_value_is_correct(month_integer: int):
    determine_month_from_number(month_integer)


@pytest.mark.parametrize('month_integer', [0, 13, 99])
def test_raises_incorrect_month_value(month_integer: int):
    with pytest.raises(Exception) as exc_info:
        determine_month_from_number(month_integer)
    assert str(exc_info.value) == 'Incorrect value of the month. It should be between 1 and 12'
