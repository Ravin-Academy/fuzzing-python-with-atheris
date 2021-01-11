
# https://stackoverflow.com/a/20170614
import atheris
import termcolor
import sys
import struct

def ok(text, color):
    if color == 1:
        termcolor.cprint(text,color='red')
    if color == 2:
        termcolor.cprint(text,color='green')
    else:
        print("colored print function: color argument", color, "is not a viable argument, specify 1 or 0")
        #raise RuntimeError

def TestOneInput(data):
	if data:
		mydata = data
		fdp = atheris.FuzzedDataProvider(data)
		yourclolor = fdp.ConsumeUnicode(sys.maxsize)
		print(data)

		ok(mydata, yourclolor)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
