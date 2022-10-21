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

    if n % 10 == 1:
        count1 += 1
    else:
        count0 += 1

    if n // 10 % 10 == 1:
        count1 += 1
    else:
        count0 += 1

    if n // 100 % 10 == 1:
        count1 += 1
    else:
        count0 += 1

    if n // 1000 % 10 == 1:
        count1 += 1
    else:
        count0 += 1

    if n // 10000 == 1:
        count1 += 1
    else:
        count0 += 1

    return count1 > count0

print(main(10101))