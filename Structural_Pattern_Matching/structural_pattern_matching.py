def respond(language):
    match language:
        case "Java":
            return "Hmm, coffee!"
        case "Python":
            return "I'm not scared of snakes!"
        case "Rust":
            return "Don't drink too much water!"
        case "Go":
            return "Collect $200"
        case _:
            return "I'm sorry..."


print(respond("Go"))

def respond(language):
    match language:
        case "Java" | "Javascript":
            return "Love those braces!"
        case "Python":
            return "I'm a lumberjack and I don't need no braces"
        case _:
            return "I have no clue!"

print(respond("Java"))



symbols = {
    "F": "\u2192", 
    "B": "\u2190", 
    "L": "\u2191", 
    "R": "\u2193", 
    "pick": "\u2923", 
    "drop": "\u2925"
}

def op(command):
    match command:
        case "move F":
            return symbols["F"]
        case "move B":
            return symbols["B"]
        case "move L":
            return symbols["L"]
        case "move R":
            return symbols["R"]
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")

print(op("move L"))
l=[
    op("move F"),
    op("move F"),
    op("move L"),
    op("pick"),
    op("move R"),
    op("move L"),
    op("move F"),
    op("drop"),
]

print(l)

def op(command):
    match command:
        case ["move", ("F" | "B" | "L" |"R") as direction]:
            return symbols[direction]
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")

print(op(["move", "L"]))


def op(command):
    match command:
        case ['move', *directions]:
            return tuple(symbols[direction] for direction in directions)
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")

l2=[
    op(["move", "F", "F", "L"]),
    op("pick"),
    op(["move", "R", "L", "F"]),
    op("drop"),
]
print(l2)
