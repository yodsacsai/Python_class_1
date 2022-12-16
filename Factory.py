from Car import Car
from Motorcycle import Motorcycle
from Bicycle import Bicycle
print('======================================')
print('==         VEHICLE FACTORY          ==')
print('======================================')
print('')
type = input('Please select (1-Car, 2-Motocycle, 3-Bicycle):')

if type == '1': 
    print('Building car...') 
    wheels = int(input('Please input numbers of wheels:'))
    engine = input('Please input engine:')
    seats =  int(input('Please input numbers of seats:'))
    model = input('Please specify model:')   
    car = Car(wheels, engine, seats, model)
    print('Build car successfully') 
    print('MODEL: ', car.model)
    print('WHEELS: ', car.wheels)
    print('ENGINE: ', car.engine)
    print('SEATS: ', car.seats)
elif type == '2': 
    print('Building motorcycle...') 
    wheels = 2
    engine = input('Please input engine:')
    seats = int(input('Please input numbers of seats:'))
    model = input('Please specify model:')
    tire_type = input('Please select tire:')
    gear_n = int(input('Please select type of gear box (1-auto, 2-manual):'))
    motorcycle = Motorcycle(wheels, engine, seats, model, tire_type)
    print('Build motorcycle successfully') 
    print('ENGINE: ', motorcycle.engine)
    print('SEATS: ', motorcycle.seats)
    print('MODEL: ', motorcycle.model)
    print('TIRE TYPE: ', motorcycle.tire_type)
    print('GEAR BOX TYPE: ', motorcycle.gearbox_type[gear_n-1])
elif type == '3':
    print('Build Bicycle...')
    wheels = 2
    engine = ''
    seats = 1
    seats_height = int(input('Please input seat height (cm):'))
    handle_bar_type = input('Please input tpye of handle bar:')
    gear_number = int(input('Please input number of gear:'))
    bicycle = Bicycle(wheels, engine, seats, seats_height, handle_bar_type, gear_number)
    print('Build bicycle successfully')
    print('SEAT HEIGHT: '+ str(bicycle.seats_height) + 'cm')
    print('TYPE OF HANDLE BAR: ', bicycle.handle_bar_type)
    print('NUMBER OF GEARS: ', bicycle.gear_number)
else: 
    print('Please select the type of vehicle.') 
    