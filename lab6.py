#Cau 1
def main():
  n = int(input("Nhập số lượng phần tử: "))
  mang_so_nguyen = []

  for i in range(n):
    so_nguyen = int(input(f"Nhập phần tử thứ {i + 1}: "))
    mang_so_nguyen.append(so_nguyen)

  tong_chan = 0
  tong_le = 0

  for so in mang_so_nguyen:
    if so % 2 == 0:
      tong_chan += so
    else:
      tong_le += so

  print(f"Tổng các số chẵn: {tong_chan}")
  print(f"Tổng các số lẻ: {tong_le}")

if __name__ == "__main__":
  main()

#Cau 2
def main():
  try:
    n = int(input("Nhập số lượng phần tử của mảng: "))
  except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số nguyên dương.")
    return
 
  mang = [int(input(f"Nhập phần tử thứ {i + 1} của mảng: ")) for i in range(n)]

  print("\nCác số nguyên tố trong mảng:")
  so_nguyen_to = [so for so in mang if so > 1 and all(so % i != 0 for i in range(2, int(so ** 0.5) + 1))]
  print(so_nguyen_to)

  print("\nCác số hoàn hảo trong mảng:")
  so_hoan_hao = [so for so in mang if so > 1 and sum(i for i in range(1, so) if so % i == 0) == so]
  print(so_hoan_hao)

if __name__ == "__main__":
  main()


#Cau 3
def main():
    try:
        numbers = [float(x) for x in input("Nhập dãy số: ").split()]
        
        if len(numbers) == 0:
            print("Dãy số rỗng.")
            return
        
        max_number = max(numbers)
        min_number = min(numbers)
        
        print("Số lớn nhất trong dãy số là:", max_number)
        print("Số nhỏ nhất trong dãy số là:", min_number)
    
    except ValueError:
        print("Vui lòng nhập các số nguyên hoặc số thực.")

if __name__ == "__main__":
    main()


#Cau 4
#a
def fibonacci(n):
  if n < 1:
    raise ValueError("n <= 1")
  
  return [0, 1] + [a + b for a, b in zip([0, 1], range(2, n))]

def main_fibonacci():
  try:
    n = int(input("Nhập số lượng số Fibonacci cần tạo: "))
  except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số nguyên.")
    return
  
  fibonacci_list = fibonacci(n)
  print(f"Dãy {n} số Fibonacci đầu tiên:")
  print(fibonacci_list)

if __name__ == "__main__":
  main_fibonacci()

#b
def is_prime(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def main_prime_numbers():
  prime_numbers = [num for num in range(2, 100) if is_prime(num)]
  print(f"Danh sách các số nguyên tố nhỏ hơn 100:")
  print(prime_numbers)

if __name__ == "__main__":
  main_prime_numbers()


#Cau 5
def main():
  try:
    day_so = [int(input(f"Nhập phần tử thứ {i + 1} của dãy số: ")) 
              for i in range(int(input("Nhập số lượng phần tử: ")))]
  except ValueError:
    print("Giá trị nhập vào không hợp lệ. Vui lòng nhập số nguyên.")
    return
  sai_so = [day_so[i + 1] - day_so[i] for i in range(len(day_so) - 1)]

  if len(set(sai_so)) == 1:
    print(f"Dãy số {day_so} là cấp số cộng.")
  else:
    print(f"Dãy số {day_so} không phải là cấp số cộng.")

if __name__ == "__main__":
  main()
