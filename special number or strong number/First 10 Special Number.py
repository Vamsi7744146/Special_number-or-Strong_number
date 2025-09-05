#write a program to print first 10 special numbers
num=1
target=10
count=0

while target>count:
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
        print(num)
        count+=1  
    num+=1