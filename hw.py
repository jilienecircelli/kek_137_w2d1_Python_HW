






# PYTHON HW TONIGHT 12/4
# 1.
list_num = []
num = 1

while True:
    cubed = num ** 3
    if cubed > 1000:
        break
    list_num.append(cubed)
    num += 1

print(list_num)

# 2.
primes = []

for num in range(2, 101):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)

print(primes)

# 3.
age = 80

if age < 18:
    print("Kids")
elif 18 <= age <= 65:
    print("Adults")
else:
    print("Seniors")