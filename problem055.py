# Lychrel numbers

def is_lychrel(n):
    for i in range(50):
        number = n + int(str(n)[::-1])
        if str(number) == str(number)[::-1]:
            return False
        n = number
    return True

count = 0

for i in range(10001):
    if is_lychrel(i):
        count += 1

print(count)