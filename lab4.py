#Cau1
def main():
  tong = 0
  dem = 0
  so_le = []
  so_chan = []

  while tong <= 1000:
    so = int(input("Nhập số nguyên dương: "))
    dem += 1
    tong += so
    if so % 2 == 0:
      so_chan.append(so)
    else:
      so_le.append(so)
#a
  print("Các số lẻ đã nhập là:", so_le)
#b
  print("Các số chẵn đã nhập là:", so_chan)
#c
  print("Đếm số lượng số nguyên đã nhập là:", dem)

if __name__ == "__main__":
  main()

#Cau2.a
def main():
  so = 2

  while so < 100:
    so_nguyen_to = True
    for i in range(2, so):
      if so % i == 0:
        so_nguyen_to = False
        break

    if so_nguyen_to:
      print(so)

    so += 1

if __name__ == "__main__":
  main()

#Cau2.b
def main():
  so = 1
  while so <= 10:
    so_chinh_phuong = so * so
    print(so_chinh_phuong)
    so += 1

if __name__ == "__main__":
  main()

#Cau2.c
def main():
    a, b = 0, 1
    print(a)
    
    while b < 1000:
        print(b)
        a, b = b, a + b

if __name__ == "__main__":
    main()

#Cau3
def main():
  so = int(input("Nhập số nguyên: "))
  so_chu_so = 1

  while so // 10 > 0:
    so //= 10
    so_chu_so += 1
  print("Số chữ số của số nguyên đó là:", so_chu_so)

if __name__ == "__main__":
  main()

#Cau4.a
def main():
    n = int(input("Nhập số nguyên n (n > 10): "))
    
    S1 = 0
    a = 0
    so = 6

    while S1 <= n:
        S1 += so ** a
        a += 1

    print("Tổng S1 =", S1)

if __name__ == "__main__":
    main()

#Cau4.b
def main():
    n = int(input("Nhập số nguyên n (n > 10): "))
    
    S2 = 0
    a = 0
    so = 3

    while S2 <= n:
        S2 += 1 / (so ** (2 * a + 1))
        a += 1

    print("Tổng S2 =", S2)

if __name__ == "__main__":
    main()

#Cau4.c
def main():
    n = int(input("Nhập số nguyên n (n > 10): "))

    S3 = 0
    a = 1

    while a <= n:
        S3 += ((-1) ** a) * (a ** 2)
        a += 1

    print("Tổng S3 =", S3)

if __name__ == "__main__":
    main()

#Cau5
def main():
  while True:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))

    print("Chọn phép toán bạn muốn thực hiện:")
    print("1. Cộng (+) ")
    print("2. Trừ (-) ")
    print("3. Nhân (*) ")
    print("4. Chia (/) ")

    choice = int(input("Lựa chọn của bạn (1-4): "))

    if choice == 1:
      ketqua = a + b
      pheptoan = "+"
    elif choice == 2:
      ketqua = a - b
      pheptoan = "-"
    elif choice == 3:
      ketqua = a * b
      pheptoan = "*"
    elif choice == 4:
      ketqua = a / b
      pheptoan = "/"
    else:
      print("Lựa chọn không hợp lệ!")
      continue

    print(f"{a} {pheptoan} {b} = {ketqua}")

    tieptuc = input("Bạn muốn tiếp tục không (y/n): ")
    if tieptuc.lower() == "n":
      break

if __name__ == "__main__":
  main()
