from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    person_n, second_m, fish_k = map(int, input().split())
    arrived_time_list = list(map(int, input().split()))
    arrived_time_list.sort()

    # 초당 붕어빵 생성 개수 구하기
    # 사람이 도착했을 때 게이지가 1이상이면 Possible 임
    flag = True
    for idx in range(person_n):
        gage = arrived_time_list[idx] // second_m

        # 하나도 안 가져갔을 때 만들어진 붕어빵 개수
        total_fish = gage * fish_k
        if total_fish - (idx+1) < 0:
            flag = False
            break
    if flag:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')