
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price: seat validation and show-time branches

def test_valid_seat():
    assert ticket_price("regular", 25, 15, False) == 150


def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


def test_negative_show_hour():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_show_hour_above_range():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_morning_discount():
    assert ticket_price("regular", 25, 11, False) == 100


def test_afternoon_no_time_adjustment():
    assert ticket_price("regular", 25, 15, False) == 150


def test_evening_surcharge():
    assert ticket_price("regular", 25, 18, False) == 180


def test_weekend_surcharge():
    assert ticket_price("regular", 25, 15, True) == 190


def test_child_under_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_adult_full_price():
    assert ticket_price("regular", 25, 15, False) == 150


def test_child_half_price():
    assert ticket_price("regular", 12, 15, False) == 75


def test_adult_age_thirteen():
    assert ticket_price("regular", 13, 15, False) == 150


def test_senior_half_price():
    assert ticket_price("regular", 60, 15, False) == 75


# Group discount: each threshold and student condition

def test_zero_tickets_raises_error():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_small_group_no_discount():
    assert group_discount(2, False) == 0


def test_four_tickets_no_discount():
    assert group_discount(4, False) == 0


def test_five_tickets_get_ten_percent():
    assert group_discount(5, False) == 10


def test_nine_tickets_get_ten_percent():
    assert group_discount(9, False) == 10


def test_ten_tickets_get_fifteen_percent():
    assert group_discount(10, False) == 15


def test_student_group_with_discount():
    assert group_discount(5, True) == 15


def test_student_group_without_base_discount():
    assert group_discount(2, True) == 0


# Snack combo: small, medium, other sizes, and coupon branches

def test_small_without_coupon():
    assert snack_combo("small", False) == 120


def test_medium_without_coupon():
    assert snack_combo("medium", False) == 180


def test_other_size_without_coupon():
    assert snack_combo("large", False) == 250


def test_small_with_coupon():
    assert snack_combo("small", True) == 70


def test_medium_with_coupon():
    assert snack_combo("medium", True) == 130


def test_other_size_with_coupon():
    assert snack_combo("large", True) == 200
