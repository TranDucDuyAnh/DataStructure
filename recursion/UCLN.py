# Tìm UCLN sử dụng đệ quy 101

def UCLN(a, b):
    if b == 0:  # Trả về a bởi vì 0 chia hết cho mọi số a => a là UCLN
        return a
    else:  # Nếu b không bằng 0
        if b > a:  # Đổi vị trí hai số để tiện tính toán
            b, a = a, b
        # VD tìm UCLN của 18 và 12 -> 6
        # Bây giờ lấy 18%12 = 6 và tìm UCLN của 12 và 6 -> 6
        # Suy ra UCLN(18, 12) = UCLN(12, 18%12)
        return UCLN(b, a % b)


def main():
    a = abs(int(input("Nhap so a: ")))
    b = abs(int(input("Nhap so b: ")))
    ans = UCLN(a, b)
    print("UCLN cua 2 so la:", ans)


if __name__ == "__main__":
    main()
