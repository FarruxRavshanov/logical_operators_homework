def main(a, b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    c = a < 0 or b < 0
    return c

print(main(5, 7))