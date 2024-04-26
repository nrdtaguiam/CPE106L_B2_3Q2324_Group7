filename = input('Enter file name: ')
lines = []
with open(filename, 'r') as f:
    for line in f:
        lines.append(line.strip())
    print("The file has", len(lines), "lines.")
    while True:
        if len(lines) == 0:
            break
        lineNumber = int(input("Enter a line number [0 to quit]: "))
        if lineNumber == 0:
            break
        elif lineNumber > len(lines):
            print("ERROR: line number must be less than or equal to", len(lines))
        else:
            print(lineNumber, ": ", lines[lineNumber - 1], "\n")
