class CCNumbers:

    # Checks to see if a numbers is prime
    def isPrime(num):
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # print(num, "is not a prime number")
                    # print(i, "times", num // i, "is", num)
                    return False
                    break
            else:
                # print(num, "is a prime number")
                return True

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            # print(num, "is not a prime number")
            return False
