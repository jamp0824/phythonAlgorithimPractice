def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    zeroCount = 0
    actualWinNumCount = 0
    maxCount = 0
    for i in lottos:
        if i == 0: zeroCount+=1
        if i in win_nums: actualWinNumCount+=1

    maxCount = zeroCount + actualWinNumCount

    if maxCount == 6: answer.append(1)
    elif maxCount==5: answer.append(2)
    elif maxCount==4: answer.append(3)
    elif maxCount==3: answer.append(4)
    elif maxCount==2: answer.append(5)
    else: answer.append(6)

    if actualWinNumCount == 6: answer.append(1)
    elif actualWinNumCount==5: answer.append(2)
    elif actualWinNumCount==4: answer.append(3)
    elif actualWinNumCount==3: answer.append(4)
    elif actualWinNumCount==2: answer.append(5)
    else: answer.append(6)

    return answer

lottos = [0,0,0,0,0,0]
win_nums = [1,2,3,4,5,6]

solution(lottos,win_nums)