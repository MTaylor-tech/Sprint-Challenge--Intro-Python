# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    """ Base class for all vehicles """
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    """ A category class for flying vehicles """
    def __init__(self):
        super().__init__()
        pass

class GroundVehicle(Vehicle):
    """ A category class for vehicles that move along the ground """
    def __init__(self):
        super().__init__()
        pass

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        self.name = "Jefferson"
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()
        self.former_name = "Jefferson"
        pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        self.noise = "Vroom vroom!"
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass
