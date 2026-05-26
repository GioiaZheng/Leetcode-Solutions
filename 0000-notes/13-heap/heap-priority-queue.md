# Heap / Priority Queue

## Pattern description

A heap keeps the next smallest (or largest) item available in `O(log n)` per update. In Python, `heapq` is a min-heap; use negative values or tuples for max-heap behavior and tie-breaking.

## When to use it

Use a heap when the problem repeatedly asks for:

- the next earliest ending time
- the current smallest/largest candidate
- top `k` items
- scheduling with rooms, machines, or delayed work
- merging or processing events in priority order

If you only sort once, a heap may be unnecessary. If priorities change over time, a heap is often the right tool.

## Template code

```python
import heapq

heap = []
for item in items:
    heapq.heappush(heap, (priority(item), item))

while heap:
    prio, item = heapq.heappop(heap)
    # process smallest priority first
```

Max-heap pattern:

```python
heapq.heappush(heap, (-score, value))
score, value = heapq.heappop(heap)
score = -score
```

Two-heap scheduling pattern:

```python
available = list(range(n))          # room ids
busy = []                           # (end_time, room_id)
heapq.heapify(available)

for start, end in meetings:
    while busy and busy[0][0] <= start:
        _, room = heapq.heappop(busy)
        heapq.heappush(available, room)

    if available:
        room = heapq.heappop(available)
        heapq.heappush(busy, (end, room))
    else:
        finish, room = heapq.heappop(busy)
        heapq.heappush(busy, (finish + end - start, room))
```

## Common pitfalls

- Forgetting Python heaps are min-heaps.
- Putting unorderable objects in tuple positions used for tie-breaking.
- Forgetting to pop expired entries before reading the heap top.
- Using a heap when simple sorting or `Counter.most_common()` is clearer.
- Not tracking counts separately when the heap only stores priorities.

## Linked solved problems

- [`2402-meeting-rooms-iii`](../../problems/2402-meeting-rooms-iii/) â€” two heaps for available and busy rooms.
- [`0692-top-k-frequent-words`](../../problems/0692-top-k-frequent-words/) â€” frequency ranking / top-k thinking.
- [`2343-query-kth-smallest-trimmed-number`](../../problems/2343-query-kth-smallest-trimmed-number/) â€” repeated ordering queries.
- [`0347-top-k-frequent-elements`](../../problems/0347-top-k-frequent-elements/) â€” compare heap, sorting, bucket, and counter approaches.
