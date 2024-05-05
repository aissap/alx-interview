#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes: A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    num_boxes = len(boxes)
    visited = set()
    visited.add(0)  # Start with the first box
    box_queue = [0]  # Queue for BFS traversal

    while box_queue:
        current_box = box_queue.pop(0)
        for key in boxes[current_box]:
            if key < num_boxes and key not in visited:
                visited.add(key)
                box_queue.append(key)

    return len(visited) == num_boxes
