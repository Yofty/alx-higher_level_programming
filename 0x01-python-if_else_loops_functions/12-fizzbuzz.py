#!/usr/bin/python3
def fizzbuzz():

    for x in range(1, 101):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz", end=" ")
        elif x % 5 == 0:
            if x != 100:
                print("Buzz", end=" ")
            else:
                print("Buzz")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(f"{x}", end=" ")
