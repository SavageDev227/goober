import base64

e = "Z29v"
y = "YmVy"
b = "ISEhISE="

goober = str(base64.b64decode(bytes(e + y + b)))

goober_goob = base64.b64encode(bytes(goober))
print(str(goober_goob))
