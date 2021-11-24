
# O(1) time and space complexity.
# It will always take the same number
# of moves and the same recursion depth
# to solve this puzzle.
# This code assumes we will always start
# with 3 rods and 3 disks.
def towers_of_hanoi(disks):
    return get_moves(disks, 0, 2, 1)

def get_moves(disk, src, dest, aux):
    # If we moved all the other disks,
    # just put the last disk in the right place.
    if disk == 1:
        return [Move(disk, src, dest)]

    # Move all the other disks from src to aux.
    moves = []
    moves += get_moves(disk - 1, src, aux, dest)
    # Move this disk to the destination.
    moves += [Move(disk, src, dest)]
    # Move the remaining disks from aux back to src.
    moves += get_moves(disk - 1, aux, dest, src)
    return moves

class Move:

    def __init__(self, disk, src, dest):
        self.disk = disk
        self.src = src
        self.dest = dest

    def __repr__(self):
        return "Move disk {} from {} to {}.".format(self.disk, self.src, self.dest)

print(towers_of_hanoi(3))