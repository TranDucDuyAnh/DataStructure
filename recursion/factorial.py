# Tính giai thừa bằng đệ quy
# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

def factorial(n):
    if n == 1:  # Điều kiện dừng n = 1
        return 1
    return n*factorial(n-1)  # n! = n * (n-1)!


def main():
    n = abs(int(input("Nhap so n: ")))
    ans = factorial(n)
    print("n! =", ans)


if __name__ == "__main__":
    main()
