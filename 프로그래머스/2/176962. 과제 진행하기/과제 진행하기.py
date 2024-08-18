def solution(plans):
    answer = []
    stack = []

    for plan in plans:
        # plan[1]은 시작 시간, plan[2]는 playtime
        hh, mm = map(int, plan[1].split(':')) 
        plan[1] = hh * 60 + mm  # 시작 시간을 분으로 변환
        plan[2] = int(plan[2])  # playtime을 정수로 변환
    
    # 과제 시작 시간 순으로 정렬
    plans.sort(key=lambda x: x[1])
    
    for i in range(len(plans) - 1):
        stack.append([plans[i][0], plans[i][2]])  # 과제 이름과 남은 시간을 스택에 추가
        diff = plans[i+1][1] - plans[i][1]  # 다음 과제 시작 시간과 현재 과제 시작 시간의 차이 계산
        
        while stack:
            if stack[-1][1] <= diff: 
                # 스택의 가장 최근 과제의 남은 시간이 diff보다 작거나 같으면 과제 완료
                comp_name, comp_time = stack.pop()
                diff -= comp_time
                answer.append(comp_name)
            else:
                # 스택의 최근 과제를 완전히 풀 수 없으면 남은 시간만 수정
                stack[-1][1] -= diff
                diff = 0
                break
    
    # 마지막 과제를 추가
    answer.append(plans[-1][0])   
    
    # 남아 있는 과제 처리
    while stack:
        name, remain_time = stack.pop()
        answer.append(name)
    
    return answer