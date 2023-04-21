# Vẽ bàn cờ. 1 chỉ vị trí quân hậu được đặt vào bàn cờ
def draw_board(n):
    for i in range(n):
        for j in range(n):
            if j == queen_pos[i]:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()


# Kiểm tra nếu vị trí đặt quân hậu là an toàn. Có 3 điều kiện được kiểm tra
# 1. Không nằm trên cùng cột của những con hậu đã được đặt (Điều kiện đầu)
# 2. Không nằm trên đường chéo của con hậu đã được đặt (2 điều kiện sau)
# (Không kiểm tra hàng bởi nó luôn khác nhau)
def possible(line, col):
    for i in range(line):
        if queen_pos[i] == col or col - line == queen_pos[i] - i or col + line == queen_pos[i] + i:
            return False
    return True


# Tạo phương án. Nếu vị trí hợp lệ, đặt con hậu ở hàng i cột j và tăng hàng i lên 1
# Khi i = số hàng - 1, vẽ bàn cờ & phương án
def gen(i, n):
    for j in range(n):
        if possible(i, j):
            queen_pos[i] = j
            if i == n - 1:
                print(queen_pos)
                draw_board(n)
            gen(i+1, n)


n = abs(int(input("Nhap so n (tuong ung voi n quan hau tren ban co nxn): ")))
# Tạo list các quân hậu, với index chỉ số hàng (VD: 0 là hàng 1, 1 là hàng 2) và giá trị chỉ số cột
queen_pos = n * [0]
# Bắt đầu với hàng đầu tiên, tương ứng với quân hậu đầu tiên
# Mỗi quân hậu sẽ được đặt theo từng hàng từ trên xuống
gen(0, n)
