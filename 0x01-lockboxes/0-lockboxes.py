#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes: A list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False

    num_boxes = len(boxes)
    if num_boxes == 0:
        return False

    visited_boxes = set([0])
    unvisited_boxes = set(boxes[0]).difference(set([0]))

    while unvisited_boxes:
        current_box = unvisited_boxes.pop()
        if not 0 <= current_box < num_boxes:
            continue
        visited_boxes.add(current_box)
        unvisited_boxes = unvisited_boxes.union(set(boxes[current_box]).difference(visited_boxes))

    return len(visited_boxes) == num_boxes
