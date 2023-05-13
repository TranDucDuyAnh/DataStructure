# Hàm tìm kiếm nhị phân
# + list: mảng đầu vào
# + low: giá trị trái cùng
# + high: giá trị phải cùng
# + m: số cần tìm
def binary_search(list, low, high, m):
    # Nếu mảng có ít nhất 1 phần tử
    if high >= low:
        # Lấy phần tử nằm chính giữa
        mid = (low + high)//2
        # Phần tử giữa có giá trị cần tìm
        if list[mid] == m:
            print("Gia tri m nam o vi tri", mid)
            return
        # Nếu nhỏ hơn thì kiểm tra mảng con bên trái
        elif m < list[mid]:
            return binary_search(list, low, mid - 1, m)
        # Nếu lớn hơn thì kiểm tra mảng con bên phải
        elif m > list[mid]:
            return binary_search(list, mid + 1, high, m)
    else:
        print("Gia tri khong tim thay")
        return


if __name__ == "__main__":
    # Tạo một list
    input_list = []
    n = abs(int(input("Nhap so phan tu n: ")))
    for i in range(n):
        print("Nhap so thu", i + 1, "=", end=" ")
        x = int(input(""))
        input_list.append(x)
    m = abs(int(input("Nhap phan tu can tim m: ")))
    # Bắt đầu tìm kiếm
    binary_search(input_list, 0, n-1, m)
