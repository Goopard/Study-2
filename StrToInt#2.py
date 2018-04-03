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
        n_copy = n
        result = 0
        while n_copy > 0:
            result += 1
            n_copy = n_copy // 10
        return result
    if len(s) == 1:
        return ord(s[0])
    elif len(s) == 0:
        return 0
    else:
        add = ord(s[len(s) - 1])
        int_s = str_to_int(s[:len(s) - 1]) * (10 ** len_of_int(add)) + add
        return int_s


a = 'adskdnladnlakndakldnalskdnaklsndakndlkansdlkanalsk'
print(str_to_int(a))
