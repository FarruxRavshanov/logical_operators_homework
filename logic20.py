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

    x1 = n % 10
    count0 += 1 and x1 == 0
    count1 += 1 and x1 == 1

    x2 = n // 10 % 10
    count0 += 1 and x2 == 0
    count1 += 1 and x2 == 1

    x3 = n // 1000 % 10
    count0 += 1 and x3 == 0
    count1 += 1 and x3 == 1

    x4 = n // 1000 % 10
    count0 += 1 and x4 == 0
    count1 += 1 and x4 == 1

    x5 = n // 10000
    count0 += 1 and x5 == 0
    count1 += 1 and x5 == 1

    return count1 > count0

print(main(11010))