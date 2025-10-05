import sys

# 두 수를 문자열 형태로 입력받습니다.
a, b = sys.stdin.readline().split()

# 각 자릿수의 합을 저장할 리스트입니다.
result_parts = []

# 두 문자열의 마지막 인덱스에서 포인터를 시작합니다.
pointer_a = len(a) - 1
pointer_b = len(b) - 1

# 두 포인터 중 하나라도 유효한 위치에 있는 동안 반복합니다.
while pointer_a >= 0 or pointer_b >= 0:

    # a의 현재 자릿수를 가져옵니다. 포인터가 범위를 벗어나면 0으로 처리합니다.
    digit_a = 0
    if pointer_a >= 0:
        digit_a = int(a[pointer_a])

    # b의 현재 자릿수를 가져옵니다. 포인터가 범위를 벗어나면 0으로 처리합니다.
    digit_b = 0
    if pointer_b >= 0:
        digit_b = int(b[pointer_b])

    # 두 자릿수를 더한 값을 문자열로 변환하여 리스트에 추가합니다.
    result_parts.append(str(digit_a + digit_b))

    # 포인터를 왼쪽으로 한 칸씩 이동시킵니다.
    pointer_a -= 1
    pointer_b -= 1

# result_parts에는 [4, 4, 4, 4, 5] 와 같이 결과가 역순으로 저장되어 있습니다.
# reversed()로 리스트를 뒤집은 후, join()으로 합쳐서 최종 결과를 출력합니다.
print("".join(reversed(result_parts)))