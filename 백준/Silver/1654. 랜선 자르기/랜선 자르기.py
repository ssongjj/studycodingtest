k, n = map(int, input().split())
length = [ int(input()) for _ in range(k)] #k개의 랜선의 길이를 받는다.

st = 1
en = max(length)   #나올 수 있는 가장 큰 길이는 k 랜선의 길이 중 최댓값이 됨


while st <= en:
    mid = (st + en) // 2 
    cnt = 0
    
    for i in length:
        cnt += i//mid 
    if cnt >= n: #자른 수가 n개보다 많으면 지금 길이보다 더 길어져야 됨 
        st = mid + 1
    else:
        en = mid - 1

print(en)
 