import pytest

from src.processing import filter_by_state, sort_by_date

operations = [
    {"state": "EXECUTED", "date": "2026-08-01"},
    {"state": "CANCELED", "date": "2026-08-03"},
    {"state": "EXECUTED", "date": "2026-08-02"},
]


@pytest.mark.parametrize(
    ("state", "expected_count"),
    [("EXECUTED", 2), ("CANCELED", 1), ("PENDING", 0)],
)
def test_filter_by_state(state: str, expected_count: int) -> None:
    assert len(filter_by_state(operations, state)) == expected_count


@pytest.mark.parametrize(
    ("reverse", "expected_dates"),
    [
        (True, ["2026-08-03", "2026-08-02", "2026-08-01"]),
        (False, ["2026-08-01", "2026-08-02", "2026-08-03"]),
    ],
)
def test_sort_by_date(reverse: bool, expected_dates: list[str]) -> None:
    result = sort_by_date(operations, reverse)
    assert [operation["date"] for operation in result] == expected_dates
