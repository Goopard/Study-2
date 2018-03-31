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
    if len(s) == 1:
        return ord(s[0])
    else:
        add = ord(s[len(s) - 1])
        int_s = str_to_int(s[:len(s) - 1]) * (10 ** len_of_int(add)) + add
        return int_s


a = 'abcdefghABC'
print(str_to_int(a))
