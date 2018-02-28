'''
Created on 28 Feb 2018

@author: Slaporter
'''
import re
from countMeIn.lightTester import lightTester


def main(filename):
    instructions=parse_file(filename)
    lights=lightTester(instructions[0])
    for cmd in instructions[1:]:
        lights.apply(cmd)
    print("Number of lights on:", lights.count)
    
def parse_file(filename):
    fh1=open(filename).read().splitlines()
    rex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
    my_list=[int(fh1[0])]
    for line in fh1[1:]:
        rexy = rex.match(line)
        my_cmd=[]
        for i in range(1,6):
            if i==1:
                my_cmd.append(rexy.group(i))
            else:
                my_cmd.append(int(rexy.group(i)))    
        my_list.append(my_cmd)
    return my_list
    
parse_file("../input_test")
main("../input_test")
    