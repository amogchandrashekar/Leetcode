from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        all_paths = defaultdict(list)

        for path in paths:
            path = path.split()
            root_dir, files = path[0], path[1:]

            for file in files:
                file = file.strip(')')
                file_name, content = file.split('(')
                all_paths[content].append(f'{root_dir}/{file_name}')

        return [duplicate_text for content, duplicate_text in all_paths.items() if len(duplicate_text) > 1]


if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
    print(Solution().findDuplicate(paths))

