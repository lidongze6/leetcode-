class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        dict1 = {emp.id: [emp.importance, emp.subordinates] for emp in employees}

        def dfs(id):
            if id not in dict1:
                return 0
            else:
                score, em = dict1[id][0], dict1[id][1]
                for e in em:
                    score += dfs(e)
            return score

        return dfs(id)
