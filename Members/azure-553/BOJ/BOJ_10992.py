import sys

star_n = int(sys.stdin.readline())

for i in range(star_n):
    if i == star_n - 1:
        print('*' * (2 * star_n - 1))
    elif i == 0:
        print(' ' * (star_n - 1) + '*')
    else:
        print(' ' * (star_n - 1 - i) + '*' + ' ' * (2 * i - 1) + '*')