import sys
from collections import deque

# 줄 세우기를 위한 큐 생성
queue = deque()
# 명령어 개수 입력 받기
order_n = int(sys.stdin.readline())

# Q의 최대 길이 구하기
max_q_len = 0
# 사람 번호의 최솟값 구하기
min_person_number = float('inf')

for _ in range(order_n):
    order = sys.stdin.readline().split()
    # print(order)
    order_type = int(order[0])

    if order_type == 1:
        person_num = int(order[1])
        queue.append(person_num)

        current_len = len(queue)

        if current_len > max_q_len:
            max_q_len = current_len
            min_person_number = person_num
        # 길이가 같을 경우
        elif current_len == max_q_len:
            # 가장 작은 번호의 사람 구하기
            if person_num < min_person_number:
                min_person_number = person_num

    elif order_type == 2:
        if queue:
            queue.popleft()

print(max_q_len, min_person_number)