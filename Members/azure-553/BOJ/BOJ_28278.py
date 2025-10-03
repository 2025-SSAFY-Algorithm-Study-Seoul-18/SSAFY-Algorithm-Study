import sys

# 명령 갯수 입력
order_n = int(sys.stdin.readline())

# Stack을 수행할 빈 배열 만들기
stack = []

for i in range(order_n):
    # 명령을 담을 배열
    number_li = input().split()

    # 맨 앞 요소가 1이라면
    if number_li[0] == '1':
        # stack에 push
        stack.append(number_li[1])
    # 2라면
    elif number_li[0] == '2':
        # Stack이 비어있지 않다면
        if stack:
            # 맨 위 값 빼고 출력
            print(stack.pop())
        else:
            print(-1)
    # Stack 길이 구하기
    elif number_li[0] == '3':
        print(len(stack))
    # Stack이 비었는지 확인
    elif number_li[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    # 맨 위의 정수 peek
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
