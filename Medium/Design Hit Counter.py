from bisect import bisect_right


class HitCounter:

    def __init__(self):
        self.queue = list()

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        idx = bisect_right(self.queue, timestamp - 300)
        self.queue = self.queue[idx:]
        return len(self.queue)


if __name__ == '__main__':
    hitCounter = HitCounter()
    hitCounter.hit(1)
    hitCounter.hit(2)
    hitCounter.hit(3)
    print(hitCounter.getHits(4))
    hitCounter.hit(300)
    print(hitCounter.getHits(300))
    hitCounter.getHits(301)