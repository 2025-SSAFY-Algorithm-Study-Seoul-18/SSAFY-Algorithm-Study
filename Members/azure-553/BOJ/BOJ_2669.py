matrix = [[0] * 100 for _ in range(100)]

count = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x_loc in range(x1, x2):
        for y_loc in range(y1, y2):
            if matrix[x_loc][y_loc] == 0:
                matrix[x_loc][y_loc] += 1
                count += 1
print(count)