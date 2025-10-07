'''
한 줄씩 입력 받아서
열린 괄호일 경우 스택에 넣고 닫힌 괄호를 만나면 pop
Stack에 남아있으면 No 출력
빈 스택이면 YES 출력


'''
import sys

# 온점을 기준으로 여러줄 받기
sentences = []

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break
    sentences.append(sentence)
# print(sentences)
vps = {
    '(': ')',
    '[': ']'
}

for st in sentences:
    stack = []
    is_balanced = True

    for char in st:
        if char in vps.keys():
            stack.append(char)
        elif char in vps.values():
            if not stack or vps[stack.pop()] != char:
                is_balanced = False
                break
    # print(stack)

    if not stack and is_balanced:
        print("yes")
    else:
        print("no")