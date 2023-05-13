# Duyệt từ trái sang phải và kết thúc chương trình khi tìm được/không tìm được giá trị cần tìm

def main():
    # Tạo một list
    input_list = []
    n = abs(int(input("Nhap so phan tu n: ")))
    for i in range(n):
        print("Nhap so thu", i + 1, "=", end = " ")
        x = int(input(""))
        input_list.append(x)
    m = abs(int(input("Nhap phan tu can tim m: ")))
    # Cho found = False, đây sẽ là dấu hiệu để biết nếu phần tử m có tồn tại
    found = False
    # Duyệt từng phần tử
    for i in range(n):
        if m == input_list[i]:  # Nếu bằng giá trị cần tìm
            print("Gia tri", m, "nam o vi tri", i)
            found = True  # Đã tìm thấy
    if not found:  # Còn không thì
        print("Khong tim thay gia tri m")


if __name__ == "__main__":
    main()
