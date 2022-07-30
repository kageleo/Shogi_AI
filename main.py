from command import usi, setoption, position, go

while True:
    cmd = input().split()

    # 思考エンジンの起動時、GUIから最初に受け取るコマンド（id:必須、option:任意）。エンジンの初期設定を行う。最後に usiok を返す。
    if cmd[0] == "usi":
        usi.usi()

    # 対局開始前に送る。対局準備完了後 readyok を返す。
    elif cmd[0] == "isready":
        print("readyok")

    # GUIから思考エンジンの設定を受け取る。
    elif cmd[0] == "setoption":
        setoption.setoption(cmd[2],cmd[4:])

    # 対局開始時に送る。
    elif cmd[0] == "usinewgame":
        pass

    # 思考開始局面をGUIから受け取る。
    elif cmd[0] == "position":
        position.position(cmd[1:])

    # 思考開始の合図
    elif cmd[0] == "go":    
        go.go(cmd[1:])

    # 思考エンジンの予想手が外れた場合にGUIから送られるコマンド。
    elif cmd[0] == "stop":
        pass

    # 思考エンジンの予想手が当たった場合にGUIから送られるコマンド。
    elif cmd[0] == "ponderhit":
        pass

    # 思考エンジンの終了を命令するコマンド
    elif cmd[0] == "quit":
        break

    # 対局状態を終了して、対局待ち状態になる。isready および usinewgame の受信で次の対局開始になる。
    elif cmd[0] == "gameover":
        pass

    # 対応していないコマンドの確認用
    else:
        print(f'invalid command: {" ".join(cmd)}')

