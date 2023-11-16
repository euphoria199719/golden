# Write the utility functions here
#function to find the factors of a number
def find_factors(number):
    factors=[]
    for i in range (1,number+1):
        if number % i ==0:
          factors.append(i)
    return factors
#function to find the n-th number in the fibonacci series    
def fibonacci(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    else:
        f_series=[0,1]
        while len(f_series)<n:
            next_num=f_series[-1]+f_series[-2]
            f_series.append(next_num)
        return f_series
#function to convert celsius to fahrenheit and vice-versa    
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius+9/5) + 32
    return fahrenheit
def  fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32) * 5/9
    return celsius
#function to check given number is prime or not
def is_prime(number):
    if number<=1:
        return False
    if number<=3:
        return True
    if number%2 == 0 or number%3 ==0:
        return False
    i=5
    while i*1 <=number:
        if number%i ==0 or number%(i+2)==0:
            return False
        i+=6
        return True