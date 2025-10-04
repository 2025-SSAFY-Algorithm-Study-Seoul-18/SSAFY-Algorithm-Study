from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command_line = sys.stdin.readline().split()
    command = command_line[0]

    if command == "push":
        num = int(command_line[1])
        queue.append(num)  # 큐에 숫자 추가
    elif command == "pop":
        if queue:
            print(queue.popleft())  # 큐에서 가장 앞에 있는 원소 제거 후 출력
        else:
            print("-1")  # 큐가 비어있으면 -1 출력
    elif command == "size":
        print(len(queue))  # 큐의 크기 출력
    elif command == "empty":
        if not queue:
            print("1")  # 큐가 비어있으면 1 출력
        else:
            print("0")  # 큐가 비어있지 않으면 0 출력
    elif command == "front":
        if queue:
            print(queue[0])  # 큐의 가장 앞에 있는 원소 출력
        else:
            print("-1")  # 큐가 비어있으면 -1 출력
    elif command == "back":
        if queue:
            print(queue[-1])  # 큐의 가장 뒤에 있는 원소 출력
        else:
            print("-1")  # 큐가 비어있으면 -1 출력
