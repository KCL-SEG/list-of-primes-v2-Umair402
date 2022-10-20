"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 3
    if number_of_primes <= 0:
        raise ValueError('You must enter a number above 0')
    elif number_of_primes == 1:
        list = [2]
    elif number_of_primes == 2:
        list = [2,3]
    else:
        list =[2,3]
        while len(list) < number_of_primes:
            prime = True
            number += 1
            for divisor in range(2,number):
                if number % divisor == 0:
                    prime = False
                    break
            if prime == True:
                list.append(number)
    return list