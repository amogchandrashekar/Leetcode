class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = list()
        self.pop_stack = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.push_stack:
            return self.push_stack[0]
        else:
            return self.pop_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.push_stack and not self.pop_stack


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    q.push(5)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()