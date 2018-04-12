#!/usr/bin/env python3.6.4


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = list(input().split(' '))
        try:
            a, b = int(a), int(b)
            try:
                print(a // b)
            except ZeroDivisionError as error:
                    print('Error code: {}'.format(str(error.args[0])))
        except ValueError as error:
            print('Error code: {}'.format(str(error.args[0])))
