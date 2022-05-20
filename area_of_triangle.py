#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: May 2022
# This program calculates the area of a triangle


def calculate_area(base, height):
    # calculate area

    # process
    area = base * height / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets base and height

    try:
        # input
        base_from_user = int(input("Enter the base of the triangle (cm): "))
        height_from_user = int(input("Enter the height of the triangle (cm): "))
        print("")

        # call functions
        calculate_area(base_from_user, height_from_user)
    except Exception:
        print("\nThis was not an integer, please enter an integer.")


if __name__ == "__main__":
    main()
