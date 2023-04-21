# Bài toán tháp Hà Nội
# Giải thuật:
# - Chuyển n-1 đĩa sang cột trung gian B
# - Chuyển đĩa n sand cột đích C
# - Chuyển n-1 đĩa từ cột trung gian B sand cột đích C

def hanoi(n, A, B, C):
    if n == 1:
        print("Dia 1 tu", A, "sang", C) # Nếu chỉ có 1 đĩa, ta chuyển ngay sang cột đích C
        return
    hanoi(n - 1, A, C, B)  # Chuyển n-1 đĩa sang cột B, C làm cột trung gian
    print("Dia", n, "tu", A, "sang", C)  # Chuyển đĩa n sang cột C, B làm cột trung gian
    hanoi(n - 1, B, A, C) # Chuyển n-1 đĩa từ cột B sang cột C, A làm cột trung gian


def main():
    n = abs(int(input("Nhap so dia n: ")))
    hanoi(n, "A", "B", "C")
    print("So buoc:", 2**n - 1)


if __name__ == "__main__":
    main()
