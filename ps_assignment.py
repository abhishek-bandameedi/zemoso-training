def WINNER(arr,n):
    #[1,2,3,4,5,6,7]
    #alice: 1+3+5+7
    #bob: 2+4+6
    s=0
    alice=[]
    bob=[]
    for i in range(n):
        if i%2==0:
            alice.append(arr[i])
            s+=arr[i]
        else:
            bob.append(arr[i])
    if s%2==0:
        return "Alice wins"
    else:
        return "Bob wins"
n=int(input("enter the number of elements in the sequence: "))
arr=list(map(int,input("enter the sequence: ").split()))[:n]
print(WINNER(arr,n))
