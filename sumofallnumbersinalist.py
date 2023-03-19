num = list(input().split())

def sumoflist(num):
    sum=0
    for i in num:
        
        sum = sum + int(i) 
    return sum 
result = sumoflist(num)
print(result)