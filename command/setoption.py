import json

with open("./config.json") as f:
    settings = json.load(f)


def setoption(name, value):
    if name in settings["option"]:    
        settings["option"][name]["value"] = " ".join(value)
    else:
        print(f'Not Found :  "{name}"')
    
