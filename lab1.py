#bai 1
poem = """
  i carry your heart with me (i carry it in
  my heart) i am never without it (anywhere
  i go you go, my dear, and whatever is done
  by only me is your doing, my darling)
  i fear no fate (for you are my fate, my sweet)
  i want no world (for beautiful you are my world, my true)
  and it's you are whatever a muon has always meant
  and whatever a sun will always sing is you

  here is the deepest secret nobody knows
  There is the root of the root and the bud of the bud
  and the sky of the sky of a tree called life, which grows
  higher than soul can hope or mind can hide)
  and this is the wonder that's keeping the stars apart

  i carry your heart (i carry it in my heart)
  --i carry your heart with me by e.e. cummings--
  """
lines = poem.split("\n")
for line in lines:
  print(line)
#bai 2
def quan_ly_thu_vien(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong):
  thong_tin_sach = f"""
Thư viện ĐHKTKTCN có {so_luong} sách {ten_sach} với mã số {ma_sach}. Cuốn sách của tác giả {tac_gia} được xuất bản vào năm {nam_xuat_ban}.
  """

  return thong_tin_sach

ma_sach = input("Nhập mã sách: ")
ten_sach = input("Nhập tên sách: ")
tac_gia = input("Nhập tác giả: ")
nam_xuat_ban = int(input("Nhập năm xuất bản: "))
so_luong = int(input("Nhập số lượng sách: "))

thong_tin_sach = quan_ly_thu_vien(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong)
print(thong_tin_sach)
#bai 3
so_tien_ban_dau = float(input("Nhập số tiền ban đầu: "))
lai_suat_hang_nam = float(input("Nhập lãi suất hàng năm: "))
amoun_after_5_years = so_tien_ban_dau * (1 + lai_suat_hang_nam / 100) ** 5
amoun_after_10_years = so_tien_ban_dau * (1 + lai_suat_hang_nam / 100) ** 10
grow_rate = (amoun_after_10_years-amoun_after_5_years)*100/amoun_after_5_years
print(f"Số tiền sau 5 nam là: {amoun_after_5_years:.2f}")
print(f"Số tiền sau 10 nam là: {amoun_after_10_years:.2f}")
print(f"Tỷ lệ tăng trưởng là: {grow_rate:.2f}%")
#bai 4
canh_day = float(input("Nhập độ dài cạnh đáy: "))
chieu_cao = float(input("Nhập chiều cao: "))
dien_tich_xq = 2* canh_day * chieu_cao
dien_tich_tp = dien_tich_xq +canh_day ** 2
the_tich = (1 / 3) (canh_day * 2)* chieu_cao
print(f"Diện tích xung quanh: {dien_tich_xq:.2f}")
print(f"Diện tích toàn phần: {dien_tich_tp:.2f}")
print(f"Thể tích: {the_tich:.2f}")
#bai 5
so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))
print(f"Số tiền điện cần phải trả là: {(( 1.5 * so_gio_su_dung ) * 5000):.2f} đồng")
#bai 6
toa_do_a = tuple(map(float, input("Nhập tọa độ vectơ A (x, y): ").split()))
toa_do_b = tuple(map(float, input("Nhập tọa độ vectơ B (x, y): ").split()))
do_dai_a = (toa_do_a[0]**2 + toa_do_a[1]**2)**0.5
do_dai_b = (toa_do_b[0]**2 + toa_do_b[1]**2)**0.5
 
print("Tọa độ vectơ A + B: ",toa_do_a[0] + toa_do_b[0], toa_do_a[1] + toa_do_b[1])
print("Tọa độ vectơ A - B: ",toa_do_a[0] - toa_do_b[0], toa_do_a[1] - toa_do_b[1])
print(f"Độ dài vectơ A: {do_dai_a:.2f}")
print(f"Độ dài vectơ B: {do_dai_b:.2f}")
print(f"Cosin góc giữa hai vectơ A và B: {(toa_do_a[0] * toa_do_b[0] + toa_do_a[1] * toa_do_b[1]) / (do_dai_a * do_dai_b):.2f}")
#bai 7
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))
print(f"Nghiệm của hệ phương trình là:")
print(f"x = {round((c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1), 2):.2f}")
print(f"y = {round((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1), 2):.2f}")
#bai 8
from math import *
x = float(input("Nhập giá trị của x: "))
z = float(input("Nhập giá trị của z: "))
print("f(x) =",round((((x**2)*sin(z)+abs(x)**0.5)/(log(z)+e**(x-1)))- atan(z*x),2))
#bai 9
mx, my = map(float, input("Nhập tọa độ x, y của điểm M: ").split())
nx, ny = map(float, input("Nhập tọa độ x, y của điểm N: ").split())
px, py = map(float, input("Nhập tọa độ x, y của điểm P: ").split())
qx, qy = map(float, input("Nhập tọa độ x, y của điểm Q: ").split())

mnx = (mx + nx) / 2
mny = (my + ny) / 2

npx = (nx + px) / 2
npy = (ny + py) / 2

pqx = (px + qx) / 2
pqy = (py + qy) / 2

qmx = (qx + mx) / 2
qmy = (qy + my) / 2

print("Tọa độ trung điểm MN:", mnx, mny)
print("Tọa độ trung điểm NP:", npx, npy)
print("Tọa độ trung điểm PQ:", pqx, pqy)
print("Tọa độ trung điểm QM:", qmx, qmy)

