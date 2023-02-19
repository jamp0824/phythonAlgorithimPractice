n = int(input())
fear = list(map(int,input().split()))
fear.sort()
result =0
group = 0
for i in fear:
    result+=1
    if(result>=i ):
        group +=1
        result = 0

print(group)



