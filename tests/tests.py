'''
Created on 1 Mar 2018

@author: Slaporter
'''
import sys
sys.path.append(".")


from countMeIn.main import main, parse_file, script_run
from countMeIn.lightTester import lightTester

# def test_main():
#     assert 4==4
    
def test_parse_file():
    answer=[10, ['turn on', 0,0,9,9], ['turn off', 0,0, 9,9], ['switch', 0,0,9,9], ['turn off', 0,0,9,9], ['turn on', 2,2,7,7]]
    assert answer==parse_file('input_test')

#     
# def test_script_run():
#     assert
#     
# def test_lightester_apply():


