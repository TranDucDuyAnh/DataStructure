# Tạo đối tượng stack

class Stack:
    def __init__(self):
        self.stack = []  # Khởi tạo stack bằng 1 list trống

    def add(self, value):
        # Thêm phần tử vào cuối list dùng append() (LI - Last In)
        if value not in self.stack:
            print("Đã thêm phần tử giá trị", value)
            self.stack.append(value)
        else:
            print("Giá trị đã nằm trong stack!")

    def print_stack(self):
        print("Stack hiện tại:", self.stack)
        print("Giá trị nằm trên cùng stack:", self.peek())

    # Hàm peek() để trả giá trị được thêm cuối cùng vào stack
    def peek(self):
        return self.stack[-1]

    # Hàm remove() loại bỏ giá trị được thêm vào cuối cùng (FO - First Out)
    def remove(self):
        if len(self.stack) <= 0:
            return "Không thể bỏ giá trị nào"
        else:
            print("Đã xóa phần tử giá trị", self.peek())
            self.stack.pop()


if __name__ == "__main__":
    test_stack = Stack()
    first_val = input("Nhập một giá trị để bắt đầu stack: ")
    test_stack.add(first_val)
    finish = False
    while finish is not True:
        print()
        print("HELP: 1 - Thêm, 2 - In, 3 - Xóa, 4 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if (select > 4) or (select < 1):
            print("Số không hợp lệ!")
            continue
        elif select == 1:
            next_val = input("Nhập một giá trị bất kì để thêm vào stack: ")
            test_stack.add(next_val)
            continue
        elif select == 2:
            test_stack.print_stack()
            continue
        elif select == 3:
            test_stack.remove()
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")

