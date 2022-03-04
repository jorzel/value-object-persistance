from datetime import datetime

from value_objects.open_hours import OpenHours


def test_open_hours_initialization_with_valid_config():
    open_hours = OpenHours(
        {
            "days": [1, 2, 3, 4, 5, 6],
            "hours": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        }
    )

    assert open_hours.days == [1, 2, 3, 4, 5, 6]
    assert open_hours.hours == [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


def test_open_ours_is_open_True_when_datetime_within_period():
    open_hours = OpenHours(
        {
            "days": [1, 2, 3, 4, 5, 6],
            "hours": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        }
    )
    dt = datetime(2022, 3, 4, 11, 12, 10)  # 4.03.2022 11:12:10 Friday

    assert open_hours.is_open(dt) is True


def test_open_ours_is_open_False_when_datetime_within_period():
    open_hours = OpenHours(
        {
            "days": [1, 2, 3, 4, 5, 6],
            "hours": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        }
    )
    dt = datetime(2022, 3, 6, 11, 12, 10)  # 6.03.2022 11:12:10 Sunday

    assert open_hours.is_open(dt) is False
