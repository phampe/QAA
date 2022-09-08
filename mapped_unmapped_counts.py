#!/usr/bin/env python

mapped:int=0
unmapped:int=0

dir ="/projects/bgmp/ppham4/bioinfo/Bi621/PS/PS8/align"

file="/projects/bgmp/ppham4/bioinfo/Bi623/work/align_fox/foxAligned.out.sam"

with open(file,"r") as sam:
    for line in sam:
        #print(line)
        if line[0] != "@":    # Only make it get the first value in the strin. if line.startswith(<character>) is another method
            #print(line)
            line_list=line.split("\t")
            flag=int(line_list[1])
            
            #print(flag)
            
            # if((flag & 4)!=4):
            #     ##this looks to see if there is a mapped cause it does not equal to 4
            #     #mapped=True

            #     if((flag & 256)!=256):
            #         ### this double checks that there isn't a secondary alignment at the 256 bit position
            #         mapped+=1

            # elif((flag & 4) ==4):

            #     unmapped+=1

            if((flag & 256) != 256):

                if((flag & 4) !=4):
                    mapped +=1

                elif((flag & 4) ==4):
                    unmapped +=1

print("mapped is :", mapped)
print("unmapped is :", unmapped)
