with open("input6.txt") as input:
  for line in input.readlines():
    windowsize = 4
    for i in range(windowsize-1,len(line)):
      if len(set(line[i-windowsize:i])) == windowsize:
        print("Part 1: "+str(i))
        break

with open("input6.txt") as input:
  for line in input.readlines():
    windowsize = 14
    for i in range(windowsize-1,len(line)):
      if len(set(line[i-windowsize:i])) == windowsize:
        print("Part 2: "+str(i))
        break