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
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Hàm thêm node vào đầu danh sách
    def addAtBeginning(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    # Hàm thêm node vào cuối danh sách
    def addAtEnd(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode

    # Hàm thêm node vào giữa 2 node có sẵn trong danh sách
    def addInBetween(self, mid_node, data):
        if mid_node is None:
            print("Node không tồn tại")
            return
        NewNode = Node(data)
        NewNode.next = mid_node.next
        mid_node.next = NewNode

    # Xóa 1 node
    def removeNode(self, value):
        head_val = self.head
        if head_val is not None:
            if head_val.data == value:
                self.head = head_val.next
                head_val.data = None
                return
        while head_val is not None:
            if head_val.data == value:
                break
            prev = head_val
            head_val = head_val.next
        if head_val is None:
            return
        prev.next = head_val.next
        head_val = None


if __name__ == '__main__':
    # Bắt đầu bằng list trống
    llist = LinkedList()

    llist.head = Node("apple")  # Tạo node 1, cho nó là node đầu (head)
    second = Node("banana")  # Tạo node 2
    third = Node("orange")  # Tạo node 3

    ''' 
    3 node đã được tạo với 3 nhãn: head, second, third

    llist.head              second                 third 
         |                    |                      | 
         |                    |                      | 
    +--------+------+     +---------+------+     +--------+------+ 
    | apple  | None |     | banana  | None |     | orange | None | 
    +--------+------+     +---------+------+     +--------+------+ 
    '''

    llist.head.next = second  # Nối node 1 với node 2

    ''' 
    Bây giờ phần next của node 1 chỉ vào node 2, nên chúng nối với nhau (1 chiều)

    llist.head              second                 third 
         |                    |                      | 
         |                    |                      | 
    +--------+------+     +---------+------+     +--------+------+ 
    | apple  |  o-------->| banana  | None |     | orange | None | 
    +--------+------+     +---------+------+     +--------+------+   
    '''

    second.next = third  # Nối node 2 với node 3

    ''' 
    Bây giờ phần next của node 2 chỉ vào node 3, nên bây giờ 3 node đã liên kết với nhau

    llist.head              second                 third 
         |                    |                      | 
         |                    |                      | 
    +--------+------+     +---------+------+     +--------+------+ 
    | apple  |  o-------->| banana  |  o-------->| orange | None | 
    +--------+------+     +---------+------+     +--------+------+    
    '''

    llist.printList()
    print("------")

    llist.addAtBeginning("grape")
    llist.printList()
    print("------")
    ''' 
    Lúc này node đầu (head) chuyển cho node mới thêm vào. Node mới liên kết với node head cũ
    Node tên second và third vẫn giữ nguyên
        llist.head                                     second                 third 
             |                                           |                      | 
             |                                           |                      | 
        +--------+------+     +---------+------+     +--------+------+       +--------+------+
        | grape  |  o-------->| apple   |  o-------->| banana |  o---------->| orange | None |
        +--------+------+     +---------+------+     +--------+------+       +--------+------+
    '''

    llist.addAtEnd("mango")
    llist.printList()
    print("------")
    ''' 
    Node cuối trong danh sách cũ liên kết với node mới được thêm vào
        llist.head                                     second                 third 
             |                                           |                      | 
             |                                           |                      | 
        +--------+------+     +---------+------+     +--------+------+       +--------+------+     +-------+------+
        | grape  |  o-------->| apple   |  o-------->| banana |  o---------->| orange |  o-------->| mango | None |
        +--------+------+     +---------+------+     +--------+------+       +--------+------+     +-------+------+
    '''

    llist.addInBetween(third, "strawberry")
    llist.printList()
    print("------")
    ''' 
    Node mới được đặt sau node tên third
        llist.head                                     second                 third 
            |                                           |                      | 
            |                                           |                      | 
        +--------+------+     +---------+------+     +--------+------+       +--------+------+     +------------+------+
        | grape  |  o-------->| apple   |  o-------->| banana |  o---------->| orange |  o-------->| strawberry |  o----
        +--------+------+     +---------+------+     +--------+------+       +--------+------+     +------------+------+
        
        
             +-------+------+
        ---->| mango | None |
             +-------+------+
    '''

    llist.removeNode("grape")
    llist.removeNode("orange")
    llist.printList()
    ''' 
            llist.head               second                
                |                      |                      
                |                      |                       
            +---------+------+     +--------+------+       +------------+------+     +-------+------+
            | apple   |  o-------->| banana |  o---------->| strawberry |  o-------->| mango | None |
            +---------+------+     +--------+------+       +------------+------+     +-------+------+
    '''