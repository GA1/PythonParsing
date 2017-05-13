import re


def addApoAndComa(s):
    splitted = s.split("\n")
    for i in range(len(splitted) - 1):
        splitted[i] = p.match(splitted[i])
        print("\"" + splitted[i] + "\"," )
    print("\"" + splitted[len(splitted) - 1] + "\"")

addApoAndComa("bell")