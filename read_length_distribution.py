#!/usr/bin/env python

### This script is to calculate the length of each read and then create a graph to show the distribution of the lengths


import argparse
import gzip

def get_args():
    parser=argparse.ArgumentParser(description="Getting files and length")
    parser.add_argument("-o", help= "Forward Read " )
    parser.add_argument("-t", help= "Reverse Read" )

    return parser.parse_args()

args=get_args() ### gets you your function 

o = args.o
t = args.t

#######################################################################################################################
## dictionary for count
count_dict_forward = {}
count_dict_reverse = {}
#######################################################################################################################
with gzip.open(o,"rt") as read1:
    i = 0
    for line in read1:
        i+=1
        if i%4==2:
            line =line.strip()
            length = len(line)
            if length in count_dict_forward:
                count_dict_forward[length] +=1

            else:
                count_dict_forward[length] = 0
                count_dict_forward[length] += 1

#print(count_dict_forward)

import matplotlib.pylab as plt

lists = sorted(count_dict_forward.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y,"-r", label = "Forward")
plt.xlabel("Length of Trimmed Reads")
plt.ylabel("Count")
plt.title(o)
plt.savefig("Forward_pair_both")


with gzip.open(t,"rt") as read2:
    i = 0
    for line in read2:
        i+=1
        if i%4==2:
            line =line.strip()
            length = len(line)
            if length in count_dict_reverse:
                count_dict_reverse[length] +=1

            else:
                count_dict_reverse[length] = 0
                count_dict_reverse[length] += 1

#print(count_dict_forward)

lists2 = sorted(count_dict_reverse.items()) # sorted by key, return a list of tuples

x, y = zip(*lists2) # unpack a list of pairs into two tuples

plt.plot(x, y,"-b", label ="reverse")
plt.xlabel("Length of Trimmed Reads")
plt.ylabel("Count")
plt.legend(loc = "upper left")
plt.title("Forward and Reverse fox_s21")
plt.savefig("forward_reverse_pair_fox")
