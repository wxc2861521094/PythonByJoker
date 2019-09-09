# 在Python中除了None，0和False，其他都代表True/
# 命名变量要见名思议。
# Python/Python3 da01.py
# in是判断在容器中(可迭代对象)有没有这个东西

# 153 = 1**3 + 5 **3 + 3 **3
#Number = input('请输入一个数字:')

#bai = int(Number[0])
#shi = int(Number[1])
#ge = int(Number[2])

#if bai **3 + shi **3 + ge **3 == int(Number):
#    print('是水仙花')
#else:
#    print('不是水仙花')







#1.
#celsius=float(input('输入温度:'))
#fahrenheit=(9/5)*celsius+32
#print('%.1f华氏度 is %.1f摄氏度'%(celsius,fahrenheit))

#2.
#import math
#r=float(input('输入圆的半径:'))
#h=float(input('输入圆的高:'))
#area=r*r*math.pi
#volume=area*h
#print('%.2f面积'%area)
#print('%.2f体积'%volume)

#3.
#feet=float(input('输入一个英尺：'))
#meters=feet*0.305
#print('%.3ffeet is %.3fmeters'%(feet,meters))

#4.
#M=float(input('输入以千克计量的水量：'))
#initialtemperature=float(input('输入水的初始温度:'))
#finaltemperature=float(input('输入水的最终温度:'))
#Q=M*(finaltemperature - initialtemperature)*4184
#print('所需能量：%.2fQ'%(Q))

#5.
#balance = float(input('请输入差额：'))
#interest_rate = float(input('请输入年利率：'))
#insterest = balance * (interest_rate / 1200)
#print('下月需付利息:%.5f' %insterest)

#.6
#v0=float(input('输入初始速度：'))
#v1=float(input('输入末速度:'))
#t=float(input('输入所占的时间：'))
#a=(v1-v0)/t
#print('平均加速度：%.2f' %a)

#7.
#num = float(input('请输入每月存款数：'))
#rate = 0.05 / 12
#interest = 1 + rate
#count =[0]
#for i in range(6):
#    month = (100 + count[i]) * interest
#    count.append(month)
#print('六个月后的账户总额：%.2f' % count[6])


#8.
#num=int(input('请输入一个0-1000的数：'))
#ge=int(num/100)
#shi=int(num/10%10)
#bai=int(num%10)
#sum=ge+shi+bai
#print('各位数字之和为：',sum)