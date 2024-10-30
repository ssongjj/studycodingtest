def time_to_seconds(time):
    min, sec = map(int, time.split(':'))
    return min * 60 + sec

def seconds_to_str(sec):
    min = sec // 60
    sec = sec % 60
    return f"{min:02}:{sec:02}"

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    # 시간의 경우 전체를 최소인 초 단위로 맞추는 게 더 효율적
    video_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_st_sec = time_to_seconds(op_start)
    op_ed_sec = time_to_seconds(op_end)
    
    if op_st_sec <= pos_sec <= op_ed_sec:
        pos_sec = op_ed_sec
    
    for comm in commands:
        if comm == 'prev':
            pos_sec = max(0, pos_sec - 10)
        elif comm == 'next':
            pos_sec = min(pos_sec + 10, video_sec)

        if op_st_sec <= pos_sec <= op_ed_sec:
            pos_sec = op_ed_sec

    answer = seconds_to_str(pos_sec)

    return answer