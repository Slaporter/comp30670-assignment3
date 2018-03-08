'''
Created on 28 Feb 2018

@author: Slaporter
'''

class lightTester:
    lights=None
    
    def __init__(self,n):
        self.lights = [[False]*(n+1) for _ in range(n+1)]
        self.count = 0
        
    def turn_on(self,cmd):
        for i in range(cmd[1],cmd[3]+1):
                for j in range(cmd[2],cmd[4]+1):
                    if self.lights[i][j]==False:
                        self.count +=1
                        self.lights[i][j]=True
                        
    def turn_off(self,cmd):
        for i in range(cmd[1],cmd[3]+1):
                for j in range(cmd[2],cmd[4]+1):
                    if self.lights[i][j]==True:
                        self.count -=1
                        self.lights[i][j]=False 
                        
    def switch(self,cmd):
        for i in range(cmd[1],cmd[3]+1):
                for j in range(cmd[2],cmd[4]+1):
                    if self.lights[i][j]==False:
                        self.count +=1
                        self.lights[i][j]=True
                    else:
                        self.count-=1
                        self.lights[i][j]=False
    
    def apply(self, cmd):
        if cmd[0] == "switch":
            self.switch(cmd)
        elif cmd[0] == "turn on":
            self.turn_on(cmd)              
        elif cmd[0] == "turn off":
            self.turn_off(cmd)
        
    def count(self):
        return self.count