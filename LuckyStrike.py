import sys
n_list = list(map(int,sys.stdin.readline().rstrip()))
result1 = 0
result2 = 0
for i in range(len(n_list)):
    if i < (len(n_list)/2) : result1+=n_list[i]
    else: result2+=n_list[i]

if result1 == result2: print("LUCKY")
else: print("READY")