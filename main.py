file = open('wikipedia_russia.html')

string = ''

cnt_lines = 0
for line in file:
    cnt_lines += 1
    string += line

print(f"numb lines: {cnt_lines}")
print(f"total length: {len(string)}")