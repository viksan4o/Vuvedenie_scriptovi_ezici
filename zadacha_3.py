a = int(input("Input number a: "))
b = int(input("Input number b: "))
if a > b:
    temp = a
    a = b
    b = temp
perfects = []
abundant_count = 0
for x in range(a, b + 1):
    if x <= 0:
        continue       
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i            
    if sum == x:
        perfects.append(x)
    elif sum > x:
        abundant_count += 1
if len(perfects) == 0:
    print("Not found")
else:
    for p in perfects:
        print(p, end=" ")
    print()
print(f"Аbundant: {abundant_count}")