class MyQueue:

    def __init__(self):
        self.my_list = []

    def push(self, x: int) -> None:
        self.my_list.append(x)

    def pop(self) -> int:
        return self.my_list.pop(0)

    def peek(self) -> int:
        return self.my_list[0]

    def empty(self) -> bool:
        return False if self.my_list else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()