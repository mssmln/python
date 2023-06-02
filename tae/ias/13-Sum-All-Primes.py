# Sum All Primes
# 
# A prime number is a whole number greater than 1 with exactly two divisors: 1 and itself. 
# For example, 2 is a prime number because it is only divisible by 1 and 2. In contrast, 4 is not prime since it is divisible by 1, 2 and 4.
# Rewrite sumPrimes so it returns the sum of all prime numbers that are less than or equal to num.


def sumPrimes (num) :
    factorial = []
    res = 0
    while num > 1 :
        i = 1
        while i <= num :
            if num % i == 0 :
                factorial.append(i)
            i += 1
        if len(factorial) == 2 :
            res += factorial[1]
        factorial = []
        num -= 1
    return res


print(sumPrimes(977))