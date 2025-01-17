class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def toposort(n: int, vertexs: List[List[int]]): 
            indegree = [0] * n
            m = defaultdict(list)
            for parent, child in vertexs:
                indegree[child] += 1
                m[parent].append(child)
            source = []
            for i in range(n):
                if indegree[i] == 0:
                    source.append(i)
            result = []
            while source:
                point = source.pop()
                result.append(point)
                for next_point in m[point]:
                    indegree[next_point] -= 1
                    if indegree[next_point] == 0:
                        source.append(next_point)
            return result
        return len(toposort(numCourses, prerequisites)) == numCourses
        