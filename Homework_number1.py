def encode(text):
    result = ""
    i = 0
    while i < len(text):
        bukva = text[i]
        count = 0
        while i < len(text) and text[i] == bukva:
            count += 1
            i += 1
        result = result + bukva + str(count)
    return result

def decode(encoded_text):
    result = ""
    i = 0
    while i < len(encoded_text):
        bukva = encoded_text[i]
        count = int(encoded_text[i+1])
        result = result + (bukva * count)
        i += 2
    return result

n = int(input("Enter number 1 (to encode text) or 2 (to decode text): "))
if n == 1:
    text = input("Enter text: ")
    print("Result:", encode(text))
elif n == 2:
    text = input("Enter encoded text: ")
    print("Result:", decode(text))
else:
    print("Invalid choice!")