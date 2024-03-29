#câu 1
import math
while True:
    n = int(input("Nhập một số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương.")
    else:
        break
#a
S1 = sum(range(1, n + 1))
print("Tổng S1 =", S1)
#b
S2 = sum(1/i for i in range(1, n + 1))
print("Tổng S2=", S2)
#c
S3 = sum(1 / math.sqrt(2 * i) for i in range(1, n + 1))
print("Tổng S3 =", S3)
#d
S4 = sum((-1)**(i + 1) / i for i in range(1, n + 1))
print("Tổng S4 =", S4)
#câu 2
#a
total = 0

for number in range(2000, 4001):
    if number % 7 == 0 and number % 5 != 0:
        total += number

print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là:", total)
#b
total = 0

for number in range(500, 1001):
    if number % 4 == 0 and number % 6 != 0:
        total += number

print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000 là:", total)
#Câu 3
#a
def so_nguyen_to(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print("Các số nguyên tố từ 100 đến 1000:")
for num in range(100, 1001):
    if so_nguyen_to(num):
        print(num)
#b
print("Các số chính phương từ 1 đến 1000:")
for num in range(1, 1001):
    if num == int(num ** 0.5) ** 2:
        print(num)
#c
a, b = 0, 1
print("Chuỗi Fibonacci mà số cuối cùng nhỏ hơn 100:")
while a < 100:
    print(a, end=" ")
    a, b = b, a + b
#d
def so_hoan_hao(num):
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisor_sum == num

print("Các số hoàn hảo bé hơn 500:")
for number in range(1, 500):
    if so_hoan_hao(number):
        print(number)
#e
def so_ngu_giac(n):
    return n * (3 * n - 1) // 2

total = 0
for n in range(1, 201):
    total += so_ngu_giac(n)

print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 là:", total)


