def binary_search(list, low, high, m):
    if high >= low:
        mid = (low + high)//2
        if list[mid] == m:
            print("Gia tri m nam o vi tri", mid)
            return
        elif m < list[mid]:
            return binary_search(list, low, mid - 1, m)
        elif m > list[mid]:
            return binary_search(list, mid + 1, high, m)
    else:
        print("Gia tri khong tim thay")
        return


if __name__ == "__main__":
    input_list = []
    n = abs(int(input("Nhap so phan tu n: ")))
    for i in range(n):
        print("Nhap so thu", i + 1, "=", end=" ")
        x = int(input(""))
        input_list.append(x)
    m = abs(int(input("Nhap phan tu can tim m: ")))
    binary_search(input_list, 0, n-1, m)
