count=0
for i in range(10000,100000):
        if i%10==6 and i%3==0 :
                count+=1
print('个位数为6且能被3整除的五位数共有%d个'%count)               
        
