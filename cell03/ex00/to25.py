#!/usr/bin/env python
num = int(input("Enter a number less than 25 "))
if num > 25:
    print("Error")
else:
    for i in range(num, 25+1):
        print("Inside the loop, my variable is ", i)