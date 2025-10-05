'''
정사각형으로 직사각형 만들기
'''
import sys

rect_n = int(sys.stdin.readline())

count = 0

# 가로 길이 먼저 지정
for i in range(1, rect_n+1):
    # 세로길이
    for j in range(i, rect_n+1):
        # 만약 가로 * 세로가 넓이보다 넓으면
        if i * j > rect_n:
            # 멈추기
            break
        count += 1

print(count)