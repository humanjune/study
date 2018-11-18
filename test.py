def identify_prime(n):
    result = True
    if n == 1:
        return False
    for x in range(2, n):
        if (n % x) == 0:
            result = False
    return result

