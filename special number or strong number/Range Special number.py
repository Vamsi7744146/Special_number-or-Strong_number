#write a program to print factorial number given by range
LL=int(input())
UL=int(input())
for num in range(LL,UL+1):
    dummy=num
    summ=0
    while dummy>0:
        rem=dummy%10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
        dummy//=10
    if summ==num:
        print(num) 