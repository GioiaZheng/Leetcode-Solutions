from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by original start time
        meetings.sort()

        # Min-heap of available rooms (by room number)
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap of busy rooms: (end_time, room_number)
        busy = []

        # Count how many meetings each room holds
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free up rooms that have finished by 'start'
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign meeting immediately to the smallest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # No room available → delay meeting
                finish_time, room = heapq.heappop(busy)
                # Start when this room becomes free
                new_end = finish_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # Return the room with the maximum count (smallest index if tie)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
