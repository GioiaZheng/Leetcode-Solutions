from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        back_online_time = [-1] * numberOfUsers

        def priority(e):
            return 0 if e[0] == "OFFLINE" else 1

        events.sort(key=lambda e: (int(e[1]), priority(e)))

        for event_type, time_str, data in events:
            t = int(time_str)

            # bring users back online BEFORE processing event
            for u in range(numberOfUsers):
                if not online[u] and back_online_time[u] <= t:
                    online[u] = True
                    back_online_time[u] = -1

            if event_type == "OFFLINE":
                u = int(data)
                online[u] = False
                back_online_time[u] = t + 60

            else:  # MESSAGE
                if data == "ALL":
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif data == "HERE":
                    for u in range(numberOfUsers):
                        if online[u]:
                            mentions[u] += 1
                else:
                    for token in data.split():
                        u = int(token[2:])
                        mentions[u] += 1

        return mentions
