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
    if x1 == 1:
        count1 += 1
    else:
        count0 += 1

    x2 = n // 10 % 10
    if x2 == 1:
        count1 += 1
    else:
        count0 += 1

    x3 = n // 100 % 10
    if x3 == 1:
        count1 += 1
    else:
        count0 += 1

    x4 = n // 1000 % 10
    if x4 == 1:
        count1 += 1
    else:
        count0 += 1

    x5 = n // 10000
    if x5 == 1:
        count1 += 1
    else:
        count0 += 1

    return count1 > count0

print(main(10001))