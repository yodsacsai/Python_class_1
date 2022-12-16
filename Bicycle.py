from Vehicle import Vehicle

class Bicycle(Vehicle):
    seats_height = 80
    handle_bar_type = ''
    gear_number = 1
    
    def __init__(self, wheels, engine, seats, seats_height, handle_bar_type, gear_number) -> None:
        super().__init__(wheels, engine, seats)
        self.seats_height = seats_height
        self.handle_bar_type = handle_bar_type
        self.gear_number = gear_number
    
        