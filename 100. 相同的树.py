class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def arraytotree(self, nums, l, i):
        if i > l:
            return
        root = TreeNode(None)
        root.val = nums[i]
        root.left = self.arraytotree(nums, l, i * 2 + 1)
        root.right = self.arraytotree(nums, l, i * 2 + 2)
        return root

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        if l and r and p.val == q.val:
            return True
        else:
            return False


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 4, 1]
    r = Solution()
    root1 = r.arraytotree(arr, len(arr) - 1, 0)
    root2 = r.arraytotree(arr2, len(arr) - 1, 0)
    print(r.isSameTree(root1,root2))
