def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


def main():
    n = abs(int(input("Nhap so n: ")))
    ans = factorial(n)
    print("n! =", ans)


if __name__ == "__main__":
    main()