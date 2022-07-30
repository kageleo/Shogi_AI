
startposition = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL"
moves = []
turn = "b"
Bpieces = []
Wpieces = []

def position(sfen):

    global startposition
    global moves
    global trun
    global Bpieces
    global Wpieces

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
        Bpieces = []
        Wpieces = []
        pieces = sfen[3]
        p = ""
        for piece in pieces:
            p += piece
            if piece.isupper():
                Bpieces.append(p)
                p = ""
            elif piece.islower():
                Wpieces.append(p)
                p = ""

