x = int(input('Please enter the first number: '))
y = int(input('Please enter the second number: '))
a = abs(x)
b = abs(y)
if x == 0 and y == 0:
    print('The greatest common divisor of 0 and 0 is undefined!')
    exit(0)
while a != b and a * b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
GCD = max(a, b)
print('The greatest common divisor of the numbers {} and {} is {}.'.format(x, y, GCD))
