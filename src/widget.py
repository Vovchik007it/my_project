"""Функции для работы с банковскими картами, счетами и датами."""

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:

    name, number = account_card.rsplit(" ", 1)

    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    date = datetime.fromisoformat(date_string)
    return date.strftime("%d.%m.%Y")
