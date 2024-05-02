#Cau 1
def t(N):
    return {x: x**3 for x in range(1, N+1)}
if __name__ == "__main__":
    N = int(input("Nhập vào số nguyên N: "))
    NGUYEN_TRAN_MINH_VU = t(N)
    print(NGUYEN_TRAN_MINH_VU)

#Cau 2
def xep_loai(diem):
    if diem < 4.0:
        return 'F' 
    elif 4.0 <= diem <= 5.4:
        return 'D'
    elif 5.5 <= diem <= 6.9:
        return 'C'
    elif 7.0 <= diem <= 8.4:
        return 'B'
    else:
        return 'A'

if __name__ == "__main__":
    thong_tin_sinh_vien = {}
    thong_ke_hoc_luc = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for i in range(10):
        ten,diem = input(f"Nhập tên sinh viên thứ {i+1}: "),float(input("Nhập điểm thi: "))
        loai = xep_loai(diem)
        thong_tin_sinh_vien[ten] = {'Điểm': diem, 'Xếp loại': loai}
        thong_ke_hoc_luc[loai] += 1
    print("\nThông tin và xếp loại học lực của sinh viên:")
    for ten, info in thong_tin_sinh_vien.items():
        print(f"{ten}: Điểm - {info['Điểm']}, Xếp loại - {info['Xếp loại']}")
    print("\nThống kê số lượng sinh viên theo học lực:")
    for loai, so_luong in thong_ke_hoc_luc.items():
        print(f"Học lực {loai}: {so_luong} sinh viên")

#Cau 3
def dem_tu(van_ban):
    tu_dem = {}
    for tu in van_ban.split():
        if tu in tu_dem:
            tu_dem[tu] += 1
        else:
            tu_dem[tu] = 1
    
    tu_nhieu_nhat = max(tu_dem, key=tu_dem.get)
    tu_it_nhat = min(tu_dem, key=tu_dem.get)
    
    return tu_nhieu_nhat, tu_dem[tu_nhieu_nhat], tu_it_nhat, tu_dem[tu_it_nhat]

if __name__ == "__main__":
    van_ban = """Dog is a pet animal It is the oldest friend of human beings
             It watches our house 
             It is very faithful animal and never left his master
             It is used by police to fight crime Sheep- rearers also use them.
             Thus it is useful for us in many ways"""
    tu_nhieu_nhat, so_lan_nhieu_nhat, tu_it_nhat, so_lan_it_nhat = dem_tu(van_ban)
    
    print(f"Từ xuất hiện nhiều nhất: '{tu_nhieu_nhat}' với {so_lan_nhieu_nhat} lần.")
    print(f"Từ xuất hiện ít nhất: '{tu_it_nhat}' với {so_lan_it_nhat} lần.")

#Cau 4
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)

#Cau 5
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = {san_pham: (so_luong, gia_tien[san_pham], so_luong * gia_tien[san_pham]) 
           for san_pham, so_luong in kho.items()}
print("Hóa đơn mua hàng:")
for san_pham, (so_luong, don_gia, thanh_tien) in hoa_don.items():
    print(f"{san_pham},Số lượng: {so_luong}, Đơn giá: {don_gia},Số tiền: {thanh_tien}")

print(f"Tổng số tiền của hóa đơn: {sum(kho[san_pham] * gia_tien[san_pham] for san_pham in kho)}")
print("\nSố lượng của các mặt hàng trong kho sau khi mua:")
for san_pham, so_luong in kho.items():
    print(f"{san_pham}: {so_luong}")