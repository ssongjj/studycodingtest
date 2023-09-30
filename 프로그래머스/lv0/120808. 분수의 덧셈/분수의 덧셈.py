def solution(numer1, denom1, numer2, denom2):
    numer = denom1 * numer2 + denom2 * numer1
    denom = denom1 * denom2
    for i in range(denom, 1, -1):
        if numer % i == 0 and denom % i == 0:
            numer = numer // i
            denom = denom // i
    answer = [numer, denom]
    return answer