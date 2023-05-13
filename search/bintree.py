# Đối tượng nút với 3 thuộc tính
# + value: giá trị nút
# + left: nút con bên trái
# + right: nút con bên phải
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Đối tượng cây nhị phân với thuộc tính nút rễ
class BinaryTree:
    def __init__(self):
        self.root = None

    # Hàm thêm nút rễ
    def add_root_node(self, value):
        print("Đã thêm nút giá trị", value, "là nút gốc của cây")
        self.root = Node(value)

    # Hàm thêm nút mới giá trị value
    def add_new_node(self, value, curr):
        # Cây nhị phân tìm kiếm không có các nút có giá trị lặp lại
        if value == curr.value:
            print("Nút có giá trị", value, "đã tồn tại")
        # Nếu value nhỏ hơn giá trị nút hiện tại
        elif value < curr.value:
            if curr.left is None:  # Nút con trái không tồn tại thì tạo nút mới
                curr.left = Node(value)
                return
            else:  # Còn không thì tiếp tục kiểm tra
                self.add_new_node(value, curr.left)
        # Nếu value lớn hơn giá trị nút hiện tại
        elif value > curr.value:
            if curr.right is None:  # Nút con phải không tồn tại thì tạo nút mới
                curr.right = Node(value)
                return
            else:  # Còn không thì tiếp tục kiểm tra
                self.add_new_node(value, curr.right)

    # Hàm in hết nút với các nút con của chúng
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

    # Hàm tìm nút giá trị value
    def find_node(self, value, curr):
        # Nếu tìm thấy
        if value == curr.value:
            print("Nút có giá trị", value, "tồn tại")
        # Nếu value nhỏ hơn giá trị nút hiện tại
        elif value < curr.value:
            if curr.left is None:  # Cùng đường
                print("Không tìm thấy nút")
                return
            else:  # Tiếp tục tìm
                self.find_node(value, curr.left)
        # Nếu value lớn hơn giá trị nút hiện tại
        elif value > curr.value:
            if curr.right is None:  # Cùng đường
                print("Không tìm thấy nút")
                return
            else:  # Tiếp tục tìm
                self.find_node(value, curr.right)


if __name__ == '__main__':
    # Bắt đầu bằng 1 giá trị bất kì
    first_val = int(input("Nhập một giá trị để bắt đầu một cây nhị phân: "))
    # Tạo một cây nhị phân với nút gốc chứa giá trị vừa nhập
    binary_tree = BinaryTree()
    binary_tree.add_root_node(first_val)
    # Vòng lặp vô tận, khi bằng True thì kết thúc chương trình
    finish = False
    while finish is not True:
        # Câu lệnh bằng số
        print()
        print("HELP: 1 - Danh sách nút, 2 - Thêm nút con, 3 - Tìm kiếm, 4 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if select == 1:
            binary_tree.print_all_nodes(binary_tree.root)
            continue
        elif select == 2:
            child_node = int(input("Nhập giá trị của nút con mới: "))
            binary_tree.add_new_node(child_node, binary_tree.root)
            continue
        elif select == 3:
            search = int(input("Nhập giá trị cần tìm: "))
            binary_tree.find_node(search, binary_tree.root)
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")
        else:
            print("Số không hợp lệ!")
