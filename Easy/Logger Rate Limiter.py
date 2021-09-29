from collections import deque


class Logger:

    def __init__(self):
        self.queue = deque()
        self.seen = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        while self.queue and self.queue[0][0] <= timestamp:
            elem = self.queue.popleft()
            self.seen.remove(elem[1])

        if message not in self.seen:
            self.queue.append([timestamp + 10, message])
            self.seen.add(message)
            return True
        else:
            return False