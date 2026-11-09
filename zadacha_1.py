n = int(input("Input a number: "))
if n <= 0:
    print("Invalid count")
else:
    count_div_3 = 0
    positive_sum = 0
    positive_count = 0
    for _ in range(n):
        num = int(input("Input a number: "))
        if num % 3 == 0:
            count_div_3 += 1
        if num > 0:
            positive_sum += num
            positive_count += 1
    print(f"Multiples of 3: {count_div_3}")
    if positive_count > 0:
        avg = positive_sum / positive_count
        print(f"Average of positives: {avg:.2f}")
    else:
        print("Average of positives: No positives")