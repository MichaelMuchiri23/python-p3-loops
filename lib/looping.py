#!/usr/bin/env python3

def happy_new_year():
    num = 10

    while num > 0:
        print(num)
        num -= 1
    
    print('Happy New Year!')
    

def square_integers(int_list):
    new_int_list = [x * x for x in int_list]
    return new_int_list

def fizzbuzz():
    num = 1
    while num < 101:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1                