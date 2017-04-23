number=int(input('请输入一个整数:'))
if number>0 :
        print('%d 是一个正'%number,end='')
        if(number%2==0):
                print('偶数')
        else:print('奇数')
elif number<0 :
        print('%d 是一个负'%number,end='')
        if(number%2==0):
                print('偶数')
        else:print('奇数')
else:print('0 是0')
