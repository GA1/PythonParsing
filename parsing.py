
def add_apostrophes_and_comas(s):
    split = [s.strip() for s in s.split("\n")]
    for i in range(len(split) - 1):
        print("\"" + split[i] + "\"," )
    print("\"" + split[len(split) - 1] + "\"")

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

add_apostrophes_and_comas(s)
