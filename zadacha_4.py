n = int(input("Input a number: "))
while n < 5:
    n = int(input("Input a number: "))
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
twin_numbers = []
for p in range(2, n - 1):
    if p + 2 <= n and is_prime(p) and is_prime(p + 2):
        twin_numbers.append((p, p + 2))
        print(f"{p} {p + 2}")
print(f"Twins_count: {len(twin_numbers)}")
if twin_numbers:
    largest = twin_numbers[-1]
    print(f"The biggest twins: {largest[0]} {largest[1]}")