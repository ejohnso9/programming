import sys
import math

# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def nextHurdle(track, current_pos: int) -> int:
    """
    how many steps forward until jump (i.e., one space in front of the hurdle space is 0
    """

    return track.index('#', current_pos + 1) - 1

    
player_no = int(input())
nb_games = int(input())  # always 1 for wood league

# game loop
while True:
    # ignoring 3 lines of score info...
    for i in range(3):
        score_info = input()

    for i in range(nb_games):
        ip = input().split()
        track = ip[0]  # print(track, file=sys.stderr)
        pos_l = [int(ip[i]) for i in [1, 2, 3]]
        stun_l = [int(ip[i]) for i in [4, 5, 6]]
        cur_pos = pos_l[player_no]
        print(f"mypos: {cur_pos}")
        # print(regs, file=sys.stderr)

    # Write an action using print
    n = nextHurdle(track, cur_pos)
    print(f"nextHurdle() is {n}")
    print("UP")

