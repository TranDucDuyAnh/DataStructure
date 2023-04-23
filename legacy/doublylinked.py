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
    def push(self, value):
        new_node = Node(value)  # Tạo nút mới
        new_node.next = self.head   # Trỏ phần next của nút vào nút đầu head
        if self.head is not None:   # Nếu nút head tồn tại, trỏ phần prev vào nút mới
            self.head.prev = new_node
        self.head = new_node    # Gán head cho nút mới

    # Chèn nút vào danh sách
    def insert(self, prev_node, value):
        if prev_node is None:   # Nếu prev_node không tìm thấy thì kết thúc
            print("Dùng push() nếu muốn thêm nút vào đầu danh sách")
            return
        new_node = Node(value)  # Tạo nút mới
        new_node.next = prev_node.next  # Trỏ phần next của nút mới vào nút mà phần next của prev_node trỏ vào
        prev_node.next = new_node   # Trỏ phần next của prev_node vào nút mới
        new_node.prev = prev_node   # Trỏ phần prev của nút mới vào prev_node
        if new_node.next is not None:   # Nếu có nút nằm sau nút mới, cho phần prev của nút nằm sau đó trỏ vào nút mới
            new_node.next.prev = new_node

    # Xóa nút ở đầu danh sách
    def delete_at_start(self):
        if self.head is None:   # Không có nút head
            print("Danh sách trống")
            return
        if self.head.next is None:  # Chỉ có nút head
            self.head = None
            return
        self.head = self.head.next  # Gán head là nút tiếp theo
        self.head.prev = None   # Xóa con trỏ prev của nút head

    # Xóa nút ở cuối danh sách
    def delete_at_end(self):
        if self.head is None:   # Không có nút head
            print("Danh sách trống")
            return
        if self.head.next is None:  # Chỉ có nút head
            self.head = None
            return
        n = self.head
        while n.next is not None:   # Kiểm tra nếu nút tiếp theo tồn tại
            n = n.next
        n.prev.next = None  # Xóa nút

    # In list
    def print_list(self):
        node = self.head    # Bắt đầu từ nút đầu head
        while node is not None:  # Kiểm tra nếu nút có tồn tại
            print(node.data)    # In dữ liệu nút
            node = node.next    # Sang nút tiếp theo


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.push(12)
    dllist.push(8)
    dllist.push(62)
    dllist.print_list()
    print()
    ''' 
                head
                  |                    
        +------+-----+------+     +-----+----+------+     +-----+----+------+ 
        | None | 62  |  o------------>  | 8  |  o------------>  | 12 | None | 
        |      |     |  <------------o  |    |  <------------o  |    |      |
        +------+-----+------+     +-----+----+------+     +-----+----+------+ 
    '''
    dllist.insert(dllist.head, 13)  # Thêm nút giá trị 13 sau nút đầu
    dllist.print_list()
    print()

    dllist.delete_at_start()
    dllist.print_list()
    print()

    dllist.delete_at_end()
    dllist.print_list()
    print()