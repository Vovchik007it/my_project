import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    ("card_number", "expected"),
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("123456789012", "1234 56** **** 9012"),
        ("12345", "1234 5** **** 2345"),
        ("", " ** **** "),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    ("account_number", "expected"),
    [
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),
        ("12", "**12"),
        ("", "**"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "function",
    [get_mask_card_number, get_mask_account],
)
def test_mask_functions_raise_type_error_for_none(function) -> None:
    with pytest.raises(TypeError):
        function(None)
