#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# this program tells the difference between equilateral,
# isosceles and scalene triangles


def main():
    # this program tells the difference between equilateral,
    # isosceles and scalene triangles

    # input

    side1_string = input("Enter the length of the first side: ")
    side2_string = input("Enter the length of the second side: ")
    side3_string = input("Enter the length of the third side: ")

    # process
    try:
        side1 = int(side1_string)
        side2 = int(side2_string)
        side3 = int(side3_string)

        if side1 == side2 and side2 == side3 and side1 == side3:
            print("That's an equilateral triangle.")
        else:
            if side1 == side2 or side2 == side3 or side1 == side3:
                print("That's an isosceles triangle.")
            else:
                print("That's a scalene triangle")
    except:
        print("Invalid Input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
