def main():
    input_list = []
    n = abs(int(input("Nhap so phan tu n: ")))
    for i in range(n):
        print("Nhap so thu", i + 1, "=", end = " ")
        x = int(input(""))
        input_list.append(x)
    # Chuyển về set (là list nhưng giá trị không lặp lại 2 lần) để bỏ giá trị trùng lặp
    # Sau đó chuyển lại về list để lấy giá trị
    unique_val = list(set(input_list))
    for i in unique_val:
        print("(", i, ",", input_list.count(i), ")")


if __name__ == "__main__":
    main()
