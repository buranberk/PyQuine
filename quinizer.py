
with open("quine_code.py", "r") as f:
    code = f.read()

processed =code
processed = processed.replace("\\", "\\\\")
processed = processed.replace('\"', '\\"')
processed = processed.replace("\'", "\\'")
processed = processed.replace("\t", "\\t")
processed = processed.replace("\r", "\\r")
processed = processed.replace("\n", "\\n")


code = code.replace("¬", processed)

with open("quine.py", "w") as f:
    f.write(code)