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

    x4 = n // 1000
    if x4 == 1:
        count1 += 1
    else:
        count0 += 1

    return count0 < count1

print(main(1110))