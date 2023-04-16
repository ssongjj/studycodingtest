n=int(input())
w=sorted(map(int,input().split()))

left=0
right=n-1
ans=[left,right]
m=abs(w[left]+w[right])

while(left<right):
    if abs(w[left]+w[right])<m:
        m=abs(w[left]+w[right])
        ans=[left,right]
        
    lleft = w[left+1]+w[right]
    rleft = w[left]+w[right-1]
    
    if abs(lleft)<abs(rleft):
        left+=1
    else:
        right-=1
        
print(str(w[ans[0]])+" "+str(w[ans[1]]))