# Tạo đối tượng stack

class Stack:
    def __init__(self):
        self.stack = []  # Khởi tạo stack bằng 1 list trống

    def add(self, value):
        # Thêm phần tử vào cuối list dùng append() (LI - Last In)
        if value not in self.stack:
            self.stack.append(value)
        else:
            print("Gia tri da nam trong stack!")

    # Hàm peek() để trả giá trị được thêm cuối cùng vào stack
    def peek(self):
        return self.stack[-1]

    # Hàm remove() loại bỏ giá trị được thêm vào cuối cùng (FO - First Out)
    def remove(self):
        if len(self.stack) <= 0:
            return "Không thể bỏ giá trị nào"
        else:
            return self.stack.pop()


# Tạo stack
test_stack = Stack()

# Thêm 2 phần tử vào stack
test_stack.add("Mon")
test_stack.add("Tue")

# Xem phần tử thêm vào cuối cùng. Trả về "Tue"
print(test_stack.peek())

# Thêm 2 phần tử vào stack
test_stack.add("wed")
test_stack.add("Thu")

# Xem phần tử thêm vào cuối cùng. Trả về "Thu"
print(test_stack.peek())

# Bỏ phần tử thêm vào cuối cùng
test_stack.remove()

# Xem phần tử thêm vào cuối cùng. Trả về "Wed"
print(test_stack.peek())
