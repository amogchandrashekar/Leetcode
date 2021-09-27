class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0, 0]] for _ in range(length)]
        self.cur_snap = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.cur_snap:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.cur_snap, val])

    def snap(self) -> int:
        self.cur_snap += 1
        return self.cur_snap - 1

    def get(self, index: int, snap_id: int) -> int:
        sorted_arr = self.arr[index]
        left, right = 0, len(sorted_arr) - 1
        ans = None
        while left <= right:
            mid = (left + right) // 2
            old_snap_id, _ = sorted_arr[mid]

            if old_snap_id == snap_id:
                ans = mid
                break
            elif old_snap_id < snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return self.arr[index][ans][1]


if __name__ == '__main__':
    snapshotArr = SnapshotArray(3)
    snapshotArr.set(0,5)
    print(snapshotArr.snap())
    snapshotArr.set(0,6)
    print(snapshotArr.get(0,0))