##
##
## Jumble - Reads a list of lines in a file and then jumbles them up
##
##

import random
import sys

# Seed random number generator based on time only
random.seed()

#' (1,1)  (1,4)  leaving (1,2,3,5)
#' (2,2)  (2,3)  leaving (1,2,5)
#' (3,3)  (3,1)  leaving (2,5)
#' (4,4)  (4,5)  leaving (2)=
#' (5,5)  (5,2)  leaving ()

def jumble(inputlines):
    # Jumble up lines
    jumbledlines = []
    # Lets work out a list of numbers - more efficient to do indexes !!
    inputlines_count = len(inputlines)
    linemappings = []
    indexes = range(0, inputlines_count)
    for index in range(0,inputlines_count):
        # OK, have to work out a random index into indexes
        subindex = random.randint(0,len(indexes)-1)
        linemappings.append(indexes[subindex])
        # While we're at it lets assign the line.
        jumbledlines.append(inputlines[indexes[subindex]])
        # print "Swapping line %d from %d" % (index,indexes[subindex])
        # Now remove that entry.
        del indexes[subindex]
    if not len(inputlines)==len(jumbledlines):
        print "Error jumble.py - Jumbled lines mismatch with inputlines"
    return jumbledlines

def readfile(filename):
    filelines = ()
    f1 = open(filename,'r')
    # Now read all the lines - Hey not too big a file please ...
    # A better jumbler would be able to handle big files by starting at
    # random areas (after getting file size to see if it was appropriate)
    filelines = f1.readlines()
    f1.close()
    return filelines

def writefile(filename, lines):
    f1 = open(filename,'w')
    # Now write out all the lines
    for line in lines:
        f1.write(line)
    f1.close()
    return

def Jumble_Up(filename):
    writefile(jumble_file, jumble(readfile(jumble_file)))

try:
	jumble_file = sys.argv[1]
except:
	jumble_file = 'testlist.txt'

#test if not exist
Jumble_Up(jumble_file)

