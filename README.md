# pypromanager

create your own project with python and this project manager for python

# quick start

copy the build.py to your project folder and create this tree of directory:
```dir
project/
-- build.py
-- buildfs.json
-- src/
---- main.py (optional)
-- build/ (auto added)
-- dist/ (auto added)
```

and run:
```console
$ python3 build.py build python
```

to clear use:
```console
$ python3 build.py clear
```

## buildfs.json

inside pbuildfs.json you can use for example:
```json
[
    "main.py"
]
```
it will interpret like this:
```json
[
    "src/main.py"
]
```

if you add `src/main.py` it will interpret like `src/src/main.py`<br>
remember: pbuildfs.json is for build python files only!<br>
remember: cbuildfs.json is for build c or c++ files only"<br>

how to use cbuildfs.json like this for example:
```json
{
    "main.c": "outname"
}
```

and compile with:
```console
$ python3 build.py build c
```

you can use C++ files too!
## libs

you need to install pyinstaller and add it to your path!

## note

you can remove all the content of this README.md and copy this repo to use an pre-made structure!<br>
the .gitignore already have some things to help your project!