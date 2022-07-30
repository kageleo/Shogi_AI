
startposition = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"
moves = []
turn = "b"

def position(sfen):

    global startposition
    global moves
    global trun

    if sfen[0] == "startpos":
        moves = sfen[2:]
        if len(moves) % 2 == 0:
            trun = "b"
        else:
            trun = "w"
    else:
        startposition = sfen[1]
        trun = sfen[2]
        moves = sfen[6:]