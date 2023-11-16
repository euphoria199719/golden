# import the utility module here

import utility

## Call the utility functions and check the output with sample inputs 
number=28

#find the factors of a number
factors= utility.find_factors(number)
print(f"factors of {number}: {factors}")

#find the 10th number in the fibonacci series
n=11
f_series=utility.fibonacci(n)
print(f"the {n}-th fibonacci number: {f_series[-1]}")

#convert celsius to fahrenheit
celsius_temp=30
fahrenneit_temp=utility.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} C is equal to {fahrenneit_temp} F")

#check if a number is prime
prime_number=13
if utility.is_prime(prime_number):
    print(f"{prime_number}is a prime number")
else:
    print(f"{prime_number}is not a prime number")