#Cau 1
def chuyen_doi_sang_nhi_phan(so_nguyen_duong):
    if so_nguyen_duong == 0:
        return '0'
    so_nhi_phan = ''
    while so_nguyen_duong > 0:
        phan_du = so_nguyen_duong % 2
        so_nhi_phan = str(phan_du) + so_nhi_phan
        so_nguyen_duong = so_nguyen_duong // 2
    return so_nhi_phan

def main():
    nhap_so_nguyen_duong = int(input("Nhập số nguyên dương: "))
    if nhap_so_nguyen_duong < 0:
        print("Nhập số nguyên dương.")
        return
    Ra_so_nhi_phan = chuyen_doi_sang_nhi_phan(nhap_so_nguyen_duong)
    print("Số nhị phân tương ứng là:", Ra_so_nhi_phan)

if __name__ == "__main__":
    main()


#Cau 2
def chuoi_con_chung_ngan_nhat(str1, str2):
  dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

  for i in range(len(str1) + 1):
    for j in range(len(str2) + 1):
      if i == 0 or j == 0:
        dp[i][j] = 0
      elif str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  chuoi_con_chung = ""
  i = len(str1)
  j = len(str2)
  while i > 0 and j > 0:
    if str1[i - 1] == str2[j - 1]:
      chuoi_con_chung += str1[i - 1]
      i -= 1
      j -= 1
    else:
      if dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
      else:
        j -= 1

  chuoi_con_chung = chuoi_con_chung[::-1]
  return chuoi_con_chung

def main():
    str1 = input("Nhập chuỗi ký tự thứ nhất: ")
    str2 = input("Nhập chuỗi ký tự thứ hai: ")
    
    chuoi_con_chung = chuoi_con_chung_ngan_nhat(str1, str2)
    
    if chuoi_con_chung:
        print("Chuỗi ký tự con chung có độ dài ngắn nhất là:", chuoi_con_chung)
    else:
        print("Không có chuỗi ký tự con chung.")

if __name__ == "__main__":
    main()


#Cau 3
def tim_kiem_va_dem_tu(chuoi_van_ban, tu_can_tim):
  vi_tri = chuoi_van_ban.find(tu_can_tim)
  so_lan_xuat_hien = chuoi_van_ban.count(tu_can_tim)
  return vi_tri, so_lan_xuat_hien

def main():
  chuoi_van_ban = input("Nhập chuỗi văn bản: ")
  tu_can_tim = input("Nhập từ cần tìm kiếm: ")

  vi_tri, so_lan_xuat_hien = tim_kiem_va_dem_tu(chuoi_van_ban, tu_can_tim)

  if vi_tri != -1:
    print(f"Từ '{tu_can_tim}' xuất hiện tại vị trí {vi_tri} trong chuỗi văn bản.")
  else:
    print(f"Từ '{tu_can_tim}' không được tìm thấy trong chuỗi văn bản.")

  tu_dien = {}
  for tu in chuoi_van_ban.split():
    if tu in tu_dien:
      tu_dien[tu] += 1
    else:
      tu_dien[tu] = 1

  tu_xuat_hien_nhieu_nhat = max(tu_dien, key=tu_dien.get)
  so_lan_xuat_hien_nhieu_nhat = tu_dien[tu_xuat_hien_nhieu_nhat]

  print(f"Từ '{tu_xuat_hien_nhieu_nhat}' xuất hiện nhiều nhất với {so_lan_xuat_hien_nhieu_nhat} lần.")

if __name__ == "__main__":
  main()


#Cau 4
def kiem_tra_so_nguyen_to(n):
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

def main():

  chuoi_van_ban = input("Nhập chuỗi ký tự: ")
  chuoi_so = ""
  for ky_tu in chuoi_van_ban:
    if ky_tu.isdigit():
      chuoi_so += ky_tu
  if not chuoi_so:
    print("Chuỗi không chứa số.")
    return

  so = int(chuoi_so)

  if kiem_tra_so_nguyen_to(so):
    print(f"{so} là số nguyên tố.")
  else:
    print(f"{so} không phải là số nguyên tố.")

if __name__ == "__main__":
  main()


#Cau 5
def tron_chuoi_voi_dau_gach_noi(chuoi1, chuoi2):

  chuoi_ket_qua = ""
  for i in range(len(chuoi1)):
    if i < len(chuoi2):
      chuoi_ket_qua += chuoi1[i] + "-" + chuoi2[i]
    else:
      chuoi_ket_qua += chuoi1[i]

  return chuoi_ket_qua

def main():
  chuoi1 = input("Nhập chuỗi ký tự thứ nhất: ")
  chuoi2 = input("Nhập chuỗi ký tự thứ hai: ")

  chuoi_ket_qua = tron_chuoi_voi_dau_gach_noi(chuoi1, chuoi2)
  print(f"Chuỗi kết quả sau khi trộn: {chuoi_ket_qua}")

if __name__ == "__main__":
  main()


#Cau 6
def main():
  chuoi = input("Nhập chuỗi ký tự: ")
  ky_tu_dac_biet = {}
  tong_so_ky_tu = 0

  for ky_tu in chuoi:
    if not ky_tu.isalnum():
      if ky_tu not in ky_tu_dac_biet:
        ky_tu_dac_biet[ky_tu] = 0
      ky_tu_dac_biet[ky_tu] += 1
      tong_so_ky_tu += 1

  if ky_tu_dac_biet:
    print("Danh sách ký tự đặc biệt và số lần xuất hiện:")
    for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
      ty_le_phan_tram = (so_lan_xuat_hien / tong_so_ky_tu) * 100
      print(f"{ky_tu}: {so_lan_xuat_hien} lần ({ty_le_phan_tram:.2f}%)")
  else:
    print("Chuỗi không chứa ký tự đặc biệt.")

if __name__ == "__main__":
  main()


#Cau 7
def dem_chu_ky_tu(chuoi):
  so_luong = {
    "chu_thuong": 0,
    "chu_hoa": 0,
    "chu_so": 0,
    "ky_tu_dac_biet": 0
  }

  for ky_tu in chuoi:
    if ky_tu.islower():
      so_luong["chu_thuong"] += 1
    elif ky_tu.isupper():
      so_luong["chu_hoa"] += 1
    elif ky_tu.isdigit():
      so_luong["chu_so"] += 1
    else:
      so_luong["ky_tu_dac_biet"] += 1

  return so_luong

def main():
  chuoi = input("Nhập chuỗi ký tự: ")

  so_luong = dem_chu_ky_tu(chuoi)

  print(f"Số lượng chữ thường: {so_luong['chu_thuong']}")
  print(f"Số lượng chữ hoa: {so_luong['chu_hoa']}")
  print(f"Số lượng chữ số: {so_luong['chu_so']}")
  print(f"Số lượng ký tự đặc biệt: {so_luong['ky_tu_dac_biet']}")

if __name__ == "__main__":
  main()


#Cau 8
def main():
  chuoi = input("Nhập chuỗi ký tự: ")
  if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự.")
    return

#8.a
  chuoi_con_1 = chuoi[2:8]
  print(f"Chuỗi con từ vị trí thứ 2 đến vị trí thứ 8: {chuoi_con_1}")

#8.b
  chuoi_con_2 = chuoi[5:5+5]
  print(f"Chuỗi con gồm 5 ký tự kể từ vị trí thứ 5: {chuoi_con_2}")

#8.c
  chuoi_con_3 = chuoi[-3:]
  print(f"Chuỗi con từ cuối chuỗi gồm 3 ký tự: {chuoi_con_3}")

#8.d
  chuoi_thuong = chuoi.lower()
  print(f"Chuỗi sau khi chuyển đổi thành chữ thường: {chuoi_thuong}")

#8.e
  chuoi_hoa = chuoi.upper()
  print(f"Chuỗi sau khi chuyển đổi thành chữ hoa: {chuoi_hoa}")

#8.f
  chuoi_dao_nguoc = chuoi[::-1]
  print(f"Chuỗi sau khi đảo ngược: {chuoi_dao_nguoc}")

if __name__ == "__main__":
  main()


#Cau 9
def kiem_tra(s1, s2):

  if len(s1) > len(s2) + 1 or len(s2) > len(s1) + 1:
    return False

  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if i == 0 or i == len(s1) - 1:
        return s1[1:] == s2 or s1[:-1] == s2
      else:
        return s1[i-1] + s1[i+1] == s2
  return True

def main():
  s1 = input("Nhập chuỗi ban đầu: ")
  s2 = input("Nhập chuỗi đích: ")

  if kiem_tra(s1, s2):
    print(f"Có thể biến đổi '{s1}' thành '{s2}' bằng cách chỉnh sửa tối đa 1 ký tự.")
  else:
    print(f"Không thể biến đổi '{s1}' thành '{s2}' bằng cách chỉnh sửa tối đa 1 ký tự.")

if __name__ == "__main__":
  main()
