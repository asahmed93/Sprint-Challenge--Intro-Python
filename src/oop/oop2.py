# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4, **kwargs):
        self.num_wheels = num_wheels
        super().__init__(**kwargs)

    def drive(self):
        return "vroom vroom"

    # TODO


class Motorcycle(GroundVehicle):
    def __init__(self, **kwargs):
        super().__init__(num_wheels=2, **kwargs)

    def drive(self):
        return "zzzzoooooooooommmm"

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO


for vehicle in vehicles:
    print(vehicle.drive())
