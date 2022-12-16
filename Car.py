from Vehicle import Vehicle

class Car(Vehicle):
    #attributea
    model = ''
    
    def __init__(self, wheels, engine, seats, model) -> None:
        super().__init__(wheels, engine, seats)
        self.model = model