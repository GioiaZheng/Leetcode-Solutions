from typing import List
from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # People who know the secret
        know = set([0, firstPerson])

        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])

        i = 0
        m = len(meetings)

        while i < m:
            time = meetings[i][2]

            # Collect all meetings at the same time
            graph = defaultdict(list)
            people = set()

            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            # BFS inside this time block
            queue = []

            for p in people:
                if p in know:
                    queue.append(p)

            visited = set(queue)

            while queue:
                cur = queue.pop()
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            # Everyone reached in this block learns the secret
            for p in visited:
                know.add(p)

        return list(know)
