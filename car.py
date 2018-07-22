class Car():
    """Represent gas and electric cars."""

    def __init__(self, make, model, year):
        """Initializw attributes."""
        self.make = make
        self.model = model
        self.year = year
        #set a default value
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a name and descriptions."""
        long_name = str(self.year) + ' ' + str(self.make) +' '+ str(self.model)
        return long_name.title()
    
    def read_odometer(self):
        """Print car's mileage."""
        print("This car has " + str(self.odometer_reading)+" miles on it.")
    
    def update_odometer(self, mileage):
        """Reject odometer changes attempts."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
my_used_car = Car('hyundai', 'i30', '2008')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23)
my_used_car.read_odometer()
my_used_car.increment_odometer(10)
my_used_car.read_odometer()

"""Chils class."""

class ElecricCar(Car):
    """Represent electric cars aspects."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent Car class."""
        super().__init__(make, model, year)
        #define attributes for child class
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

class Battery():
    """Model a battery for an electric car."""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print battery description."""
        print("This car has a " + str(self.battery_size) + "kWh battery.")
    
    def get_range(self):
        """Print the rage of the battery."""
        if self.battery_size == 70:
            range_is = 240
        if self.battery_size == 85:
            range_is = 270
        
        message = "This car can go approximattely " + str(range_is)
        message += " miles on a full charge."
        print(message)

my_el_car = ElecricCar("Nissan", "Almera", "2000")
print(my_el_car.get_descriptive_name())
my_el_car.battery.describe_battery()
my_el_car.battery.get_range()