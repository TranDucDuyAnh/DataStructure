# Node class
class Node:

    # Hàm tạo node
    def __init__(self, data):
        self.data = data  # Thuộc tính dữ liệu, lấy tham số đầu vào data
        self.next = None  # Thuộc tính next trỏ đến nút tiếp theo
        # next mặc định là None


# Linked List class
class LinkedList:

    # Hàm tạo object danh sách liên kết
    def __init__(self):
        self.head = None

    # Hàm in nội dung danh sách liên kết bắt đầu từ node đầu (head)
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Hàm thêm node vào đầu danh sách
    def add_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Đã thêm nút giá trị", value, "vào đầu danh sách")

    # Hàm thêm node vào cuối danh sách
    def add_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print("Đã thêm nút giá trị", value, "vào cuối danh sách")

    # Hàm thêm node vào giữa 2 node có sẵn trong danh sách
    def add_after(self, node_value, value):
        curr_node = self.head
        while curr_node.data != node_value:
            if curr_node.next is None:
                print("Node không tồn tại")
                return
            curr_node = curr_node.next
        new_node = Node(value)
        new_node.next = curr_node.next
        curr_node.next = new_node
        print("Đã thêm nút giá trị", value, "vào sau nút", curr_node.data)

    # Xóa 1 node
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
            print("Đã xóa nút có giá trị", curr_node.data)
            curr_node.data = None
            return
        while curr_node.data != value:
            if curr_node.next is None:
                print("Node không tồn tại")
                return
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = curr_node.next
        print("Đã xóa nút có giá trị", curr_node.data)
        curr_node.data = None
        curr_node.next = None


if __name__ == '__main__':
    # Bắt đầu bằng list trống
    first_val = input("Nhập một giá trị để bắt đầu danh sách liên kết đơn: ")
    linked_list = LinkedList()
    linked_list.head = Node(first_val)
    finish = False
    while finish is not True:
        print()
        print("HELP: 11 - Thêm vào đâu, 12 - Thêm vào cuối, 13 - Thêm sau nút")
        print("HELP: 2 - In, 3 - Xóa, 4 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if select == 11:
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.add_at_beginning(next_val)
            continue
        elif select == 12:
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.add_at_end(next_val)
            continue
        elif select == 13:
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