def main():
    input_list = []
    n = abs(int(input("Nhap so phan tu n: ")))
    for i in range(n):
        print("Nhap so thu", i + 1, "=", end = " ")
        x = int(input(""))
        input_list.append(x)
    m = abs(int(input("Nhap phan tu can tim m: ")))
    found = False
    for i in range(n):
        if m == input_list[i]:
            print("Gia tri", m, "nam o vi tri", i)
            found = True
    if not found:
        print("Khong tim thay gia tri m")


if __name__ == "__main__":
    main()
