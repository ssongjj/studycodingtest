def check_center(cur, num, hand):
    distance_dic = {2: {0: 3, 1: 1, 2: 0, 3: 1, 4: 2, 5: 1, 6: 2, 7: 3, 8: 2, 9: 3, "*": 4, "#": 4}
        , 5: {0: 2, 1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 1, 7: 2, 8: 1, 9: 2, "*": 3, "#": 3}
        , 8: {0: 1, 1: 3, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 0, 9: 1, "*": 2, "#": 2}
        , 0: {0: 0, 1: 4, 2: 3, 3: 4, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 2, "*": 1, "#": 1}}

    if distance_dic[num][cur[0]] < distance_dic[num][cur[1]]:
        cur[0] = num
        return 'L', cur
    elif distance_dic[num][cur[0]] > distance_dic[num][cur[1]]:
        cur[1] = num
        return 'R', cur
    else:
        if hand == "right":
            cur[1] = num
            return 'R', cur
        else:
            cur[0] = num
            return 'L', cur


def solution(numbers, hand):
    answer = ''
    cur = ["*", "#"]

    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            cur[0] = num
        elif num in (3, 6, 9):
            answer += 'R'
            cur[1] = num
        else:
            s, cur = check_center(cur, num, hand)
            answer += s

    return answer

