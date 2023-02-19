def solution(book_time):
    # 예약 시간대를 시작 시간 기준으로 정렬
    book_time.sort(key=lambda x: x[0])
    # 예약된 방의 퇴실 시간을 저장할 리스트
    end_times = []
    # 최소 객실 수
    min_rooms = 0
    # 각 예약 시간에 대해 번복
    for start, end in book_time:
        # 예약 시작 시간을 분 단위로 변환
        start_minutes = int(start[:2]) * 60 + int(start[3:])
        # 현재 예약 시간대가 사용 가능한 방이 있는지 확인
        end_minutes = int(end[:2]) * 60 + int(end[3:])
        for i, end_time in enumerate(end_times):
            # 현재 예약 시작 시간이 이전 예약 종료 시간 이후인 경우
            if start_minutes >= end_time:
                # 기존 예약 방을 현재 예약 시간대로 업데이트
                end_times[i] = end_minutes + 10
                break
        else:  # break를 거치지 않으면 실행되지 않음
            # 사용 가능한 방이 없는 경우 새로운 방을 추가
            end_times.append(end_minutes + 10)
            # 최소 객실 수 증가
            min_rooms += 1
    return min_rooms


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))
##
## [['14:10', '19:20'], ['14:20', '15:20'], ['15:00', '17:00'], ['16:40', '18:20'], ['18:20', '21:20']]
