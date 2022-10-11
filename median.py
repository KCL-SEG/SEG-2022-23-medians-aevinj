"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()

if (len(numbers)==1):
    print(numbers[0])
elif((len(numbers)%2)!=0):
    print(numbers[math.ceil(len(numbers)/2)-1])
else:
    lower = numbers[int((len(numbers)/2) - 1)]
    upper = numbers[int(len(numbers)/2)]
    print((lower+upper)/2)
