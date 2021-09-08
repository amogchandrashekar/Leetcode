import heapq


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        # write your code here
        rows = len(maze)
        cols = len(maze[0]) if rows else 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        start_rid, start_cid = start
        dest_rid, dest_cid = destination

        dist = [[float('inf')] * cols for row in range(rows)]
        dist[start_rid][start_cid] = 0

        priority_queue = [[0, start_rid, start_cid]]

        while priority_queue:
            cur_dist, rid, cid = heapq.heappop(priority_queue)

            if rid == dest_rid and cid == dest_cid:
                return cur_dist

            if cur_dist > dist[rid][cid]:
                continue

            for dx, dy in directions:
                dr, dc = rid + dx, cid + dy
                dist_to_wall = 0

                if dr not in range(rows) or dc not in range(cols):
                    continue

                while dr in range(rows) and dc in range(cols) and maze[dr][dc] != 1:
                    dr += dx
                    dc += dy
                    dist_to_wall += 1

                dr -= dx
                dc -= dy

                updated_dist = cur_dist + dist_to_wall
                if updated_dist < dist[dr][dc]:
                    dist[dr][dc] = updated_dist
                    heapq.heappush(priority_queue, [updated_dist, dr, dc])

        return dist[dest_rid][dest_cid] if dist[dest_rid][dest_cid] != float('inf') else -1


if __name__ == '__main__':
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]

    start = [0, 4]
    end = [4, 4]
    print(Solution().shortestDistance(maze, start, end))