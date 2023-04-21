class Queue:
    def __init__(self):
        self.queue = list()

    # Thêm phần tử mới bằng insert()
    def add_to_queue(self, value):  # FI (First In)
        if value not in self.queue:
            # Dùng insert(0, giá trị) để đưa giá trị mới vào đầu list. Đẩy giá trị thêm vào trước đi lên
            # VD: Cho list = [2, 3, 4]. insert(0, 1) sẽ cho ra list = [1, 2, 3, 4]
            self.queue.insert(0, value)
        else:
            print("Gia tri da nam trong queue")

    # Kích thước của queue
    def size(self):
        return len(self.queue)

    # Loại bỏ phần tử ở queue
    # Hàm pop() bỏ phần tử ở cuối list
    def remove(self):  # FO (First Out)
        if len(self.queue) > 0:
            self.queue.pop()
        else:
            return "Queue không có phần tử nào"


test_queue = Queue()
test_queue.add_to_queue("Mon")
test_queue.add_to_queue("Tue")
test_queue.add_to_queue("Wed")
print(test_queue.queue)
print(test_queue.size())

test_queue.remove()
print(test_queue.queue)
print(test_queue.size())

