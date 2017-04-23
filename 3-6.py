sum=0
for x in range(1,11):
        tmp=1
        for i in range(1,x+1):
                tmp*=i
        sum+=tmp
print('前十个数的阶乘为%d'%sum)
                
        
