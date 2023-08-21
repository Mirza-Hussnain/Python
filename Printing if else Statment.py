a = 20
b = 10
c = 25

if a > b and a > c:
    print('a is the greatest')
elif b > a and b > c:
    print('b is the greatest')
elif c > a and c > b:
    print('c is the greatest')
else:
    print('Some numbers are equal or there was an issue with the comparison')