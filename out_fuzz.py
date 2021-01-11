import termcolor

def coloredprint(text,color):
    if color == 1:
        termcolor.cprint(text,color='red')
    if color == 2:
        termcolor.cprint(text,color='green')
    else:
        print("colored print function: color argument", color, "is not a viable argument, specify 1 or 0")
        raise RuntimeError


coloredprint("red", 1)
