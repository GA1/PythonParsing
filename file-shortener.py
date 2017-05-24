from_file_name = 'big_file.txt'
result_file_name = 'file_with_every_nth_line.txt'
extract_frequency = 20


with open(from_file_name) as from_file:
    lines = from_file.readlines()
    result_file = open(result_file_name, 'w')
    result_lines = lines[0::extract_frequency]
    for line in result_lines:
        result_file.write(line)

from_file.close()
result_file.close()