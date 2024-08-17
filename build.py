# install pyinstaller python library!
import json
import os
import sys

def build():
    with open("pbuildfs.json", "r") as fs:
        files = json.load(fs)
    for fi in files:
        os.system("pyinstaller --onefile {}".format("src/" + fi))

def buildc(compname):
    with open("cbuildfs.json", "r") as fs:
        files = json.load(fs)
    os.system("mkdir -p build/")
    for fi in files.keys():
        if compname.lower() == "c":
            os.system("gcc " + "src/" + fi + " -o ./build/" + files[fi])
        elif compname.lower() == "c++":
            os.system("g++ " + "src/" +fi + " -o ./build/" + files[fi])
        elif compname.lower() == "cc":
            os.system("cc " + "src/" + fi + " -o ./build/" + files[fi])
        else:
            print("Error: unknown compile type: '{}' use 'c', 'c++' or 'cc'")

def handlebuild(compname):
    name = compname.lower()
    if name == "python":
        build()
    else:
        buildc(name)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "build":
            if len(sys.argv) > 2:
                handlebuild(sys.argv[2])
            else:
                print("Build usage: build.py build [python|c|c++|cc]")
        elif sys.argv[1] == "clear":
            os.system("rm -rf build/ dist/ *.spec")
        elif sys.argv[1] == "run":
            if len(sys.argv) > 4:
                os.system(sys.argv[2] + " " + sys.argv[3])
            else:
                print("Run usage: build.py run [python|python3|node|etc] <file>")
                print("Yes, you can use other things, but this will only work with 'run'")
    else:
        print("Usage: build.py [build|clear|run]")
        exit(1)