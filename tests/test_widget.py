import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792276266361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize("value", ["не дата", "2024-13-40"])
def test_get_date_invalid(value: str) -> None:
    with pytest.raises(ValueError):
        get_date(value)
