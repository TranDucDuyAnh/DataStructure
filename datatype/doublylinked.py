# Node class
class Node:
    # Hàm tạo node
    def __init__(self, data):
        self.data = data  # Gán dữ liệu
        self.next = None
        self.prev = None
        # next và prev mặc định là None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Thuộc tính head mặc định là None

    # Thêm nút vào đầu danh sách
    def add_at_beginning(self, value):
        new_node = Node(value)  # Tạo nút mới
        new_node.next = self.head   # Trỏ phần next của nút vào nút đầu head
        if self.head is not None:   # Nếu nút head tồn tại, trỏ phần prev vào nút mới
            self.head.prev = new_node
        self.head = new_node    # Gán head cho nút mới
        print("Đã thêm nút giá trị", value, "vào đầu danh sách")

    # Chèn nút vào danh sách
    def add_after(self, node_value, value):
        curr_node = self.head
        while curr_node.data != node_value:
            if curr_node.next is None:
                print("Node không tồn tại")
                return
            curr_node = curr_node.next
        new_node = Node(value)  # Tạo nút mới
        new_node.next = curr_node.next  # Trỏ phần next của nút mới vào nút mà phần next của prev_node trỏ vào
        curr_node.next = new_node   # Trỏ phần next của prev_node vào nút mới
        new_node.prev = curr_node   # Trỏ phần prev của nút mới vào prev_node
        if new_node.next is not None:   # Nếu có nút nằm sau nút mới, cho phần prev của nút nằm sau đó trỏ vào nút mới
            new_node.next.prev = new_node
        print("Đã thêm nút giá trị", value, "vào sau nút", curr_node.data)

    # Xóa nút ở đầu danh sách
    def remove_node(self, value):
        if self.head is None:
            print("Danh sách trống!")
            return
        if (self.head.next is None) and (self.head.data == value):
            self.head = None
            print("Nút duy nhất trong danh sách đã bị xóa!")
            return
        curr_node = self.head
        if self.head.data == value:
            self.head = self.head.next
            self.head.prev = None
            print("Đã xóa nút có giá trị", curr_node.data)
            curr_node.data = None
            return
        while curr_node.data != value:
            if curr_node.next is None:
                print("Node không tồn tại")
                return
            curr_node = curr_node.next
        if curr_node.next is None:
            curr_node.prev.next = None
        else:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        print("Đã xóa nút có giá trị", curr_node.data)
        curr_node.data = None
        curr_node.next = None
        curr_node.prev = None

    # In list
    def print_list(self):
        node = self.head    # Bắt đầu từ nút đầu head
        while node is not None:  # Kiểm tra nếu nút có tồn tại
            print(node.data)    # In dữ liệu nút
            node = node.next    # Sang nút tiếp theo


if __name__ == "__main__":
    first_val = input("Nhập một giá trị để bắt đầu danh sách liên kết kép: ")
    linked_list = DoublyLinkedList()
    linked_list.head = Node(first_val)
    finish = False
    while finish is not True:
        print()
        print("HELP: 11 - Thêm vào đâu, 12 - Thêm sau nút")
        print("HELP: 2 - In, 3 - Xóa, 4 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if select == 11:
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.add_at_beginning(next_val)
            continue
        elif select == 12:
            after_node = input("Nhập giá trị nút để thêm sau nó: ")
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.add_after(after_node, next_val)
            continue
        elif select == 2:
            linked_list.print_list()
            continue
        elif select == 3:
            value = input("Nhập một giá trị bất kì: ")
            linked_list.remove_node(value)
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")
        else:
            print("Số không hợp lệ!")