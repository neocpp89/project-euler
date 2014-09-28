#!/usr/bin/env python

def prize_strings_in_branch(maxd, d=0, prefix_has_late=False, consecutive_absent_count=0):
    if d == maxd:
        return 1
    c = 0
    # mark late
    if not prefix_has_late:
        c += prize_strings_in_branch(maxd, d+1, True, 0)
    # mark absent
    if consecutive_absent_count < 2:
        c += prize_strings_in_branch(maxd, d+1, prefix_has_late, consecutive_absent_count+1)
    # mark on-time
    c += prize_strings_in_branch(maxd, d+1, prefix_has_late, 0)
    return c

print prize_strings_in_branch(30)
