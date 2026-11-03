
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price tests

def test_regular_morning():
    assert ticket_price("regular", 25, 10, False) == 100


def test_premium_evening_weekend():
    assert ticket_price("premium", 25, 19, True) == 320


def test_recliner_afternoon():
    assert ticket_price("recliner", 25, 15, False) == 400


def test_free_ticket_under_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 10, 15, False) == 75


def test_senior_discount():
    assert ticket_price("premium", 60, 19, False) == 140


def test_unknown_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_show_hour(hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, hour, False)


# Group discount tests

def test_no_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_fifteen_percent_group_discount():
    assert group_discount(10, False) == 15


def test_ten_percent_group_discount():
    assert group_discount(5, False) == 10


def test_student_group_discount():
    assert group_discount(5, True) == 15


def test_student_group_without_discount():
    assert group_discount(2, True) == 0


# Snack combo tests

def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack_with_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack():
    assert snack_combo("large", False) == 250


def test_other_snack_size_with_coupon():
    assert snack_combo("extra-large", True) == 200
