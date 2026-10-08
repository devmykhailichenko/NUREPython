#Hello\nfirst\nsecond
#^     ^
import sys

file_o = open("test.txt", "r")
content = file_o.read(5)
position = file_o.tell()
print(content, position)

content = file_o.read(5)
position = file_o.tell()
print(content, position)

file_o.seek(1)
content = file_o.read(5)
position = file_o.tell()
print(content, position)

file_o.close()

file_o = open("test.txt", "r")
# line1 = file_o.readline()
# line2 = file_o.readline()
# line3 = file_o.readline()
# line4 = file_o.readline()
# line5 = file_o.readline()
# line6 = file_o.readline()

lines = file_o.readlines()

# print(line5)
# print(line6)
print(lines)

file_o.close()

#-------#
file_o = open("test.txt", "r")

for line in file_o:
    print(line)

file_o.close()

#-----#
lines_list = ['First\n', 'Second\n', 'Third\n', 'Fourth\n', 'WRITE']

file_i = open("test.txt", "a")

file_i.write("test\n")
file_i.writelines(lines_list)

file_i.close()

#---------#
with open("text.txt", "w+") as file_descriptor:
    data = file_descriptor.read()
    print(data)
    file_descriptor.write("write+")

def func1():
    pass

