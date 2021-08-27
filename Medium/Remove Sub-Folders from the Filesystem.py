from typing import List


class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_folder(self, folders):
        curr = self
        folders = folders.strip('/').split('/')
        for folder in folders:
            if folder not in curr.children:
                curr.children[folder] = Trie()
            curr = curr.children[folder]
            if curr.is_end:
                break

        curr.children = {}
        curr.is_end = True

    def get_root_folders(self):
        root_folders = list()

        def dfs(node, path):
            if node.is_end:
                nonlocal root_folders
                root_folders.append('/' + '/'.join(path))

            for children in node.children:
                dfs(node.children[children], path + [children])

        dfs(self, [])
        return root_folders


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for f in folder:
            trie.add_folder(f)

        return trie.get_root_folders()


if __name__ == '__main__':
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
    print(Solution().removeSubfolders(folder))