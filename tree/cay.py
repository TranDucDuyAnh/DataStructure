# Cây cơ bản (Generic Tree) là tập hợp các nút liên kết với nhau theo quan hệ cha-con.
# Ta tạo đối tượng Node với 2 thuộc tính: giá trị của Node đó và các Node con của nó

class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, child):
        self.children.append(child)


# Hàm thêm node
def add_node(value):
    temp = Node(value)
    return temp
