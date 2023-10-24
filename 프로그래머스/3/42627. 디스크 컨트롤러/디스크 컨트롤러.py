import heapq

def solution(jobs):
    answer = 0
    current_time = 0  # 현재 시간
    n = len(jobs)
    jobs.sort()  # 요청 시간 기준으로 정렬
    heap = []  # 최소 힙
    
    
    while jobs or heap:
        while jobs and jobs[0][0] <= current_time:
            request_time, job_time = jobs.pop(0)
            heapq.heappush(heap, (job_time, request_time))  # 작업 시간 기준으로 최소 힙에 추가
        
        if heap:
            job_time, request_time = heapq.heappop(heap)
            current_time += job_time
            answer += current_time - request_time
        else:
            current_time = jobs[0][0]  # 다음 작업 요청 시간으로 이동
        
    return answer // n