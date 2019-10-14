#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program calculates the root values of a caudratic equation.


import math


def main():
    try:
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))
        c = float(input("Enter value of c: "))
        d = (b**2) - (4*a*c)
        if d > 0:
            x1 = ((-b) + (math.sqrt(d))) / (2*a)
            x2 = ((-b) - (math.sqrt(d))) / (2*a)
            print("\nx = {:,.2f} \nx = {:,.2f}".format(x1, x2))
        elif d == 0:
            x3 = (-b) / (2*a)
            print("\nThe root is {:,.2f}".format(x3))
        elif d < 0:
            print("\nThere are no roots")
        else:
            print("\nThat was not a proper value")
    except ValueError:
        print("\nThat was not a proper value")


if __name__ == "__main__":
    main()
