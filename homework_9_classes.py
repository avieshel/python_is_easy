
import random # for testing

class Vehicle:
    # make, model, year & weight are mandatory parameters
    def __init__(self, make, model , year, weight, needs_maintenance=False, trips_since_maintenanace=0):
        self.set_make(make)
        self.set_model(model)
        self.set_year(year)
        self.set_weight(weight)
        self.set_needs_maintenance(needs_maintenance)
        self.set_trips_since_maintenance(trips_since_maintenanace)
    
    # getters
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_weight(self):
        return self.weight

    def is_needs_maintenance(self):
        return self.needs_maintenance

    def get_trips_since_maintenanance(self):
        return self.trips_since_maintenanace

    # setters
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model
    
    def set_year(self, year):
        self.year = year

    def set_weight(self, weight):
        self.weight = weight

    def set_needs_maintenance(self, needs_maintenance):
        self.needs_maintenance = needs_maintenance

    def set_trips_since_maintenance(self, trips_since_maintenanace):
        self.trips_since_maintenanace = trips_since_maintenanace
    
    def reset_trips_since_maintenance(self):
        self.set_trips_since_maintenance(0)

    def __str__(self):
        return 'Make: ' + self.get_make() + '\nModel: ' + self.get_model() + '\nYear: ' + str(self.get_year()) + '\nWeight: ' + str(self.get_weight()) + 'Kg\nNeeds maintenance: ' + str(self.is_needs_maintenance()) + '\nTrips since last maintenance: ' + str(self.get_trips_since_maintenanance())
    
    # Vehicle helper methods
    def increment_trips_counter(self):
        trips_so_far = self.get_trips_since_maintenanance()
        trips_so_far += 1
        self.set_trips_since_maintenance(trips_so_far)
    
    

class Car(Vehicle):

    def __init__(self, make, model, year, weight, is_driving=False, max_trips_before_maintenance=100):
        Vehicle.__init__(self, make, model, year, weight)
        self.set_is_driving(is_driving)
        self.set_max_trips_before_maintenance(max_trips_before_maintenance)

    def __str__(self):
        return 'Car: \n' + Vehicle.__str__(self)
    
    # getters
    def is_currently_driving(self):
        return self.is_driving

    def get_max_trips_before_maintenance(self):
        return self.max_trips_before_maintenance

    # setters
    def set_is_driving(self, is_driving):
        self.is_driving = is_driving

    def set_max_trips_before_maintenance(self, max_trips_before_maintenance):
        self.max_trips_before_maintenance = max_trips_before_maintenance
    
    # Car methods
    
    def drive(self):
        if self.is_currently_driving() == False:
            # signal the car is driving
            self.set_is_driving(True)
            
        
    def stop(self):
        if self.is_currently_driving() == True:
            # signal car stopped
            self.set_is_driving(False)
            # increment the trips counter
            self.increment_trips_counter()
            # check if by making this trip the car needs maintenance
            self.update_needs_maintenance_status()

    def update_needs_maintenance_status(self):
        if self.get_trips_since_maintenanance() >= self.get_max_trips_before_maintenance():
            self.set_needs_maintenance(True)

    def repair(self):
        # reset the trips till next maintenance
        self.reset_trips_since_maintenance()
        # set the needs_maintenance flag to False
        self.set_needs_maintenance(False)


class Plane(Vehicle):
    def __init__(self, make, model, year, weight, is_flying = False, max_trips_before_maintenance = 100 ):
        Vehicle.__init__(self, make, model, year, weight)
        self.set_is_flying(is_flying)
        self.set_max_trips_before_maintenance(max_trips_before_maintenance)

    def __str__(self):
        return 'Plane:\n' + Vehicle.__str__(self)

    # getters
    def is_currently_flying(self):
        return self.is_flying
    
    def get_max_trips_before_maintenance(self):
        return self.max_trips_before_maintenance

    # setters
    def set_is_flying(self, is_flying):
        self.is_flying = is_flying

    def set_max_trips_before_maintenance(self, max_trips_before_maintenance):
        self.max_trips_before_maintenance = max_trips_before_maintenance


    # Plane methods
    def update_needs_maintenance_status(self):
        if self.get_trips_since_maintenanance >= self.get_max_trips_before_maintenance():
            self.set_needs_maintenance(True)

    def repair(self):
        if self.is_needs_maintenance():
            self.reset_trips_since_maintenance() 
            self.set_needs_maintenance(False)

    def is_able_to_fly(self):
        if self.is_needs_maintenance() == True:
            return False
        return True

    def fly(self):
        if self.is_able_to_fly() == True and self.is_currently_flying() == False:
            self.set_is_flying(True)
    
    def land(self):
        if self.is_currently_flying() == True:
            self.set_is_flying(False)
            self.increment_trips_counter()
            # check if this plane needs maintenance
            if self.get_trips_since_maintenanance() >= self.get_max_trips_before_maintenance():
                self.set_needs_maintenance(True)



# Tests

# Car Tests
def car_tests(number_of_trips = 100, maintenance_limit = 50):
    print('='*20 + '\nCar Test\n' + '='*20)
    ferrari = Car(make = 'Ferrari', model = '458', year = 2019, weight = 1565, is_driving=False, max_trips_before_maintenance=maintenance_limit)
    corvette = Car(make = 'Chevrolet', model = 'Corvette', year = 1969, weight = 1402, is_driving=False, max_trips_before_maintenance=maintenance_limit)
    mustang = Car(make = 'Ford', model = 'Mustang', year = 1970, weight = 1416, is_driving=False, max_trips_before_maintenance=maintenance_limit)

    # print cars
    print(ferrari)
    print(corvette)
    print(mustang)
       
    # create an array of the cars
    cars = [ferrari, corvette, mustang]

    for trips in range(number_of_trips):
        r = random.randint(0,len(cars) -1) # to select a random car
        # change the state of the car
        print('CAR TEST: ' + cars[r].get_model() + ' seleted')
        if cars[r].is_currently_driving() == True:
            cars[r].stop()
            print('CAR TEST: ' + cars[r].get_model() + ' Stopped, Trips since maintenance: ' + str(cars[r].get_trips_since_maintenanance()))
        else:
            print('CAR TEST: ' + cars[r].get_model() + 'Started')
            cars[r].drive()

    # print status after tests
    print(ferrari)
    print(corvette)
    print(mustang)

# Planes Test
def plane_tests(number_of_flights = 100, max_flights_before_maintenance = 50):
    print('='*20 + '\nPlane Test\n' + '='*20)
    # define plances
    f16 = Plane('General Dynamic', 'F-16 Falcon', 2015, 9207, False, max_flights_before_maintenance)
    jumbo = Plane('Boeing', '747-400 Jumbo', 2000, 183500, False, max_flights_before_maintenance)
    f22 = Plane('Lockheed Martin', 'F-22 Raptor', 2018, 19700, False, max_flights_before_maintenance)

    # print planes
    print(f16)
    print(jumbo)
    print(f22)

    # fly them around
    planes = [f16, jumbo, f22]
    for trips in range(number_of_flights):
        p = random.randint(0, len(planes) -1) # to select random plane
        print('PLANE TEST: selected plane' + planes[p].get_model())
        if planes[p].is_currently_flying() == False:
            # try to fly, note: we might need to run a maintanance job
            print('PLANE TEST: ' + planes[p].get_model() + ' trying to takeoff...')
            if planes[p].is_needs_maintenance() == True:
                print('PLANE TEST: repairing ' + planes[p].get_model() + ' before takeoff')
                planes[p].repair()
            planes[p].fly()
            print('PLANE TEST: ' + planes[p].get_model() + ' is flying')
        else:
            planes[p].land()
            print('PLANE TEST: ' + planes[p].get_model() + ' has landed, this plane has made ' + str(planes[p].get_trips_since_maintenanance()) + ' since last maintenance job')

    print(f16)
    print(jumbo)
    print(f22)    

# run the test
car_tests(number_of_trips=100, maintenance_limit=10)
plane_tests(number_of_flights=100, max_flights_before_maintenance=10)