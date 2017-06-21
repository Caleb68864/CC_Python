class CCNumbers:
    def isPrime(num):
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            return False