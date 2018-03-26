x = int(input('Please enter the first number: '))
y = int(input('Please enter the second number: '))
a = abs(x)
b = abs(y)
while (a != b) & (a * b != 0):
    if a > b:
        a = a % b
    else:
        b = b % a
GCD = max(a, b)
if (x == 0) & (y == 0):
    print('The greatest common divisor of 0 and 0 is undefined!')
else:
    print('The greatest common divisor of the numbers {} and {} is {}.'.format(x, y, GCD))
