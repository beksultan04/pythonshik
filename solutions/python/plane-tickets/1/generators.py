"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.
    
    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.
    
    Usage:
    >>> letters = generate_seat_letters(4)
    >>> next(letters)
    'A'
    """
    seat_letters = ['A', 'B', 'C', 'D']
    index = 0
    
    for _ in range(number):
        yield seat_letters[index % 4]
        index += 1


def generate_seats(number):
    """Generate a series of seats for airline.
    
    Seats are in format: 1A, 1B, 1C, 1D, 2A, 2B, etc.
    Skip row 13 (superstition).
    
    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.
    
    Usage:
    >>> seats = generate_seats(10)
    >>> next(seats)
    '1A'
    """
    seat_letters = ['A', 'B', 'C', 'D']
    row = 1
    seat_index = 0
    seats_generated = 0
    
    while seats_generated < number:
        # Skip row 13
        if row == 13:
            row += 1
            continue
        
        # Generate seat
        seat_letter = seat_letters[seat_index]
        yield f"{row}{seat_letter}"
        
        seats_generated += 1
        seat_index += 1
        
        # Move to next row after 4 seats
        if seat_index == 4:
            seat_index = 0
            row += 1


def assign_seats(passengers):
    """Assign seats to passengers.
    
    :param passengers: list[str] - list of passenger names.
    :return: dict - dictionary of {passenger: seat}.
    
    Usage:
    >>> passengers = ['Jerimiah', 'Eric', 'Bethany']
    >>> assign_seats(passengers)
    {'Jerimiah': '1A', 'Eric': '1B', 'Bethany': '1C'}
    """
    seats = generate_seats(len(passengers))
    return {passenger: seat for passenger, seat in zip(passengers, seats)}


def generate_codes(seat_numbers, flight_id):
    """Generate 12-character ticket codes.
    
    Format: [seat_number][flight_id][zeros to pad to 12 chars]
    Example: '1A' + 'CO1234' + '0000' = '1ACO12340000'
    
    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - flight identifier.
    :return: generator - generator that yields 12-char ticket codes.
    
    Usage:
    >>> seat_numbers = ['1A', '17D']
    >>> flight_id = 'CO1234'
    >>> codes = generate_codes(seat_numbers, flight_id)
    >>> next(codes)
    '1ACO12340000'
    """
    for seat in seat_numbers:
        # Combine seat + flight_id
        base_code = seat + flight_id
        
        # Pad with zeros to make it 12 characters
        padding_needed = 12 - len(base_code)
        ticket_code = base_code + ('0' * padding_needed)
        
        yield ticket_code