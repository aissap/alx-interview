#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False

    num_boxes = len(boxes)
    if num_boxes == 0:
        return False

    visited_boxes = set([0])
    box_queue = [0]

    while box_queue:
        current_box = box_queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and key not in visited_boxes:
                visited_boxes.add(key)
                box_queue.append(key)

    return len(visited_boxes) == num_boxes
