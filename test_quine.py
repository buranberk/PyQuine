import os

# run the quine and save output to file
os.system("python quine.py > temp.py")

with open("quine.py","r") as f:
    quine=f.read()

with open("temp.py","r") as f:
    quine_test=f.read()

if len(quine)!=len(quine_test):
    print("not a quine")
    quit()

for i in range(0,len(quine_test)):
    if quine[i]!=quine_test[i]:
        print("not a quine")
        os.remove("temp.py")
        quit()

print("is a quine")
os.remove("temp.py")
