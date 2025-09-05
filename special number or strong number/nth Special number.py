#write a program to print 10th special number
num = 1
count = 0
target = 10
while count < target:
    summ = 0
    dummy = num
    while dummy > 0:
        rem = dummy % 10
        fact = 1
        for i in range(1, rem + 1):
            fact *= i
        summ += fact
        dummy //= 10
    if summ == num:
        count += 1
        if count == target:
            print(num)
    num += 1
