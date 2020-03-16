def groupAnagrams(strs):
    from collections import defaultdict
    lookup = defaultdict(list)
    for s in strs:
        lookup["".join(sorted(s))].append(s)
    return list(lookup.values())



strs= ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))




