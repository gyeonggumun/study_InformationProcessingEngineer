s = "Python Programming"

# 1. s[7:14] -> "Program"
# 2. .upper() -> "PROGRAM"
# 3. [::-1] -> "MARGORP"
result = s[7:14].upper()[::-1]

# "MARGORP"에서 인덱스 2번과 4번 글자 추출
print(result[2] + result[4]) # RO
