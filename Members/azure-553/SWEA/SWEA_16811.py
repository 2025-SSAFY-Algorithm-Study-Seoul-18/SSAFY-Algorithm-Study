T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    carrot_li = list(map(int, input().split()))
    max_carrot_aize = 30

    counts = [0] * 31
    for carrot_size in carrot_li:
        counts[carrot_size] += 1

    min_diff = float('inf')

    for i in range(1, max_carrot_aize):
        for j in range(i + 1, max_carrot_aize+1):

            box_S = sum(counts[1 : i+1])
            box_M = sum(counts[i+1 : j+1])
            box_L = sum(counts[j+1 : 31])

            if box_S == 0 or box_M == 0 or box_L == 0:
                continue

            if box_S > N // 2 or box_M > N // 2 or box_L > N // 2:
                continue

            diff = max(box_S, box_M, box_L) - min(box_S, box_M, box_L)
            min_diff = min(min_diff, diff)

    if min_diff == float('inf'):
        result = -1
    else:
        result = min_diff

    print(f"#{test_case} {result}")