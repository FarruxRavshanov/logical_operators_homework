def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    count0 = 0
    count1 = 0

    x1 = n  % 10
    count0 += x1 == 0
    count1 += x1 == 1
    n //= 10

    x2 = n  % 10 
    count0 += x2 == 0 and n != 0
    count1 += x2 == 1
    n //= 10

    x2 = n  % 10 
    count0 += x2 == 0 and n != 0
    count1 += x2 == 1
    n //= 10

    x2 = n  % 10 
    count0 += x2 == 0 and n != 0
    count1 += x2 == 1
    n //= 10
    
    return count1 > count0

print(main(1101))