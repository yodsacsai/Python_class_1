import re


class Vehicle:
    #attibutes
    wheels = 2
    engine = ''
    seats = 1
    
    def __init__(self, wheels, engine, seats) -> None:
        self.wheels = wheels
        self.engine = engine
        self.seats = seats
        
    
    
    
    #methods
    def setWheels(self, wheels):
        self.wheels = wheels
        
    def getWheels(self):
        return self.wheels
    
    def setEngine(self, engine):
        self.engine = engine
        
    def getEngine(self):
        return self.engine
    
    def setSeats(self, seats):
        self.seats = seats
        
    def getSeats(self):
        return self.seats
    

        
    
    