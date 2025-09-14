'''
Module 3 Lab Case Study
Written by: Fredeirc (Derek) Gerry, 9-13-25. Version 1.0
Stored here on Desktop: C:\Derek's Stuff\DEREK 2\MISCALENOUS\Ivy Tech College Stuff\
Everything\2025\Fall 1st Semester SDEV-220\Python code
This program demonstrates the use of classes, inheritance, and user input.
Variables used are:
vehicle_type Description: car, truck, plane, boat, or broomstick
Automobile Descritpion: year, make, model, number of doors, and type of roof'''

class Vehicle: # Parent Class
    vehicle_type = None   # Class attribute (shared by all instances)

    def __init__(self, car, truck, plane, boat, broomstick):      
        self.car = car
        self.truck = truck
        self.plane = plane
        self.boat = boat
        self.broomstick = broomstick

class Automobile(Vehicle):  # Child Class: Automobile description
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors  # two or four doors
        self.roof = roof    # solid or sunroof

def get_user_input():  # App controls
    Vehicle.vehicle_type = input("Enter the vehicle's type (car, truck, plane, boat, or broomstick): ")
    year = input("Enter the vehicle's year: ")
    make = input("Enter the vehicle's make: ")
    model = input("Enter the vehicle's model: ")
    doors = input("Enter the vehicle's number of doors (2 or 4): ")
    roof = input("Enter the vehicle's roof type (solid or sun roof): ")
    return year, make, model, doors, roof

# Collect user input
year, make, model, doors, roof = get_user_input()

# Automobile object
myVehicle = Automobile(year, make, model, doors, roof)

# Display results
print(f"Vehicle type is: {Vehicle.vehicle_type}")
print(f"Year: {myVehicle.year}")
print(f"Make: {myVehicle.make}")
print(f"Model: {myVehicle.model}")
print(f"Number of doors: {myVehicle.doors}")
print(f"Roof type: {myVehicle.roof}")