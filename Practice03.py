s = input()

#다음 숫자가 1로 바뀌는 경우 count
count0 = 0

#다음 숫자가 0으로 바뀌는 경우 count
count1 = 0

if s[0] =='1': count0+=1
else: count1+=1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        #다음 숫자가 1로 바뀌는 경우
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))