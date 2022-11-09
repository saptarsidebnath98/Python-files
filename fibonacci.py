#Fibonacci series in python

def fibonacci(n):
    l1 = [0,1]
    sum = 1
    for i in range(0, n-2):
        sum = l1[i] + l1[i+1]
        l1.append(sum)
        
    for item in l1:
        print(f"--> {item}")
        
r = int(input("Enter range: "))
fibonacci(r)
        
