n = int(input())
if n == 0:
    print("No data")
else:
    min_val = n
    increases = 0
    negatives = 0
    total = 0
    if n < 0:
        negatives += 1
    total += 1
    previous = n
    while True:
        x = int(input())
        if x == 0:
            break  
        if x < min_val:
            min_val = x     
        if x > previous:
            increases += 1    
        if x < 0:
            negatives += 1    
        total += 1
        previous = x 
    percent = round((negatives / total) * 100)
    print(f"Smallest: {min_val}")
    print(f"Increases: {increases}")
    print(f"Negative: {percent}%")