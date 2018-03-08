'''
Created on 1 Mar 2018

@author: Slaporter
'''
import sys
sys.path.append(".")


from countMeIn.main import main, parse_file, script_run
from countMeIn.lightTester import lightTester

    
def test_parse_file():
    answer=[10, ['turn on', 0,0,9,9], ['turn off', 0,0, 9,9], ['switch', 0,0,9,9], ['turn off', 0,0,9,9], ['turn on', 2,2,7,7]]
    assert answer==parse_file('input_test')

     
def test_turn_on():
    lt=lightTester(10)
    lt.turn_on(["turn on", 0, 0, 9, 9])
    assert lt.count==100

def test_turn_off():
    lt=lightTester(10)
    lt.turn_on(["turn on", 0, 0, 9, 9])
    lt.turn_off(["turn off", 0, 0, 9, 9])
    assert lt.count==0

def test_switch():
    lt=lightTester(10)
    lt.turn_on(["switch", 0, 0, 9, 9])
    assert lt.count==100



