class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_root_node(self, value):
        print("Đã thêm nút giá trị", value, "là nút gốc của cây")
        self.root = Node(value)

    def add_new_node(self, value, curr):
        if value == curr.value:
            print("Nút có giá trị", value, "đã tồn tại")
        elif value < curr.value:
            if curr.left is None:
                curr.left = Node(value)
                return
            else:
                self.add_new_node(value, curr.left)
        elif value > curr.value:
            if curr.right is None:
                curr.right = Node(value)
                return
            else:
                self.add_new_node(value, curr.right)

    def print_all_nodes(self, root):
        if root:
            if (root.left is None) and (root.right is not None):
                print(root.value, "-> L: None | R:", root.right.value)
            elif (root.right is None) and (root.left is not None):
                print(root.value, "-> L:", root.left.value,"| R: None")
            elif (root.right is None) and (root.left is None):
                print(root.value, "-> L: None | R: None")
            else:
                print(root.value, "-> L:", root.left.value, "| R:", root.right.value)
            self.print_all_nodes(root.left)
            self.print_all_nodes(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value, end=" ")


if __name__ == '__main__':
    # Bắt đầu bằng 1 giá trị bất kì
    first_val = int(input("Nhập một giá trị để bắt đầu một cây nhị phân: "))
    # Tạo một cây nhị phân với nút gốc chứa giá trị vừa nhập
    binary_tree = BinaryTree()
    binary_tree.add_root_node(first_val)
    finish = False
    # Tạo vòng lặp vĩnh cửu, chương trình chỉ kết thúc khi finish = True
    while finish is not True:
        print()
        # Đoạn mã nhập lệnh bằng số đơn giản
        # Kiểm tra nếu số người dùng nhập vào là hợp lệ:
        # + Nếu hợp lệ thì thực hiện 1 trong những lệnh liệt kê bên dưới
        # + Nếu không thì báo lỗi và cho người dùng nhập lại
        print("HELP: 1 - Danh sách nút, 2 - Thêm nút con, 3 - Duyệt cây, 4 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if select == 1:
            binary_tree.print_all_nodes(binary_tree.root)
            continue
        elif select == 2:
            child_node = int(input("Nhập giá trị của nút con mới: "))
            binary_tree.add_new_node(child_node, binary_tree.root)
            continue
        elif select == 3:
            choice = abs(int(input("Chọn cách duyệt: 1 - Trước, 2 - Sau: ")))
            if choice == 1:
                binary_tree.preorder_traversal(binary_tree.root)
            elif choice == 2:
                binary_tree.postorder_traversal(binary_tree.root)
            else:
                print("Số không hợp lệ!")
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")
        else:
            print("Số không hợp lệ!")
