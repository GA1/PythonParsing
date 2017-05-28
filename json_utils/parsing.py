import re


def add_apostrophes_and_comas(s):
    split = [s.strip() for s in s.split("\n")]
    json_sentence = ''
    json_sentence = json_sentence + "{\n"
    json_sentence = json_sentence + "\"words\":[\n"
    for i in range(len(split) - 1):
        json_sentence = json_sentence + "\"" + split[i] + "\",\n"
    json_sentence = json_sentence + "\"" + split[len(split) - 1] + "\"\n"
    json_sentence = json_sentence + "],\n"
    json_sentence = json_sentence + "\"words_translation\":[\n"
    for i in range(len(split) - 1):
        json_sentence = json_sentence + "\"\",\n"
    json_sentence = json_sentence + "\"\"\n"
    json_sentence = json_sentence + "],\n"
    json_sentence = json_sentence + "\"translation\":\"\"\n"
    json_sentence = json_sentence + "}\n"
    return json_sentence

with open('input.txt') as input_file:
    output = open('output.txt', 'w')
    data = input_file.read().replace('\n', ' ')
    sentences = re.compile('[.!\?]').split(data)
    json_sentences = []
    for sentence in sentences:
        joint = '\n'.join(sentence.split())
        json_sentence = add_apostrophes_and_comas(joint)
        json_sentences.append(json_sentence)
    output.write('[' + ','.join(json_sentences) + ']')
