from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        know = {0, firstPerson}
        meetings.sort(key=lambda meeting: meeting[2])

        i, m = 0, len(meetings)
        while i < m:
            time = meetings[i][2]

            # Build the meeting graph for this single timestamp.
            graph: dict[int, list[int]] = defaultdict(list)
            people: set[int] = set()
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            # BFS from every already-knowing person in this block. Anyone
            # reachable through same-time meetings learns the secret too.
            queue = deque(p for p in people if p in know)
            while queue:
                cur = queue.popleft()
                for nei in graph[cur]:
                    if nei not in know:
                        know.add(nei)
                        queue.append(nei)

        return list(know)
