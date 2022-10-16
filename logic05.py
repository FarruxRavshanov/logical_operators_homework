def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    d = a % 2 == 1 and b % 2 == 1
    return d

print(main(53, 77))