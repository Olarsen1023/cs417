"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    """A priority-based task scheduler.

    Tasks are added with a priority (lower number = more urgent).
    Tasks with the same priority are processed in FIFO order.
    """

    def __init__(self):
        """Initialize the scheduler."""
        self._heap = []
        self._counter = 0


    def add_task(self, priority, description):
        """Add a task to the scheduler.

        Args:
            priority: An integer priority (lower = more urgent).
            description: A string describing the task.
        """
        heapq.heappush(self._heap, (priority, self._counter, description))
        self._counter += 1

    def next_task(self):
        """Remove and return the highest-priority task's description.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Pop from the heap, return the description
        if not self._heap:
            return None
        _, _, description = heapq.heappop(self._heap)
        return description

    def peek(self):
        """Return the highest-priority task's description without removing it.

        Returns:
            The description string, or None if empty.
        """
        # TODO: Look at h[0] without popping
        if not self._heap:
            return None
        _, _, description = self._heap[0]
        return description

    def __len__(self):
        """Return the number of pending tasks."""
        # TODO: Return the length of the heap
        return len(self._heap)

    def is_empty(self):
        """Return True if there are no pending tasks."""
        # TODO
        return len(self._heap) == 0
