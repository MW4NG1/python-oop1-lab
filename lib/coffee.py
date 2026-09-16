#!/usr/bin/env python3

class Coffee:
    def __init__(self, size="Small", price=0.0):
        # Check that the size is valid
        if size in ["Small", "Medium", "Large"]:
            self.size = size
        else:
            print("size must be Small, Medium, or Large")
            self.size = size

        # Store the coffee price
        self.price = price

    def tip(self):
        # Print the required message and add 1 to the price
        print("This coffee is great, here’s a tip!")
        self.price += 1