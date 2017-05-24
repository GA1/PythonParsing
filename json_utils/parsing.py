


def add_apostrophes_and_comas(s):
    split = [s.strip() for s in s.split("\n")]
    for i in range(len(split) - 1):
        print("\"" + split[i] + "\"," )
    print("\"" + split[len(split) - 1] + "\"")


with open('input.txt') as f:
    data = f.read().replace('\n', ' ')
    joint = '\n'.join(data.split())
    add_apostrophes_and_comas(joint)
