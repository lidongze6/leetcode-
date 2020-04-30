# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findMountaintop(mountain_arr: 'MountainArray'):
            l, r = 0, mountain_arr.length() - 1
            while l < r:
                mid = l + (r - l) // 2
                if mountain_arr.get(mid) >= mountain_arr.get(mid + 1):
                    r = mid
                else:
                    l = mid + 1
            if l >= r:
                return l

        def findMountaintarger(target, l, r, mountain_arr: 'MountainArray', revers: bool):
            while l + 1 < r:
                mid = l + (r - l) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) > target:
                    if revers:
                        l = mid + 1
                    else:
                        r = mid - 1
                elif mountain_arr.get(mid) < target:
                    if revers:
                        r = mid - 1
                    else:
                        l = mid + 1
            if mountain_arr.get(l) == target:
                return l
            elif mountain_arr.get(r) == target:
                return r
            else:
                return -1

        l, r = 0, mountain_arr.length() - 1
        mt = findMountaintop(mountain_arr)
        if mountain_arr.get(mt) == target: return mt
        lres = findMountaintarger(target, l, mt - 1, mountain_arr, False)
        if lres != -1: return lres
        rres = findMountaintarger(target, mt + 1, r, mountain_arr, True)
        if rres != -1: return rres
        return -1


