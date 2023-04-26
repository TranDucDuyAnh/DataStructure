# 8 trường hợp có thể di chuyển của quân mã
# Ví dụ 2 giá trị x, y đầu tiên = -2, -1 có nghĩa là di chuyển 2 ô về bên trái và 1 ô lên trên
kx_move = [-2, -2, -1, -1, 1, 1, 2, 2]
ky_move = [-1, 1, -2, 2, -2, 2, -1, 1]


# Vẽ bàn cờ
def result():
    for i in range(n):  # Hàng
        for j in range(n):  # Cột
            print(chess[i][j], end=" ")  # In giá trị, giá trị đó biểu hiện bước đi của quân mã
        print()


def move(x, y):
    global step
    step += 1 # Tăng số bước lên 1
    chess[y][x] = step
    for i in range(8):  # Lặp lại 8 trường hợp quân mã có thể đi
        if step == n*n:   # Kiểm tra nếu số bước vượt quá số vị trí của bàn cờ. Nếu có thì kết thúc chương trình
            print("Buoc di chuyen cua quan ma:")
            result()
            quit()
        # Di chuyển đến vị trí mới
        u = x + kx_move[i]
        v = y + ky_move[i]
        if (u >= 0) and (u < n) and (v >= 0) and (v < n) and (chess[v][u] == 0):
            # Kiểm tra nếu vị trí mới nằm trong bàn cờ và vị trí đó chưa đi qua
            move(u, v)
    # Lùi lại 1 bước nếu không tìm được bước đi tiếp theo
    step -= 1
    chess[y][x] = 0  # Reset lại vị trí ô cờ thành ô chưa đi qua


flag = False


n = abs(int(input("Nhap so n (ban co nxn): ")))

# Khởi tạo số bước là 0 và tạo bàn cờ trống (tất cả các phần tử bằng 0)
step = 0
chess = [[0 for i in range(n)] for j in range(n)]


while not flag:
    print("HELP: Vi tri goc tren cung ben trai la x, y = (0, 0)")
    a = abs(int(input("Nhap vi tri xuat phat x: ")))
    b = abs(int(input("Nhap vi tri xuat phat y: ")))
    # Kiểm tra nếu vị trí ban đầu nằm ngoài bàn cờ. Nếu nằm ngoài người dùng phải nhập lại vị trí
    if a < n and b < n:
        flag = True
        move(a, b)
        print("No move")
    else:
        print("x hoac y vuot qua so luong quy dinh!")