#write a program to check the given number is special number or not
num=int(input())
summ=0
dummy=num
while dummy>0:
    rem=dummy%10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    summ+=fact
    dummy//=10

if summ==num:
    print('n is special number')
else:
    print('n is not special')