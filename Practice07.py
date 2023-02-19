def solution(book_time):
    # 시작시간을 기준으로 정렬
    book_time.sort(key = lambda x: x[0])
    # 끝나는 시간을 기준으로 비교
    end_times = []
    # 최소 객실 수
    min_rooms = 0
    # 예약 시간에 대한 번복
    for start, end in book_time:
        # 시작 예약 시간을 분 단위로 변환
        start_minutes = int(start[:2])*60+int(start[3:])
        # 종료 예약 시간을 분 단위로 변환
        end_minutes = int(end[:2])*60+int(start[3:])
        for i, end_time in enumerate(end_times):
            # 현재 예약 시간이 이전 예약 시간 종료보다 뒤인경우
            if start_minutes > end_time:
                end_times[i] = end_time + 10
                break
        # 예약할 방이 없는 경우
        else:
            end_times.append(end_minutes + 10)
            min_rooms+=1
    return min_rooms


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))
##
## [['14:10', '19:20'], ['14:20', '15:20'], ['15:00', '17:00'], ['16:40', '18:20'], ['18:20', '21:20']]
