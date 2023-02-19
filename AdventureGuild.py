n = int(input())
fears = list(map(int, input().split()))
fears.sort()  # 공포도를 기준으로 오름차순 정렬

count = 0  # 그룹 수
members = 0  # 그룹에 속한 모험가 수

for f in fears:
    members += 1  # 그룹에 모험가 추가
    if members >= f:  # 공포도 X명 이상인 그룹이 만들어지면
        count += 1  # 그룹 수 증가
        members = 0  # 그룹 초기화

print(count)
