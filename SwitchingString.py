s = input() # 문자열 입력 받기

count = 0 # 뒤집는 횟수를 기록할 변수
current = s[0] # 첫번째 문자를 기준으로 설정

for i in range(1, len(s)): # 두번째 문자부터 마지막 문자까지 확인
    if s[i] != current: # 현재 문자와 이전 문자가 다르면 뒤집는 행동을 진행
        count += 1
        current = s[i] # 기준 문자를 현재 문자로 변경

print(count)
