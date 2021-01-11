import atheris
import sys

from django.utils.http import urlsafe_base64_encode

def TestOneInput(data):
	if data:
		#print(data)
		print(urlsafe_base64_encode(data))

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
