from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        result = parse_seat(s)
        assert isinstance(result, tuple)
        assert len(result) == 2
    except ValueError:
        pass


@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        result = total_price(s)
        assert isinstance(result, float)
        assert result >= 0
    except ValueError:
        pass


@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        result = average_rating(s)
        assert isinstance(result, float)
        assert 1 <= result <= 5
    except ValueError:
        pass
