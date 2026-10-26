n = int(input("Enter a number (N): "))

a = 0
b = 1

print(f"Fibonacci numbers below {n}:")

while a < n:
    print(a, end=" ")  
    
    a, b = b, a + b