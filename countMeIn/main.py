'''
Created on 28 Feb 2018

@author: Slaporter
'''
def main(filename):
    instructions=parse_file(filename)
    lights=lightTester(instructions[0])
    for cmd in instructions:
        lights.apply(cmd)
    print("Number of lights on:",lights.count())
    
def parse_file(filename):
    pass


    