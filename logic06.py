def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is positive".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    z = a >= 0 and b < 0 or b >= 0 and a < 0
    return z

print(main(-3, -2))