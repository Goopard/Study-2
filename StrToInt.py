def str_to_int(s: str) -> int:
    """This function transforms some string s to an integer.

    :param s: String that will be transformed.
    :type s: str.
    :returns int.
    """
    def len_of_int(n: int) -> int:
        """This function counts the number of digits in an integer.

        :param n: integer.
        :type n: int.
        :returns int.
        """
        temp = n
        res = 0
        while temp > 0:
            res += 1
            temp = temp // 10
        return res
    int_s = ord(s[0])
    for i in range(1, len(s)):
        int_s = int_s * (10 ** len_of_int(ord(s[i]))) + ord(s[i])
    return int_s


s = str(input('Please enter the string: '))
print(str_to_int(s))
