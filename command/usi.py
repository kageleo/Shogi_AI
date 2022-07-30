import json

with open("./config.json") as f:
    jsn = json.load(f)


def usi():
        print(f'id name {jsn["id"]["ENGINE_NAME"]}')
        print(f'id author {jsn["id"]["ENGINE_AUTHOR"]}')

        for key in jsn["option"]:
            print(f'option {jsn["option"][key]}')

        print("usiok")

