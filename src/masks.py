def get_mask_card_number(card_number: str) -> str:

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:

    return f"**{account_number[-4:]}"


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
