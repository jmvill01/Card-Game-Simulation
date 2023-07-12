import random

def call_play(val: int) -> str:

    if val <= 7:
        return "Greater"

    if val == 8:
        rand = random.randrange(0, 2)
        if rand == 1:
            return "Lesser"
        else:
            return "Greater"
        
    if val >= 9:
        return "Lesser"