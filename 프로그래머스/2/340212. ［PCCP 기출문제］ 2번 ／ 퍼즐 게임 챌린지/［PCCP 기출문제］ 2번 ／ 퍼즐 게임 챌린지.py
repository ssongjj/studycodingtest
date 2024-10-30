def cal_time(diffs, times, level): # 걸리는 시간
    total = 0
    n = len(diffs)
    
    for i in range(n):
        diff = diffs[i]
        time_cur = times[i]
        
        if diff <= level:
            total += time_cur
        else:
            time_prev = times[i - 1] if i > 0 else 0
            total += (diff - level) * (time_cur + time_prev) + time_cur
    return total

def solution(diffs, times, limit):
    left, right = 1, max(diffs) # 최소 난이도와 최대 난이도
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if cal_time(diffs, times, mid) <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer