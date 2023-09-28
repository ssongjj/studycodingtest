from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    queue1_sum, queue2_sum = sum(queue1), sum(queue2)
    total_sum = queue1_sum + queue2_sum
    
    #만약 합친 값을 2로 나눴는데 나머지가 있을 때는 -1 
    if total_sum % 2 != 0:
        return -1
    
    for i in range(300000):
        if queue1_sum == queue2_sum:
            return i
        elif queue1_sum > queue2_sum:
            num = queue1.popleft()
            queue2.append(num)
            queue1_sum -= num
            queue2_sum += num
        else: 
            num = queue2.popleft()
            queue1.append(num)
            queue2_sum -= num
            queue1_sum += num
    return -1