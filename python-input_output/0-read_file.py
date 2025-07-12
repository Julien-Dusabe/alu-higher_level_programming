#!/usr/bin/paython3
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
