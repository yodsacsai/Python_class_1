from Vehicle import Vehicle

class Motorcycle(Vehicle):
    model = ''
    tire_type = ''
    gearbox_type = ['AUTO', 'MANUAL']
    
    def __init__(self, wheels, engine, seats, model, tire_type) -> None:
        super().__init__(wheels, engine, seats)
        self.model = model
        self.tire_type = tire_type
    
