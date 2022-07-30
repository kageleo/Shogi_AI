from command import usi

while True:
    cmd = input().split()

    # 思考エンジンの起動時、最初に送るコマンド（id:必須、option:任意）。最後に usiok を返す。
    if cmd[0] == "usi":
        usi.usi()

    # 対局開始前に送る。対局準備完了後 readyok を返す。
    elif cmd[0] == "isready":
        print("readyok")

    # 思考エンジンに対して設定をする時に送る。
    elif cmd[0] == "setoption":
        pass

    # 対局開始時に送る。
    elif cmd[0] == "usinewgame":
        pass

    # 思考開始局面をエンジンに知らせるためのコマンド
    elif cmd[0] == "position":
        pass

    # 思考開始の合図
    elif cmd[0] == "go":
        # 即時投了
        print("bestmove resign")

    # エンジンに対し思考停止を命令するコマンド
    elif cmd[0] == "stop":
        pass

    # 思考エンジンが先読み中、前回のbestmoveコマンドでエンジンが予想した手を相手が指した時に送る。
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

