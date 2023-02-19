s = input()

# Remove any non-numeric characters from the input string
s = ''.join(filter(str.isdigit, s))

# If the string is empty, set the result to 0
if not s:
    result = 0
else:
    # 첫 번째 숫자를 결과값에 넣는다.
    result = int(s[0])

    for i in range(1, len(s)):
        # 현재 숫자와 결과값 중에서 하나라도 0 또는 1인 경우에는 덧셈을 수행한다.
        num = int(s[i])
        if num <= 1 or result <= 1:
            result += num
        # 그 외의 경우에는 곱셈을 수행한다.
        else:
            result *= num

print(result)
