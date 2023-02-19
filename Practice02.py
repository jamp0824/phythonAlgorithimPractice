str = input()
print(str)
arr = []
for i in str: arr.append(int(i))
arr.sort()

result = 0
for i in arr:
    if result ==0 or i==0 : result+=i
    else: result*=i

print(result)

#it will not be converted to an integer and will cause a ValueError.

