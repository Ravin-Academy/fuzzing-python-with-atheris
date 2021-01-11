import atheris
import sys

def TestOneInput(data):
  if data == b"badbadbadbadbad123":
    print(data)
    raise RuntimeError("Badness!")

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
