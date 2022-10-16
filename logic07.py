def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    q = a < 0 and b >= 0 or b < 0 and a >= 0
    return q

print(main(-3, 8))