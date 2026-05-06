# 2행 3열 구조의 리스트 생성
# [[0, 1, 2], [0, 1, 2]]
matrix = [[i for i in range(3)] for j in range(2)]

ans = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if (row + col) % 2 == 0:
            ans += matrix[row][col] # 인덱스 합이 짝수인 원소만 합산

print(ans) # 0 + 2 + 1 = 3
