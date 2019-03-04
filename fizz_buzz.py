def is_divisible_by_5(number):
    return number % 5 == 0

def is_divisible_by_3(number):
    return number % 3 == 0

def is_prime(number):
    for divisor in range (2, number):
        if (number % divisor == 0):
            return False
    return True
'''
A Prime number has exactly two divisors 1 and itself.
To check number primality we need to loop over all the
numbers from 2 to 'number to check' and make sure that 
the % (modulo) is not 0 (zero).
we can do a better job of not checking 'things twice' 
assume we are checking primality for 13.
start by checking 13 % 2 == 0? it's false, we move on to
check 13 % 3 == 0?, again false so we move on... 
after checking 13 % 2 == 0 is false we know that 
13 % 7, 13 % 8 ... 13 % 12 will all be false.
after checking 13 % 3 we can limit the search to 5
the following function takes advantage of this to check
primality faster (little faster) than the function is_prime(number) above.
'''
def is_prime_fast(number):
    if number == 1:
        return False
    return is_prime_fast_helper(2, number, number)

def is_prime_fast_helper(divisor, numer, limit):
    if divisor >= limit:
        return True
    elif numer % divisor == 0:
        return False
    else :
        limit = (numer // divisor) + 1
        divisor += 1
        return is_prime_fast_helper(divisor, numer, limit)
        
# # primality testing
# assert is_prime_fast(1) is False, '1 is not prime'
# assert is_prime_fast(2) is True, '2 is prime'
# assert is_prime_fast(3) is True, '3 is prime'
# assert is_prime_fast(4) is False, '4 is not prime'
# assert is_prime_fast(5) is True, '5 is prime'
# assert is_prime_fast(6) is False, '6 is not prime'
# assert is_prime_fast(7) is True, '7 is prime'
# assert is_prime_fast(8) is False, '8 is not prime'
# assert is_prime_fast(9) is False, '9 is not prime'
# assert is_prime_fast(10) is False, '10 is not prime'
# assert is_prime_fast(11) is True, '11 is prime'
# assert is_prime_fast(12) is False, '12 is not prime'

# #some more tests
# for t in (2, 101):
#     assert is_prime(t) is is_prime_fast(t)


def fizz_buzz(limit):
    for n in range(1, limit + 1):
        nothing_printed_yet = True
        if is_divisible_by_3(n):
            print('fizz ', end='')
            nothing_printed_yet = False
        if is_divisible_by_5(n):
            print('buzz ', end='')
            nothing_printed_yet = False
        if  nothing_printed_yet:
            print(n, end='')
        if is_prime_fast(n):
            print(' (',n,' is prime)', end='')
        print('',end='\n') #Add new line just to make the output clearer

fizz_buzz(100)