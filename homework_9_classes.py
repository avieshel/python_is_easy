
def Vehicle(make, model, year, weight, needs_maintenance, trips_since_maintenanace):
    # make, model, year & weight are mandatory parameters
    def __init__(self, make, model , year, weight, needs_maintenance=False, trips_since_maintenanace=0):
        set_make(make)
        set_model(model)
        set_year(year)
        set_weight(weight)
        set_needs_maintenance(needs_maintenance)
        set_trips_since_maintenance(trips_since_maintenanace)
    
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
        set_trips_since_maintenance(self, 0)


def Car(make, model, year, weight, is_driving=False, max_trips_before_maintenance=100):

    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        set_is_driving(is_driving)
        set_max_trips_before_maintenance(max_trips_before_maintenance)

    def __str__(self):
        return 'Car:' + self.get_make + '\nModel: ' + self.get_model + '\nYear: ' + self.get_year + '\nWeight: ' + self.get_weight + ' Kg\nNeeds maintenance: ' + self.is_needs_maintenance() + '\nTrips since last maintenance: ' + self.get_trips_since_maintenanance
    
    # getters
    def is_driving(self):
        return self.is_driving

    def get_max_trips_before_maintenance(self):
        return self.max_trips_before_maintenance

    # setters
    def set_is_driving(self, is_driving):
        self.is_driving = is_driving

    def set_max_trips_before_maintenance(self, max_trips_before_maintenance):
        self.max_trips_before_maintenance = max_trips_before_maintenance
    
    # Car methods
    def increment_trips_counter(self):
        current_trips_made = self.get_trips_since_maintenanance()
        current_trips_made += 1
        self.set_trips_since_maintenance(current_trips_made)
    
    def drive(self):
        if is_driving() == False:
            # signal the car is driving
            set_is_driving(True)
            
        
    def stop(self):
        if is_driving() == True:
            # signal car stopped
            set_is_driving(False)
            # increment the trips counter
            increment_trips_counter()
            # check if by makeing this trip the car needs maintenance
            if self.get_trips_since_maintenanance() >= get_max_trips_before_maintenance():
                self.set_needs_maintenance(True)

    def repair(self):
        # reset the trips till next maintenance
        self.reset_trips_since_maintenance()
        # set the needs_maintenance flag to False
        self.set_needs_maintenance(False)


# Tests
ferrari = Car(make = 'Ferrari', model = '458', year = 2019, weight = 1565)
corvette = Car(make = 'Chevrolet', model = 'Corvette', year = 1969, weight = 1402)
mustang = Car(make = 'Ford', model = 'Mustang', year = 1970, weight = 1416)

# print cars
print(ferrari)
print(corvette)
print(mustang)


# drive them around 

import random
# create an array of the cars
cars = [ferrari, corvette, mustang]

for trips in range(200):
    r = random.randint(0,3) # get a random integer 0,1,2
    # change the state of the car
    if cars[r].is_driving() == True:
        cars[r].stop()
    else:
         cars[r].drive()

# print status after tests
print(ferrari)
print(corvette)
print(mustang)

