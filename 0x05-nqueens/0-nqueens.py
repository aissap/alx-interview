#!/usr/bin/python3
"""N Queens problem solver.
"""
import sys


def validate_input():
    """Validates and get the size of the board.
    
    Returns:
            The size of the board.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_conflict(pose1, pose2):
    """Check if two queens are in attacking positions.
    
    Args:
        pose1 : Position of the first queen.
        pose2 : Position of the second queen.
        
    Returns:
        bool: True if the queens are attacking each other, False otherwise.
    """
    return (pose1[0] == pose2[0] or
            pose1[1] == pose2[1] or
            abs(pose1[0] - pose2[0]) == abs(pose1[1] - pose2[1]))


def exists_in_solutions(solutions, candidate):
    """Check if the solution exists in the list of solutions.
    
    Args:
        solutions: List of existing solutions.
        candidate: Candidate solution.
        
    Returns:
        bool: True if the candidate solution exists, False otherwise.
    """
    for solution in solutions:
        if all(pose in solution for pose in candidate):
            return True
    return False


def find_solutions(n, current_row, positions, solutions):
    """Recursively finds all solutions to the N Queens problem.
    
    Args:
        n : Size of the chessboard.
        current_row: Current row to place a queen.
        poseitions: poseitions of placed queens.
        solutions: Collected solutions.
    """
    if current_row == n:
        if not exists_in_solutions(solutions, positions):
            solutions.append(positions.copy())
        return
    
    for col in range(n):
        pose = (current_row, col)
        if not any(is_conflict(pose, placed_pose) for placed_pose in positions):
            positions.append(pose)
            find_solutions(n, current_row + 1, positions, solutions)
            positions.pop()


def solve_n_queens(n):
    """Solves the N Queens problem and prints all solutions.
    
    Args:
        n : Size of the chessboard.
    """
    solutions = []
    find_solutions(n, 0, [], solutions)
    for solution in solutions:
        print([[row, col] for row, col in solution])


if __name__ == "__main__":
    n = validate_input()
    solve_n_queens(n)
