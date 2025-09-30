arr_cnt, day = map(int, input().split())
arr = list(map(int, input().split()))

if arr_cnt < day:
    print(sum(arr))
else:
    current_sum = sum(arr[0:day])
    max_num = current_sum

    for i in range(1, arr_cnt - day + 1):
        current_sum = current_sum - arr[i-1] + arr[i+day-1]
        max_num = max(max_num, current_sum)
    print(max_num)