def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a % 10
    x2 = a // 10 % 10
    x3 = a // 100
    s = (x1 + x2 + x3) % 2 == 1
    return s

print(main(122))