def parse_seat(seat):
    if not isinstance(seat, str):
        raise ValueError("Seat must be a string")

    seat = seat.strip()

    if len(seat) < 2:
        raise ValueError("Seat must contain a row letter and seat number")

    row = seat[0].upper()
    number = seat[1:]

    if not row.isalpha() or not row.isascii():
        raise ValueError("Invalid seat row")

    if not number.isdigit():
        raise ValueError("Seat number must be numeric")

    seat_number = int(number)

    if seat_number <= 0:
        raise ValueError("Seat number must be positive")

    return row, seat_number


def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        raise ValueError("Prices must be provided as a CSV string")

    if not prices_csv.strip():
        raise ValueError("Price list cannot be empty")

    try:
        parts = prices_csv.split(',')
        if any(not p.strip() for p in parts):
            raise ValueError("Empty price value")

        prices = [int(p.strip()) for p in parts]
    except ValueError:
        raise ValueError("Prices must be comma-separated integers")

    if any(p < 0 for p in prices):
        raise ValueError("Prices cannot be negative")

    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    if not isinstance(ratings, str):
        raise ValueError("Ratings must be provided as a string")

    if not ratings.strip():
        raise ValueError("Ratings cannot be empty")

    try:
        values = [int(r) for r in ratings.split()]
    except ValueError:
        raise ValueError("Ratings must contain integers")

    if any(r < 1 or r > 5 for r in values):
        raise ValueError("Ratings must be between 1 and 5")

    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    try:
        result = parse_seat(user_input)
        print("Row and Seat:", result)
    except ValueError as e:
        print("Invalid seat:", e)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    try:
        result = total_price(user_input)
        print("Total with GST:", result)
    except ValueError as e:
        print("Invalid prices:", e)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    try:
        result = average_rating(user_input)
        print("Average Rating:", result)
    except ValueError as e:
        print("Invalid ratings:", e)


if __name__ == "__main__":
    main()
