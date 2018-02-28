'''
Created on 28 Feb 2018

@author: Slaporter
'''

class lightTester:
    lights=None
    
    def __init__(self,n):
        self.lights = [[False]*(n+1) for _ in range(n+1)]
        self.count = 0
        
    def apply(self, cmd):


        if cmd[0] == "switch":
            for i in range(cmd[1],cmd[3]+1):
                for j in range(cmd[2],cmd[4]+1):
                    if self.lights[i][j]==False:
                        self.count +=1
                        self.lights[i][j]=True
                    else:
                        self.count-=1
                        self.lights[i][j]=False
        elif cmd[0] == "turn on":
            for i in range(cmd[1],cmd[3]+1):
                for j in range(cmd[2],cmd[4]+1):
                    if self.lights[i][j]==False:
                        self.count +=1
                        self.lights[i][j]=True     
        elif cmd[0] == "turn off":
            for i in range(cmd[1],cmd[3]+1):
                for j in range(cmd[2],cmd[4]+1):
                    if self.lights[i][j]==True:
                        self.count -=1
                        self.lights[i][j]=False 

        
    def count(self):
        return self.count