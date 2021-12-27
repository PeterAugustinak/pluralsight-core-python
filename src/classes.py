"""Example of using classes"""


class Flight:
    """Class representing single flight."""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not number[2:].isdigit() and int(number[2:] <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
                        [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seats(self, seat, passenger):
        """Allocate a seat to a passenger."""

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat '{seat}' already occupied!")

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        """Parsing seats - row and letter"""
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter '{letter}'")

        row_text = seat[:-1]
        row = None
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number '{row}'")

        if row not in rows:
            raise ValueError(f"Invalid row number '{row}'")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate passenger to a different seat."""

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat '{from_seat}'")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat '{to_seat}' already occupied.")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        """Count number of remaining available seats in the Aircraft"""
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        """
        Within FLight class it uses card printer to print all the occupied
        places in the Aircraft of this flight
        """
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


class Aircraft():
    """The class representing single aircraft"""

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    """The class representing specific aircraft"""

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus 319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boing777(Aircraft):
    """The class representing specific aircraft"""

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEFGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name: {passenger}"     \
             f" Flight: {flight_number}" \
             f" Seat: {seat}"        \
             f" Aircraft: {aircraft}" \
             f" |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("BA123", AirbusA319("G-EUPT"))
    f.allocate_seats("12A", "Par Smith")
    f.allocate_seats("15F", "Joh Doe")
    f.allocate_seats("15E", "Mark Antony")
    f.allocate_seats("1C", "Robert Martin")
    f.allocate_seats("1D", "Jane Holler")

    g = Flight("AF72", Boing777("F-GSPS"))
    g.allocate_seats("12A", "Par Smith")
    g.allocate_seats("15F", "Joh Doe")

    return f, g


