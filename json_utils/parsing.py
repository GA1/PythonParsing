import re


def add_apostrophes_and_comas(s):
    split = [s.strip() for s in s.split("\n")]
    print("{")
    print("\"words\":[" )
    for i in range(len(split) - 1):
        print("\"" + split[i] + "\"," )
    print("\"" + split[len(split) - 1] + "\"")
    print("]," )
    print("\"words_translation\":[" )
    for i in range(len(split) - 1):
    	print("\"\"," )
    print("\"\"")
    print("]," )
    print("\"translation\":\"\"" )
    print("}")

with open('input.txt') as f:
    data = f.read().replace('\n', ' ')
    sentences = re.compile('[\.\!\?]').split(data)
    for sentence in sentences:
    	joint = '\n'.join(sentence.split())
    	add_apostrophes_and_comas(joint)
