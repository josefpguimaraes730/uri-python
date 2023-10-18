#python -i uri.py < in.txt > out.txt

#solution algorithm
def solve(line):
  print(line)
  return

#remove \n came from stdin
def formatLine(line):
    linebreak = line.find('\n')
    return line[:linebreak] if linebreak > 0 else line

#main function gets the input
import sys

for line in sys.stdin:
    solve(formatLine(line))

