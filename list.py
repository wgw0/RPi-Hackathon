link_array = []


f = open("file.txt", "r")

for line in f:
    link_array.append(line.strip())

print(link_array)