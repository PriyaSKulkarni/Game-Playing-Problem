# Name: Priya Kulkarni
# StudentID: 1002088875

# Assess the existing condition of the game and furnish a numerical score corresponding to that state by using evalfunction.
def EvaFun(s): 
    red = s[0] * 2
    blue= s[1] * 3
    res = red-blue
    return res

# Minmax for misere version, prioritizing red moves over blue
def MinMaxmisere(s, d, a, b, max_player):
    if d == 0 or  s[1] == 0 or s[0] == 0:
        return EvaFun(s)
    if max_player:
        b_v = float('-inf') # initial best value
        b_m = -1 # initial best move
        # Generate possible moves, prioritizing red moves
        for i in [0, 1]:
            if s[i] > 0:
                n_s = list(s) # new state
                n_s[i] -= 1 
                val = MinMaxmisere(n_s, d - 1, a, b, False)
                if val > b_v:
                    b_v = val
                    b_m = i
                a = max(a, b_v)
                if b <= a:
                    break
        if b_m == 0:
            return b_v
        else:
            # Try blue moves if no red moves are available
            n_s = list(s)
            n_s[1] -= 1
            val = MinMaxmisere(n_s, d - 1, a, b, False)
            return max(b_v, val)
    else:
        b_v = float('inf')
        b_m = -1
        # Generate possible moves, prioritizing blue moves
        for i in [1, 0]:
            if s[i] > 0:
                n_s = list(s)
                n_s[i] -= 1
                val = MinMaxmisere(n_s, d - 1, a, b, True)
                if val < b_v:
                    b_v = val
                    b_m = i
                b = min(b, b_v)
                if b <= a:
                    break
        if b_m == 1:
            return b_v
        else:
            # Try red moves if no blue moves are available
            n_s = list(s)
            n_s[0] -= 1
            val = MinMaxmisere(n_s, d - 1, a, b, True)
            return min(b_v, val)

#red-blue nim in misere version
def RedBlueNim_misere(red, blue, f_p='computer', d=None):
    s = [red, blue]
    player = f_p
    while s[0] > 0 and s[1] > 0:
        print(f"Red: {s[0]} Blue: {s[1]}")
        if player == 'human':
            while True:
                try:
                    r_move = int(input("Enter no. of red stones to be removed (0 or 1): "))
                    b_move = int(input("Enter no. of blue stones to be removed (0 or 1): "))
                    if r_move >= 0 and b_move >= 0 and r_move <=1 and b_move <=1 and r_move + b_move == 1  and r_move <= s[0] and b_move <= s[1]:
                        s[0] -= r_move
                        s[1] -= b_move
                        break
                    else:
                        print("Sum of blue + red stones removed should be equal to 1. Invalid move, try again.")
                except ValueError:
                    print("Invalid input, try again.")
            player = 'computer'
        else:
            b_v = float('-inf') # best value initialization
            b_m = -1 # best move initialization
            moves = []
            for i in [0, 1]:
                if s[i] > 0:
                    n_s= list(s)
                    n_s[i] -= 1
                    val = MinMaxmisere(n_s, d or 3, float('-inf'), float('inf'), False)
                    moves.append((i, val))
            # Sort moves in descending order of value
            moves.sort(key=lambda x: x[1], reverse=True)
            for m in moves:
                i, _ = m
                if i == 0:
                    b_m = 0
                    break
                else:
                    # Try blue moves only if no red moves are available
                    n_s = list(s)
                    n_s[1] -= 1
                    val= MinMaxmisere(n_s, d or 3, float('-inf'), float('inf'), False)
                    if val > b_v: 
                        b_v = val
                        b_m = 1
            s[b_m] -= 1
            print(f"Computer removes 1 {'red' if b_m == 0 else 'blue'} stone.")
            player = 'human'
    print(f"final state: Red: {s[0]} Blue: {s[1]}")
    print("Score:", s[0] * 2 + s[1] * 3)
    print(f"{player.capitalize()} wins!")

# Minmax for standard version, prioritizing blue moves over red
def MinMaxstandard(s, d, a, b, max_player):
    if d == 0 or s[0] == 0 or s[1] == 0:
        return EvaFun(s)
    if max_player:
        b_v = float('-inf') # best  value initialization
        b_m = -1 # best move initialization
        # Generate possible moves, prioritizing blue moves
        for i in [1, 0]:
            if s[i] > 0:
                n_s = list(s)
                n_s[i] -= 1
                val = MinMaxstandard(n_s, d - 1, a, b, False)
                if val > b_v:
                    b_v = val
                    b_m = i
                a = max(a, b_v)
                if b <= a:
                    break
        if b_m == 1:
            return b_v
        else:
            # Try red moves if no blue moves are available
            n_s = list(s)
            n_s[0] -= 1
            val = MinMaxstandard(n_s, d - 1, a, b, False)
            return max(b_v, val)
    else:
        b_v = float('inf') # best value
        b_m = -1 # best move
        # Generate possible moves, prioritizing red moves
        for i in [0, 1]:
            if s[i] > 0:
                n_s= list(s)
                n_s[i] -= 1
                val = MinMaxstandard(n_s, d - 1, a, b, True)
                if val < b_v:
                    b_v = val
                    b_m = i
                b = min(b, b_v)
                if b <= a:
                    break
        if b_m == 0:
            return b_v
        else:
            # Try blue moves if no red moves are available
            n_s = list(s)
            n_s[1] -= 1
            val = MinMaxstandard(n_s, d- 1, a, b, True)
            return min(b_v, val)

# red-blue nim in standard
def RedBlueNim_standard(red, blue, f_p='computer', d=None):
    s = [red, blue]
    player = f_p
    while s[0] > 0 and s[1] > 0:
        print(f"Red: {s[0]} Blue: {s[1]}")
        if player == 'human':
            while True:
                try:
                    r_move = int(input("Enter no. of red stones to be removed (0 or 1): "))
                    b_move = int(input("Enter no. of blue stones to be removed (0 or 1): "))
                    if r_move >= 0 and b_move >= 0 and r_move <=1 and b_move <=1 and r_move + b_move == 1 and r_move <= s[0] and b_move <= s[1]:
                        s[0] -= r_move
                        s[1] -= b_move
                        break
                    else:
                        print("Sum of blue + red stones removed should be equal to 1. Invalid move, try again.")
                except ValueError:
                    print("Invalid input, try again.")
            player = 'computer'
        else:
            b_v = float('-inf')# best value initialzation
            b_m = -1 # best move initialzation
            moves = []
            for i in [1, 0]:
                if s[i] > 0:
                    n_s = list(s)
                    n_s[i] -= 1
                    val = MinMaxstandard(n_s, d or 3, float('-inf'), float('inf'), False)
                    moves.append((i, val))
            # Sort moves in descending order of value
            moves.sort(key=lambda x: x[1], reverse=True)
            for m in moves:
                i, _ = m
                if i == 1:
                    b_m = 1
                    break
                else:
                    # Try red moves only if no blue moves are available
                    n_s = list(s)
                    n_s[0] -= 1
                    val = MinMaxstandard(n_s, d or 3, float('-inf'), float('inf'), False)
                    if val > b_v:
                        b_v = val
                        b_m = 0
            s[b_m] -= 1
            print(f"Computer removes 1 {'blue' if b_m == 1 else 'red'} stone(s).")
            player = 'human'
    print(f"final state: Red: {s[0]} Blue: {s[1]}")
    print("Score: -", s[0] * 2 + s[1] * 3)
    print(f"{player.capitalize()} loses!")

import sys
def main():
    red = int(sys.argv[1])
    blue = int(sys.argv[2])
    version = sys.argv[3]
    f_p = sys.argv[4] if len(sys.argv) > 4 else "computer" # first player
    d = int(sys.argv[5]) if len(sys.argv) > 5 else 6 # depth
    if(version == "misere"):
        RedBlueNim_misere(red, blue, f_p, d)
    if(version =="standard"):
        RedBlueNim_standard(red, blue, f_p, d)

main()
