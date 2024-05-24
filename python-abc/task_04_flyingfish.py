#!/usr/bin/python3


class Fish:
    """
    A class representing a fish.
    
    Methods:
    - swim: Makes the fish swim.
    - habitat: Prints the fish's habitat.
    """
    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")


class Bird:
    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")
    
    def swim(self):
        print("The flying fish is swimming!")
    
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

print(FlyingFish.mro())
