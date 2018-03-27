for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0:
        temp = i
    else:
        temp = ''
        if i % 3 == 0:
            temp += 'Fizz'
        if i % 5 == 0:
            temp += 'Buzz'
    print(temp, end=' ')
