q="¬"
for c in q:
    if ord(c)==172:
        processed = q
        processed = processed.replace("\\", "\\\\")
        processed = processed.replace('\"', '\\"')
        processed = processed.replace("\'", "\\'")
        processed = processed.replace("\t", "\\t")
        processed = processed.replace("\r", "\\r")
        processed = processed.replace("\n", "\\n")
        print(processed, end="")
    else:
        print(c, end="")
import sys

class dummy:
    def write(self, text): pass
    def flush(self): pass
    
# redirect stdout to dummy class so that print does not print anything and break the quine
sys.stdout = dummy()
sys.__stdout__ = sys.stdout

# Paste Here