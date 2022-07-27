import json

with open("./config.json", "r") as f:
    jsn = json.load(f)


while True:
    cmd = input().split()

    if cmd[0] == "usi":
        print(f'id name {jsn["ENGINE_NAME"]}')
        print(f'id author {jsn["ENGINE_AUTHOR"]}')
        print("usiok")

    elif cmd[0] == "isready":
        print("readyok")

    elif cmd[0] == "setoption":
        pass

    elif cmd[0] == "usinewgame":
        pass

    elif cmd[0] == "position":
        pass

    elif cmd[0] == "go":
        # 即時投了
        print("bestmove resign")

    elif cmd[0] == "stop":
        pass

    elif cmd[0] == "ponderhit":
        pass

    elif cmd[0] == "quit":
        break

    elif cmd[0] == "gameover":
        pass

    else:
        print(f'invalid command: {" ".join(cmd)}')

