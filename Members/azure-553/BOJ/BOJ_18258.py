from collections import deque
import sys

# 큐 초기화
queue = deque()

# 명령 개수 입력 받기
order_n = int(input())

for _ in range(order_n):
    command = sys.stdin.readline().split()
    order_type = command[0]

    if order_type == 'push':
        order_num = command[1]
        queue.append(order_num)
    elif order_type == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif order_type == 'size':
        print(len(queue))
    elif order_type == 'empty':
        if not queue:
            print("1")
        else:
            print(0)
    elif order_type == 'front':
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif order_type == 'back':
        if queue:
            print(queue[-1])
        else:
            print("-1")