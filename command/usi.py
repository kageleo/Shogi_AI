import json

with open("./config.json") as f:
    jsn = json.load(f)


def usi():
        print(f'id name {jsn["id"]["ENGINE_NAME"]}')
        print(f'id author {jsn["id"]["ENGINE_AUTHOR"]}')

        for name, option in jsn["option"].items():
            print(f'option name {name} type {option["type"]} default {option["value"]}')

        print("usiok")

