#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened."""
  num_boxes = len(boxes)
  visited = set()
  visited.add(0)
  box_queue = [0]

  while box_queue:
      current_box = box_queue.pop(0)
      for key in boxes[current_box]:
          if key < num_boxes and key not in visited:
              visited.add(key)
              box_queue.append(key)

  return len(visited) == num_boxes
