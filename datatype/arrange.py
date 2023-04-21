find_val = []

def ascending(list):
    for i in range(0, len(list) - 1):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]


def find(list, value):
    pos = []
    for i in range(0, len(list)):
        if list[i] == value:
            pos.append(i)
    if len(pos) > 0:
        print("Gia tri", value, "tim thay o vi tri", pos)
    else:
        print("Gia tri khong tim thay")


def main():
    list = []
    n = abs(int(input("Nhap so phan tu n: ")))
    for i in range(n):
        print("Nhap so thu", i + 1, "=", end = " ")
        x = int(input(""))
        list.append(x)
    print(list)

    flag = False
    while not flag:
        value = input("Nhap gia tri can tim, nhap CANCEL de huy: ")
        if value == "CANCEL":
            flag = True
        else:
            value = int(value)
            find_val.append(value)

    for i in find_val:
        find(list, i)


if __name__ == "__main__":
    main()
