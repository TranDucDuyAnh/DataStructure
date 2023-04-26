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
    # 1. Tạo node mới
    # 2. Cho ô next node mới trỏ vào node đầu
    # 3. Gán node đầu cho node mới
    def add_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Đã thêm nút giá trị", value, "vào đầu danh sách")

    # Hàm thêm node vào cuối danh sách
    # 1. Tạo node mới
    # 2. Nếu danh sách trống, gán head cho node mới
    # 3. Di chuyển đến node cuối danh sách
    # 4. Cho ô next node đó trỏ vào node mới
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

    # Hàm thêm node vào sau một node được chỉ định (nếu tồn tại)
    # 1. Duyệt hết danh sách đến khi tìm thấy node chỉ định, nếu không tìm thấy thì báo lỗi
    # 2. Tạo node mới
    # 3. Cho ô next của node mới trỏ vào node mà ô next của node chỉ định trỏ vào
    # 4. Cho ô next của node chỉ định trỏ vào node mới
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
    # 1. Kết thúc ngay khi danh sách trống
    # 2. Xóa node duy nhất head khi thỏa mãn giá trị value
    # 3. Nếu node head có giá trị value và không phải node duy nhất, gán head cho node nằm sau nó và xóa node
    # 4. Duyệt cho đến khi đến node có giá trị value, đồng thời gán prev_node cho node nằm sau node đang duyệt
    # 5. Cho ô next prev_node trỏ vào node mà curr_node trỏ vào và xóa curr_node
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
    # Bắt đầu bằng 1 giá trị bất kì
    first_val = input("Nhập một giá trị để bắt đầu danh sách liên kết đơn: ")
    # Tạo một danh sách liên kết đơn và gán head cho node với giá trị đã nhập vừa rồi
    linked_list = LinkedList()
    linked_list.head = Node(first_val)
    finish = False
    # Tạo vòng lặp vĩnh cửu, chương trình chỉ kết thúc khi finish = True
    while finish is not True:
        print()
        # Đoạn mã nhập lệnh bằng số đơn giản
        # Kiểm tra nếu số người dùng nhập vào là hợp lệ:
        # + Nếu hợp lệ thì thực hiện 1 trong những lệnh liệt kê bên dưới
        # + Nếu không thì báo lỗi và cho người dùng nhập lại
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