# ip

l,u=map(int,input().split())
for num in range(l,u + 1):
    count=0
    for i in range(1,num+1):
           if (num % i) == 0:
               count+=1
    if(count==2):
        print(num)
