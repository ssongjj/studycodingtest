import math

def solution(wallet, bill):
    answer = 0

    while min(wallet) < min(bill) or max(wallet) < max(bill):
        if bill[0] > bill[1]:
            bill[0] = math.floor(bill[0]/2)
        else:
            bill[1] = math.floor(bill[1]/2)
        print(bill)
        answer += 1
    return answer