def addApoAndComa(s):
    splitted = s.split("\n")
    for i in range(len(splitted) - 1):
        print("\"" + splitted[i].strip() + "\"," )
    print("\"" + splitted[len(splitted) - 1].strip() + "\"")

s = """          bell
          Sigismund [name]
          until
          recently
          to be
          the biggest
          in
          Poland
          until
          in 
          year
          1999
          to create/to make
          still/even
          bigger
          bell
          which 
          to be called
          bell
          Marie
          Mother of God"""

addApoAndComa(s)