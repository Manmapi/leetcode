class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d_parents = [[] for _ in range(numCourses)]
        for parent, child in prerequisites:
            d_parents[child].append(parent)
        
        result = 0

        def find_parent(index):
            q = [index]
            visited = set(q)
            while q:
                q_new = []
                for parent in q:
                    for super_parent in d_parents[parent]:
                        if super_parent not in visited:
                            visited.add(super_parent)
                            q_new.append(super_parent)
                q = q_new
            return visited
        parents = [
            find_parent(i)
            for i in range(numCourses)
        ]
        return [
            parent in parents[child]
            for parent, child in queries
        ]